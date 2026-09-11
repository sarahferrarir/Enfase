import json, re, sys, zipfile
from collections import Counter
from xml.etree.ElementTree import iterparse

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
REL_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

def col_num(ref):
    letters = re.match(r"[A-Z]+", ref).group(0)
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n - 1

path = sys.argv[1]
with zipfile.ZipFile(path) as z:
    strings = []
    with z.open("xl/sharedStrings.xml") as f:
        for event, elem in iterparse(f, events=("end",)):
            if elem.tag == NS + "si":
                strings.append("".join(t.text or "" for t in elem.iter(NS + "t")))
                elem.clear()

    wb = iterparse(z.open("xl/workbook.xml"), events=("end",))
    sheets = []
    for _, elem in wb:
        if elem.tag == NS + "sheet":
            sheets.append((elem.attrib["name"], elem.attrib[REL_NS + "id"]))
    rels = {}
    for _, elem in iterparse(z.open("xl/_rels/workbook.xml.rels"), events=("end",)):
        if elem.tag.endswith("Relationship"):
            rels[elem.attrib["Id"]] = "xl/" + elem.attrib["Target"].lstrip("/")

    out = {"source": path, "shared_strings": len(strings), "sheets": []}
    for sheet_name, rid in sheets:
        target = rels[rid]
        headers = []
        samples = []
        row_count = 0
        max_col = 0
        nonempty_by_col = Counter()
        unique_by_col = {}
        with z.open(target) as f:
            for _, row in iterparse(f, events=("end",)):
                if row.tag != NS + "row":
                    continue
                row_count += 1
                vals = {}
                for c in row.findall(NS + "c"):
                    ref = c.attrib.get("r", "A1")
                    ci = col_num(ref)
                    max_col = max(max_col, ci + 1)
                    typ = c.attrib.get("t")
                    v = c.find(NS + "v")
                    inline = c.find(NS + "is")
                    val = None
                    if typ == "s" and v is not None and v.text is not None:
                        val = strings[int(v.text)]
                    elif typ == "inlineStr" and inline is not None:
                        val = "".join(t.text or "" for t in inline.iter(NS + "t"))
                    elif v is not None:
                        val = v.text
                    if val not in (None, ""):
                        vals[ci] = val
                        nonempty_by_col[ci] += 1
                        if row_count <= 5000:
                            unique_by_col.setdefault(ci, set()).add(str(val)[:500])
                if row_count == 1:
                    headers = [vals.get(i) for i in range(max(vals.keys(), default=-1)+1)]
                elif row_count <= 8:
                    samples.append([vals.get(i) for i in range(max(max_col, len(headers)))])
                row.clear()
        out["sheets"].append({
            "name": sheet_name,
            "target": target,
            "rows": row_count,
            "cols": max_col,
            "headers": headers,
            "samples": samples,
            "nonempty_by_col": dict(nonempty_by_col),
            "unique_first_5000_by_col": {str(k): len(v) for k,v in unique_by_col.items()},
        })
    print(json.dumps(out, ensure_ascii=False, indent=2))
