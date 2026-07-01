# Guia de Teste

Este guia cobre apenas execucao e validacao da versao atual do conversor.

## Pre-requisitos

- Python 3.10+.
- Ambiente virtual `.venv` criado na raiz de `ConversorInformativoSTF`.
- Dependencias instaladas:

```bash
cd /Users/sarahferrarir/Enfase/ConversorInformativoSTF
./.venv/bin/python -m pip install -r requirements.txt
```

O fluxo atual nao exige Ollama nem LLM.

## Comandos Basicos

Compilar os modulos:

```bash
./.venv/bin/python -m compileall src
```

Rodar testes unitarios:

```bash
./.venv/bin/python -m unittest discover -s tests
```

Converter um DOCX:

```bash
./.venv/bin/python -m src.converter exemplos/Informativo1222.docx -o /tmp/Informativo1218_teste.json
```

## Teste com Informativo 1214

```bash
./.venv/bin/python -m src.converter exemplos/Informativo1214.docx -o /tmp/Informativo1214_teste.json
jq '.julgado_stf | length' /tmp/Informativo1214_teste.json
jq '.julgado_stf[] | {titulo, classe_processo, numero_processo, resumo, noticia, html}' /tmp/Informativo1214_teste.json
```

Validacoes esperadas:

- o comando roda sem erro;
- a quantidade de itens permanece `4`;
- cada item possui `titulo`, `classe_processo` e `numero_processo`;
- `resumo`, `noticia` e `html` contem HTML com `<p>`;
- linhas finais de processos aparecem como lista HTML quando aplicavel;
- nao aparecem `SUMÁRIO`, `2 TURMAS`, `INOVAÇÕES NORMATIVAS`, `base64` ou `<img>`.

## Teste com Informativo 1218

```bash
./.venv/bin/python -m src.converter exemplos/Informativo1218.docx -o /tmp/Informativo1218_teste.json
jq '.julgado_stf | length' /tmp/Informativo1218_teste.json
jq '.julgado_stf[] | {titulo, classe_processo, numero_processo, tema_rg, repercussao_geral, resumo, noticia, html}' /tmp/Informativo1218_teste.json
```

Validacoes esperadas:

- o comando roda sem erro;
- a quantidade de itens permanece `5`;
- o item `RE 597.315/RJ` possui `tema_rg: "516 RG"`;
- o mesmo item possui `repercussao_geral: "sim"`;
- o titulo desse item nao contem `(Tema 516 RG)`;
- temas citados em precedentes, como `(Tema 323 RG)` e `(Tema 177 RG)`, nao viram tema principal;
- `resumo`, `noticia` e `html` contem HTML com `<p>`.

## Checagens Rapidas

Contar itens:

```bash
jq '.julgado_stf | length' /tmp/Informativo1214_teste.json
jq '.julgado_stf | length' /tmp/Informativo1218_teste.json
```

Verificar campos principais:

```bash
jq '.julgado_stf[] | {titulo, classe_processo, numero_processo}' /tmp/Informativo1214_teste.json
```

Verificar HTML:

```bash
jq '[.julgado_stf[].resumo, .julgado_stf[].noticia, .julgado_stf[].html]
    | map(select(. != null))
    | {p: map(test("<p>")) | any,
       a: map(test("<a target=\"_blank\"")) | any,
       ul: map(test("<ul>")) | any}' /tmp/Informativo1214_teste.json
```

Verificar secoes ou conteudo indesejado:

```bash
grep -Eio 'SUMÁRIO|SUMARIO|2 TURMAS|INOVAÇÕES NORMATIVAS|base64|<img' /tmp/Informativo1214_teste.json
grep -Eio 'SUMÁRIO|SUMARIO|2 TURMAS|INOVAÇÕES NORMATIVAS|base64|<img' /tmp/Informativo1218_teste.json
```

Se os comandos `grep` nao retornarem nada, a checagem passou.
