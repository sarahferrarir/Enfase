import json, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "analysis"

def clean(v):
    if v is None: return None
    s = " ".join(str(v).strip().split())
    return s or None

def key(v):
    v = clean(v)
    return unicodedata.normalize("NFKD", v).encode("ascii", "ignore").decode().casefold() if v else None

rows = [json.loads(x) for x in open(DATA_DIR / "metadata.jsonl", encoding="utf-8")]
fields = ["NM Ano","NM Banca","NM Órgão","NM Cargo","NM Curso","NM Edição","NM BLOCO","NM Base Produto Vinculado","Nome Resumido"]
summary = {"rows": len(rows), "fields": {}, "combinations": {}}
for f in fields:
    vals = [clean(r.get(f)) for r in rows]
    c = Counter(v for v in vals if v is not None)
    variants = defaultdict(set)
    for v in c: variants[key(v)].add(v)
    summary["fields"][f] = {
        "non_null": sum(v is not None for v in vals),
        "null": sum(v is None for v in vals),
        "unique": len(c),
        "top": c.most_common(30),
        "normalization_collisions": [sorted(x) for x in variants.values() if len(x)>1],
    }
for name, fs in {
    "ano_banca_orgao_cargo_curso": ["NM Ano","NM Banca","NM Órgão","NM Cargo","NM Curso"],
    "ano_banca_orgao_cargo": ["NM Ano","NM Banca","NM Órgão","NM Cargo"],
    "orgao_cargo": ["NM Órgão","NM Cargo"],
}.items():
    c=Counter(tuple(clean(r.get(f)) for f in fs) for r in rows)
    summary["combinations"][name]={"unique":len(c),"top":[[list(k),v] for k,v in c.most_common(30)]}

id_name_pairs = [("ID Ano","NM Ano"),("ID Banca","NM Banca"),("ID Órgão","NM Órgão"),("ID Cargo","NM Cargo"),("ID Curso","NM Curso")]
conflicts={}
for fid, fname in id_name_pairs:
    id_to_names=defaultdict(Counter); name_to_ids=defaultdict(Counter)
    for r in rows:
        i,n=clean(r.get(fid)),clean(r.get(fname))
        if i and n:
            id_to_names[i][n]+=1; name_to_ids[n][i]+=1
    conflicts[fid]={
      "ids_with_multiple_names": {i:dict(c) for i,c in id_to_names.items() if len(c)>1},
      "names_with_multiple_ids": {n:dict(c) for n,c in name_to_ids.items() if len(c)>1},
    }
summary["id_name_conflicts"]=conflicts
json.dump(summary,open(DATA_DIR / "summary.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print(json.dumps({"rows":summary["rows"],"unique":{f:d["unique"] for f,d in summary["fields"].items()},"combos":summary["combinations"],"conflict_counts":{f:{k:len(v) for k,v in d.items()} for f,d in conflicts.items()}},ensure_ascii=False,indent=2))
