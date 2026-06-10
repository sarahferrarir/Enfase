# Conversor de Informativos STF

Conversor deterministico de Informativos do STF em DOCX para JSON estruturado.

A versao atual nao usa LLM, Ollama ou chunking como fluxo principal. O pipeline ativo usa leitura direta do DOCX por XML, isolamento da secao Plenario, separacao deterministica dos itens editoriais, extracao estruturada dos campos e geracao de HTML para campos textuais.

## Objetivo

Gerar JSONs de julgados do STF a partir de Informativos em DOCX, preservando:

- campos estruturais do julgado;
- texto do resumo, noticia e noticia completa;
- HTML basico dos campos textuais;
- links, negrito, italico, sublinhado e listas quando presentes no DOCX.

## Arquitetura Atual

Fluxo principal:

```text
DOCX
  -> leitura XML do documento
  -> extracao de paragrafos, runs, estilos e links
  -> extracao de metadados do informativo
  -> isolamento da secao 1 Plenario
  -> separacao deterministica de itens editoriais
  -> extracao dos campos estruturados
  -> formatacao HTML dos campos textuais
  -> JSON final
```

## Estrutura

```text
ConversorInformativoSTF/
├── exemplos/                 # DOCX/JSONs de exemplo; nao editar manualmente
├── src/
│   ├── converter.py          # CLI e orquestracao do pipeline
│   ├── document_reader.py    # leitura DOCX via XML e relacoes de links
│   ├── metadata_extractor.py # numero, ano e data do informativo
│   ├── section_extractor.py  # isolamento da secao Plenario
│   ├── editorial_item_splitter.py # separacao deterministica dos itens
│   ├── field_extractor.py    # campos estruturados do julgado
│   ├── html_formatter.py     # HTML para campos textuais
│   ├── schemas.py            # modelos Pydantic
│   ├── utils.py              # utilitarios compartilhados
│   └── validator.py          # avisos simples de validacao
├── tests/                    # testes unitarios leves
├── requirements.txt
├── GUIA_TESTE.md
└── RESUMO_IMPLEMENTACAO.md
```

## Campos Extraidos

Principais campos gerados:

- `informativo`
- `data_informativo`
- `classe_processo`
- `numero_processo`
- `uf`
- `titulo`
- `ramo_direito`
- `materia`
- `resumo`
- `noticia`
- `noticia_completa`
- `html`
- `tese_julgado`
- `legislacao`
- `ods_onu2030`
- `tema_rg`
- `repercussao_geral`
- `relator`
- `redator_acordao`
- `data_julgamento`
- `situacao_julgamento`

Os campos textuais saem em HTML simples quando ha conteudo formatado no DOCX.

## Como Executar

```bash
cd /Users/sarahferrarir/Enfase/ConversorInformativoSTF
./.venv/bin/python -m src.converter exemplos/Informativo1218.docx -o /tmp/Informativo1218.json
```

Sem `-o`, o conversor grava o JSON ao lado do DOCX:

```bash
./.venv/bin/python -m src.converter exemplos/Informativo1218.docx
```

## Exemplo de Saida

```json
{
  "julgado_stf": [
    {
      "informativo": "1218",
      "classe_processo": "RE",
      "numero_processo": "597315",
      "uf": "RJ",
      "titulo": "Sujeição passiva das cooperativas à contribuição destinada ao custeio da seguridade social",
      "tema_rg": "516 RG",
      "repercussao_geral": "sim",
      "resumo": "<p>...</p>",
      "noticia": "<p>...</p>"
    }
  ]
}
```

## Testes

Os comandos operacionais e validacoes esperadas ficam em [GUIA_TESTE.md](GUIA_TESTE.md).

O historico das decisoes de implementacao fica em [RESUMO_IMPLEMENTACAO.md](RESUMO_IMPLEMENTACAO.md).
