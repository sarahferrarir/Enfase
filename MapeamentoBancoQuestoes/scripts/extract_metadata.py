import json, re, sys, zipfile
from pathlib import Path
from xml.etree.ElementTree import iterparse

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"

def col_num(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(0):
        n = n * 26 + ord(ch) - 64
    return n - 1

def shared_strings(z):
    result = []
    for _, elem in iterparse(z.open("xl/sharedStrings.xml"), events=("end",)):
        if elem.tag == NS + "si":
            result.append("".join(t.text or "" for t in elem.iter(NS + "t")))
            elem.clear()
    return result

def rows(z, target, strings):
    for _, row in iterparse(z.open(target), events=("end",)):
        if row.tag != NS + "row":
            continue
        vals = {}
        for c in row.findall(NS + "c"):
            ci = col_num(c.attrib.get("r", "A1"))
            typ = c.attrib.get("t")
            v = c.find(NS + "v")
            val = None
            if typ == "s" and v is not None and v.text is not None:
                val = strings[int(v.text)]
            elif typ == "inlineStr":
                val = "".join(t.text or "" for t in c.iter(NS + "t"))
            elif v is not None:
                val = v.text
            vals[ci] = val
        yield int(row.attrib.get("r", 0)), vals
        row.clear()

src = sys.argv[1]
outdir = Path(sys.argv[2])
outdir.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(src) as z:
    ss = shared_strings(z)
    it = rows(z, "xl/worksheets/sheet1.xml", ss)
    _, header_vals = next(it)
    headers = {i: v for i, v in header_vals.items()}
    wanted = [
        "Id da Questao", "ID Ano", "ID Banca", "ID Órgão", "ID Cargo", "ID Curso",
        "ID Edição", "ID BLOCO", "ID Base Produto Vinculado", "NM Ano", "NM Banca",
        "NM Órgão", "NM Cargo", "NM Curso", "NM Edição", "NM BLOCO",
        "NM Base Produto Vinculado", "Nome Resumido", "Tipo(O=Objetiva, D=Discursiva, R=Oral"
    ]
    idx = {name: i for i, name in headers.items() if name in wanted}
    with (outdir / "metadata.jsonl").open("w", encoding="utf-8") as f:
        for rownum, vals in it:
            rec = {name: vals.get(i) for name, i in idx.items()}
            rec["_sheet"] = "Base_sem duplic"
            rec["_row"] = rownum
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    list_it = rows(z, "xl/worksheets/sheet3.xml", ss)
    _, list_headers = next(list_it)
    with (outdir / "lista.jsonl").open("w", encoding="utf-8") as f:
        for rownum, vals in list_it:
            rec = {list_headers.get(i, str(i)): v for i, v in vals.items()}
            rec["_sheet"] = "Lista"
            rec["_row"] = rownum
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
