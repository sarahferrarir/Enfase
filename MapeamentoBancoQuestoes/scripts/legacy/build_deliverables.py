import hashlib, json, re, unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

OUT=Path('.')
EXTRACTION="2026-07-31"
SOURCE_FILE="Base Questões Concurso_Completa_para Adriano_13.07.26.xlsx"

def clean(v):
    if v is None: return None
    s=" ".join(str(v).strip().split())
    return s or None
def sid(prefix,*parts):
    raw="|".join("" if p is None else str(p) for p in parts)
    return f"{prefix}_{hashlib.sha256(raw.encode()).hexdigest()[:16]}"
def md(v): return "—" if v is None else str(v).replace("|","\\|")

rows=[json.loads(x) for x in open('analysis-data/metadata.jsonl',encoding='utf-8')]
for r in rows:
    for k,v in list(r.items()): r[k]=clean(v) if not k.startswith('_') else v

groups=defaultdict(list)
for r in rows:
    k=(r.get('ID Ano'),r.get('ID Banca'),r.get('ID Órgão'),r.get('ID Cargo'),r.get('ID Curso'))
    groups[k].append(r)

records=[]
for key,rs in groups.items():
    a,b,o,c,car=key; first=rs[0]
    concurso_id=sid('concurso',a,b,o,c,car)
    nome=" — ".join(x for x in [first.get('NM Órgão'),first.get('NM Cargo'),first.get('NM Ano')] if x) or None
    qids=[r.get('Id da Questao') for r in rs if r.get('Id da Questao')]
    rownums=[r['_row'] for r in rs]
    records.append({
      'concurso_id':concurso_id,'concurso_nome':nome,'concurso_nome_tipo':'rotulo_tecnico_derivado',
      'carreira_id':f"curso_enfase_{car}" if car else None,'carreira_nome':first.get('NM Curso'),
      'orgao_id':f"orgao_enfase_{o}" if o else None,'orgao_nome':first.get('NM Órgão'),
      'banca_id':f"banca_enfase_{b}" if b else None,'banca_nome':first.get('NM Banca'),
      'cargo':first.get('NM Cargo'),'prova':None,
      'ano':int(first['NM Ano']) if first.get('NM Ano','').isdigit() else None,'data_prova':None,
      'status_data':'sem_data','edicoes':sorted({r.get('NM Edição') for r in rs if r.get('NM Edição')}),
      'blocos':sorted({r.get('NM BLOCO') for r in rs if r.get('NM BLOCO')}),
      'origem_interna':{'arquivo':SOURCE_FILE,'aba':'Base_sem duplic','criterio_filtro':{
          'ID Ano':a,'ID Banca':b,'ID Órgão':o,'ID Cargo':c,'ID Curso':car},
          'quantidade_questoes':len(rs),'linhas_min_max':[min(rownums),max(rownums)],
          'questoes_id_amostra':qids[:10]},
      'observacoes':['Concurso não é campo de origem; nome e ID são rótulos técnicos derivados.',
                     'Prova e data_prova ausentes na planilha; não inferidos.'],
      'qualidade_dado':{'nivel':'parcial','campos_confirmados_internamente':['ano','banca','orgao','cargo','carreira'],
                        'campos_ausentes':['prova','data_prova'],'validacao_externa_do_certame':False}
    })
records.sort(key=lambda x:(x['ano'] or 0,x['orgao_nome'] or '',x['cargo'] or '',x['banca_nome'] or ''))

def catalog(idf,namef,prefix):
    d={}
    for r in rows:
        i,n=r.get(idf),r.get(namef)
        if i:
            d.setdefault(i,{'id':f'{prefix}_enfase_{i}','id_interno':i,'nome':n,'quantidade_questoes':0})
            d[i]['quantidade_questoes']+=1
    return sorted(d.values(),key=lambda x:(x['nome'] or ''))

catalogs={'carreiras':catalog('ID Curso','NM Curso','curso'),'orgaos':catalog('ID Órgão','NM Órgão','orgao'),
          'bancas':catalog('ID Banca','NM Banca','banca'),'cargos':catalog('ID Cargo','NM Cargo','cargo'),
          'anos':catalog('ID Ano','NM Ano','ano')}

quality={
 'total_questoes':len(rows),'total_registros_concurso_tecnico':len(records),
 'totais_catalogo':{k:len(v) for k,v in catalogs.items()},
 'lacunas':{
   'prova':len(records),'data_prova':len(records),
   'cargo_em_questoes':sum(r.get('NM Cargo') is None for r in rows),
 },
 'alertas':["A coluna NM Banca contém '(TESTE) Cargo XY' em registros produtivos.",
            "CESPE e CEBRASPE aparecem como bancas/IDs distintos; não foram fundidos.",
            "O nome de órgão 'PGE/PA' aparece associado a mais de um ID interno.",
            "Nome Resumido possui 489 valores, enquanto a chave técnica gera 485 combinações; não foi usado como chave."]
}

inventory={'schema_version':'1.0.0','data_extracao':EXTRACTION,'arquivo_origem':SOURCE_FILE,
 'metodologia':{'unidade_registro':'combinação de ID Ano, ID Banca, ID Órgão, ID Cargo e ID Curso',
 'normalizacao':'trim e colapso de espaços; nomes preservados; IDs internos preservados; sem fusão por similaridade',
 'regra_null':'informação ausente ou não confirmada recebe null','identificadores':'IDs internos quando existentes; concurso_id SHA-256 truncado da chave interna'},
 'definicoes':{
  'concurso':'Entidade técnica derivada da combinação ano+banca+órgão+cargo+curso; não equivale necessariamente ao nome oficial do edital.',
  'carreira':'Curso/trilha comercial do Ênfase (campo ID/NM Curso), usado como aproximação interna de carreira.',
  'orgao':'Órgão/instituição informado nos campos ID/NM Órgão.','banca':'Organizadora informada nos campos ID/NM Banca.',
  'prova':'Evento/caderno específico; não há campo próprio na origem.','cargo':'Cargo informado nos campos ID/NM Cargo.'},
 'resumo_qualidade':quality,'catalogos':catalogs,'registros':records}
json.dump(inventory,open('inventario-banco-questoes.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)

sources=[
 {'fonte_id':'fonte_dou','nome':'Diário Oficial da União','url':'https://www.in.gov.br/','entidade_responsavel':'Imprensa Nacional / Casa Civil','tipo':'diario_oficial','informacao_publicada':['editais','autorizações','resultados','nomeações'],'periodicidade_sugerida':'diária em dias úteis','ultima_verificacao':EXTRACTION,'evidencia_verificacao':'https://www.gov.br/pt-br/servicos/acessar-o-diario-oficial-da-uniao','criterio_vinculo':{'esfera':'federal'}},
 {'fonte_id':'fonte_cebraspe','nome':'Cebraspe — concursos','url':'https://www.cebraspe.org.br/Concursos/','entidade_responsavel':'Cebraspe','tipo':'banca','informacao_publicada':['concursos em andamento','encerrados','editais','comunicados','resultados'],'periodicidade_sugerida':'semanal; diária durante inscrições/provas','ultima_verificacao':EXTRACTION,'evidencia_verificacao':'https://www.cebraspe.org.br/Concursos/','criterio_vinculo':{'banca_nomes':['CEBRASPE','CESPE']}},
 {'fonte_id':'fonte_fgv','nome':'FGV Conhecimento — concursos e exames','url':'https://conhecimento.fgv.br/concursos','entidade_responsavel':'Fundação Getulio Vargas','tipo':'banca','informacao_publicada':['editais','cronogramas','comunicados','gabaritos','resultados'],'periodicidade_sugerida':'semanal; diária durante inscrições/provas','ultima_verificacao':EXTRACTION,'evidencia_verificacao':'https://conhecimento.fgv.br/cpnu2','criterio_vinculo':{'banca_nomes':['FGV']}},
 {'fonte_id':'fonte_fcc','nome':'Fundação Carlos Chagas — concursos','url':'https://www1.concursosfcc.com.br/','entidade_responsavel':'Fundação Carlos Chagas','tipo':'banca','informacao_publicada':['próximos concursos','inscrições','gabaritos','resultados'],'periodicidade_sugerida':'semanal; diária durante inscrições/provas','ultima_verificacao':EXTRACTION,'evidencia_verificacao':'https://www1.concursosfcc.com.br/','criterio_vinculo':{'banca_nomes':['FCC']}},
 {'fonte_id':'fonte_vunesp','nome':'Fundação Vunesp — concursos','url':'https://www.vunesp.com.br/','entidade_responsavel':'Fundação Vunesp','tipo':'banca','informacao_publicada':['próximos','inscrições abertas','em andamento','encerrados'],'periodicidade_sugerida':'semanal; diária durante inscrições/provas','ultima_verificacao':EXTRACTION,'evidencia_verificacao':'https://www.vunesp.com.br/','criterio_vinculo':{'banca_nomes':['VUNESP']}},
 {'fonte_id':'fonte_agu','nome':'AGU — concursos e processos seletivos','url':'https://www.gov.br/agu/pt-br/acesso-a-informacao/concursos','entidade_responsavel':'Advocacia-Geral da União','tipo':'orgao','informacao_publicada':['editais','orientações','nomeações','resultados'],'periodicidade_sugerida':'semanal','ultima_verificacao':EXTRACTION,'evidencia_verificacao':'https://www.gov.br/agu/pt-br/acesso-a-informacao/concursos','criterio_vinculo':{'orgao_nomes':['AGU','PGFN']}},
 {'fonte_id':'fonte_cnj_magistratura','nome':'CNJ — concursos de tribunais','url':'https://www.cnj.jus.br/poder-judiciario/concursos-de-tribunais/','entidade_responsavel':'Conselho Nacional de Justiça','tipo':'portal_publico_oficial','informacao_publicada':['painel de concursos da magistratura','ENAM','normas'],'periodicidade_sugerida':'semanal','ultima_verificacao':EXTRACTION,'evidencia_verificacao':'https://www.cnj.jus.br/poder-judiciario/concursos-de-tribunais/','criterio_vinculo':{'cargos':['Juiz de Direito','Juiz Federal','Juiz do Trabalho','ENAM']}},
 {'fonte_id':'fonte_enam_2026_1','nome':'FGV/ENFAM — 5º ENAM (2026.1)','url':'https://conhecimento.fgv.br/exames/enam/5exame','entidade_responsavel':'ENFAM / FGV','tipo':'pagina_certame','informacao_publicada':['edital','cronograma','comunicados','resultados'],'periodicidade_sugerida':'diária até homologação','ultima_verificacao':EXTRACTION,'evidencia_verificacao':'https://conhecimento.fgv.br/sites/default/files/concursos/cronograma_enam-2026.1-1.pdf','criterio_vinculo':{'orgao_nomes':['ENAM'],'ano':2026}}
]
for s in sources:
    crit=s['criterio_vinculo']; linked=[]
    for r in records:
        ok=False
        if r['banca_nome'] in crit.get('banca_nomes',[]): ok=True
        if r['orgao_nome'] in crit.get('orgao_nomes',[]): ok=True
        if r['cargo'] in crit.get('cargos',[]): ok=True
        if crit.get('ano') is not None: ok=ok and r['ano']==crit['ano']
        if crit.get('esfera')=='federal' and r['orgao_nome'] in ['AGU','DPU','MPF','MPT','PF','PGFN','SF','TST','TRF1','TRF2','TRF3','TRF4','TRF5','TRF6']: ok=True
        if ok: linked.append(r['concurso_id'])
    s['concursos_relacionados']=linked

mapped_bancas=set(sum((s['criterio_vinculo'].get('banca_nomes',[]) for s in sources),[]))
future=[{'evento_id':'evento_enam_2026_1_resultado','concurso_id':next((r['concurso_id'] for r in records if r['orgao_nome']=='ENAM' and r['ano']==2026),None),
 'descricao':'Publicação da relação nominal com o resultado definitivo da prova','data':'2026-08-18','status_data':'prevista',
 'fonte_id':'fonte_enam_2026_1','evidencia_url':'https://conhecimento.fgv.br/sites/default/files/concursos/cronograma_enam-2026.1-1.pdf','ultima_verificacao':EXTRACTION,
 'observacao':'O cronograma oficial declara que as datas são passíveis de alteração.'},
 {'evento_id':'evento_enam_2026_1_homologacao','concurso_id':next((r['concurso_id'] for r in records if r['orgao_nome']=='ENAM' and r['ano']==2026),None),
 'descricao':'Homologação do resultado final','data':'2026-08-24','status_data':'prevista','fonte_id':'fonte_enam_2026_1',
 'evidencia_url':'https://conhecimento.fgv.br/sites/default/files/concursos/cronograma_enam-2026.1-1.pdf','ultima_verificacao':EXTRACTION,
 'observacao':'O cronograma oficial declara que as datas são passíveis de alteração.'}]
source_map={'schema_version':'1.0.0','data_ultima_verificacao':EXTRACTION,'politica_fontes':'Somente páginas de entidade pública ou da banca organizadora. URLs não verificadas foram omitidas.',
 'fontes':sources,'eventos_futuros':future,'lacunas':{
  'bancas_sem_fonte_oficial_verificada':sorted({x['nome'] for x in catalogs['bancas'] if x['nome'] not in mapped_bancas}),
  'orgaos_sem_pagina_especifica_verificada':sorted({x['nome'] for x in catalogs['orgaos'] if x['nome'] not in ['AGU','PGFN','ENAM']}),
  'nota':'A ausência nesta lista não significa inexistência de fonte; significa que a URL não foi validada nesta extração.'}}
json.dump(source_map,open('fontes-oficiais-concursos.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)

lines=["# Inventário do banco de questões",f"\n**Data da extração:** {EXTRACTION}  ",f"**Arquivo:** `{SOURCE_FILE}`",
"\n## Visão geral",f"\nForam analisadas **{len(rows):,} questões** (51.190) e identificadas **{len(records)} combinações técnicas** de ano, banca, órgão, cargo e curso/carreira. A cobertura vai de {min(r['ano'] for r in records if r['ano'])} a {max(r['ano'] for r in records if r['ano'])}.",
"\nA planilha não possui campos próprios de nome oficial do concurso, prova, fase ou data de aplicação. Por isso, cada `concurso_id` abaixo identifica uma combinação interna e o nome é um rótulo técnico, não um nome oficial inferido.",
"\n## Entidades e relacionamentos","\n- **Concurso técnico:** combinação de ano, banca, órgão, cargo e curso.","- **Carreira:** corresponde a `NM Curso`, que parece representar a trilha/curso do Ênfase; não foi reinterpretada.","- **Órgão:** entidade indicada por `ID/NM Órgão`.","- **Banca:** organizadora indicada por `ID/NM Banca`.","- **Prova:** não existe como campo autônomo; permanece `null`.","- **Cargo:** função indicada por `ID/NM Cargo`.",
"\n## Cobertura por carreira","\n| ID | Carreira | Questões |","|---|---|---:|"]
for x in catalogs['carreiras']: lines.append(f"| {x['id']} | {md(x['nome'])} | {x['quantidade_questoes']} |")
lines += ["\n## Catálogo de bancas","\n| ID | Banca | Questões |","|---|---|---:|"]
for x in catalogs['bancas']: lines.append(f"| {x['id']} | {md(x['nome'])} | {x['quantidade_questoes']} |")
lines += ["\n## Catálogo de órgãos","\n| ID | Órgão | Questões |","|---|---|---:|"]
for x in catalogs['orgaos']: lines.append(f"| {x['id']} | {md(x['nome'])} | {x['quantidade_questoes']} |")
lines += ["\n## Relação entre concursos técnicos, provas e anos","\n| Concurso ID | Ano | Órgão | Cargo | Banca | Carreira | Prova | Questões |","|---|---:|---|---|---|---|---|---:|"]
for r in records: lines.append(f"| {r['concurso_id']} | {md(r['ano'])} | {md(r['orgao_nome'])} | {md(r['cargo'])} | {md(r['banca_nome'])} | {md(r['carreira_nome'])} | — | {r['origem_interna']['quantidade_questoes']} |")
lines += ["\n## Lacunas e inconsistências","\n- `prova` e `data_prova`: ausentes em todos os 485 registros técnicos.","- `NM Cargo`: ausente em 200 questões.","- `NM Banca` contém o valor anômalo `(TESTE) Cargo XY`.","- `CESPE` e `CEBRASPE` usam IDs distintos; mantidos separados sem inferir equivalência cadastral.","- `PGE/PA` aparece associado a mais de um ID interno.","- `Nome Resumido` tem 489 valores, quatro a mais que a chave técnica; não foi usado como identificador.",
"\n## Metodologia","\n1. Leitura integral das três abas do arquivo OOXML, sem modificação do original.","2. Inventário de cabeçalhos, preenchimento e cardinalidade.","3. Normalização apenas de espaços e valores vazios; nomes e IDs internos preservados.","4. Agrupamento pela chave interna `ID Ano + ID Banca + ID Órgão + ID Cargo + ID Curso`.","5. Geração de identificador estável por SHA-256 truncado; ausência ou incerteza registrada como `null`.","\nO JSON é a fonte estruturada completa e contém os mesmos 485 registros exibidos neste catálogo."]
open('inventario-banco-questoes.md','w',encoding='utf-8').write('\n'.join(lines)+'\n')

fl=["# Fontes oficiais de concursos",f"\n**Última verificação:** {EXTRACTION}","\n## Política","\nForam aceitas apenas páginas oficiais de órgãos públicos e das próprias bancas. Agregadores foram excluídos. Uma URL não verificada não foi incluída como fonte; a lacuna permanece explícita no JSON.","\n## Fontes verificadas","\n| Fonte | Responsável | URL | Conteúdo | Consulta | Concursos vinculados |","|---|---|---|---|---|---:|"]
for s in sources: fl.append(f"| {s['nome']} | {s['entidade_responsavel']} | {s['url']} | {', '.join(s['informacao_publicada'])} | {s['periodicidade_sugerida']} | {len(s['concursos_relacionados'])} |")
fl += ["\n## Datas futuras identificadas","\n| Evento | Data | Status | Evidência |","|---|---|---|---|"]
for e in future: fl.append(f"| {e['descricao']} | {e['data']} | {e['status_data']} | {e['evidencia_url']} |")
fl += ["\nAs duas datas do ENAM são **previstas**, não confirmadas: o próprio cronograma oficial informa que podem ser alteradas.","\n## Lacunas de monitoramento",f"\n- Bancas sem URL oficial verificada nesta rodada: **{len(source_map['lacunas']['bancas_sem_fonte_oficial_verificada'])}**.",f"- Órgãos sem página específica verificada nesta rodada: **{len(source_map['lacunas']['orgaos_sem_pagina_especifica_verificada'])}**.","- O DOU cobre atos federais, mas não substitui os diários estaduais/municipais nem as páginas de cada órgão.","- Não foram atribuídas datas futuras a concursos apenas porque o ano é 2026; sem edital/cronograma oficial, o status é `sem_data`.","\n## Rotina recomendada","\n1. Consultar diariamente páginas de certames ativos e diários oficiais durante janelas críticas.","2. Consultar semanalmente páginas gerais das bancas e órgãos.","3. Registrar URL do edital/comunicado, data de publicação e data de verificação.","4. Classificar datas como `confirmada` somente quando o ato oficial for definitivo; usar `prevista` quando o cronograma admitir alteração; usar `sem_data` quando não houver data oficial.","5. Nunca preencher lacunas com agregadores; registrar `null` e abrir pendência de validação."]
open('fontes-oficiais-concursos.md','w',encoding='utf-8').write('\n'.join(fl)+'\n')
