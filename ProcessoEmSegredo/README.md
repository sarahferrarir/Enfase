# ProcessoEmSegredo

Parser inicial em TypeScript para transformar PDFs de pautas de julgamento do STJ em dados estruturados.

Esta primeira versao e deterministica: nao acessa sites, nao usa banco de dados e nao usa IA.

## Instalar

```bash
npm install
```

## Executar

```bash
npm run parse exemplos/pauta1.pdf
```

O comando imprime:

- tipo da sessao;
- data principal da pauta;
- quantidade de processos encontrados;
- resumo dos primeiros 5 processos.

Ele tambem gera automaticamente um JSON em `outputs/`, sem parametro extra.

Exemplos:

```text
exemplos/pauta1.pdf -> outputs/pauta1.json
exemplos/pauta2.pdf -> outputs/pauta2.json
```

## Saida JSON

O arquivo gerado segue a estrutura:

```json
{
  "metadata": {
    "arquivoOrigem": "pauta1.pdf",
    "tipoSessao": "Ordinária",
    "dataPauta": "17/06/2026",
    "quantidadeProcessos": 22,
    "dataExtracao": "2026-07-08T19:00:00.000Z"
  },
  "processos": [
    {
      "tituloCompleto": "...",
      "classeProcesso": "...",
      "numeroProcesso": "...",
      "uf": "...",
      "numeroRegistro": "...",
      "relator": "...",
      "tipoSessao": "...",
      "dataPauta": "...",
      "textoCompleto": "..."
    }
  ]
}
```

## Arquitetura

```text
src/
  models/
    ProcessoPauta.ts
    PautaMetadata.ts
  parser/
    pdfReader.ts
    textNormalizer.ts
    headerExtractor.ts
    itemSplitter.ts
    fieldExtractor.ts
    pautaParser.ts
  exporter/
    jsonExporter.ts
  index.ts
```

## Estrategia de parsing

O parser extrai o texto do PDF, normaliza espacos e quebras de linha, le o header da pauta e divide os blocos dos processos.

A divisao dos processos nao depende de uma lista fixa de classes ou recursos. O inicio de cada item e identificado pelo padrao processual:

```text
Nº <numero> - <UF> (<registro>)
```

Exemplos:

```text
Nº 2225061 - PE (2025/0281294-7)
Nº 87 - DF (2022/0187319-4)
Nº 1091363 - SC (2008/0217715-7)
```

O `tipoSessao` e a `dataPauta` sao extraidos do header e repetidos em cada processo retornado.
