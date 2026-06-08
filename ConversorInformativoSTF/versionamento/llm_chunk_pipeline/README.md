# LLM Chunk Pipeline

Esta pasta preserva uma versão experimental do `ConversorInformativoSTF` baseada em chunking e LLM/Ollama.

Ela é histórica. A versão atual correta está em `../../src/`.

## O que era

Pipeline experimental para reduzir a dependência de regex rígida usando LLM como etapa central de extração.

Fluxo em alto nível:

1. ler o DOCX;
2. converter/limpar o texto;
3. dividir o conteúdo em chunks;
4. enviar cada chunk para o Ollama;
5. pedir à LLM que identificasse julgados principais e retornasse JSON;
6. validar, deduplicar e salvar a saída final.

## Principais arquivos

- `converter.py`: orquestrador do pipeline com chunks e LLM.
- `document_reader.py`: leitura do DOCX.
- `text_preprocessor.py`: limpeza textual.
- `chunker.py`: divisão do texto em blocos/chunks.
- `ollama_client.py`: cliente local para Ollama.
- `llm_processor.py`: prompts e processamento das respostas da LLM.
- `validator.py`: validação e merge/deduplicação.
- `schemas.py`: modelos Pydantic.
- `utils.py`: utilitários.

## Por que existiu

A ideia era usar a LLM para entender a semântica dos informativos e extrair julgados mesmo quando a estrutura textual variasse.

O experimento foi útil para demonstrar que prompts e validações poderiam apoiar campos interpretativos, mas não foi confiável como pipeline principal de extração estrutural.

## Por que foi substituída

Problemas observados:

- criava julgados inexistentes;
- confundia precedentes citados com julgados principais;
- duplicava itens;
- gerava entradas quebradas ou parciais;
- podia cortar julgados entre chunks;
- dependia demais da LLM para entender a estrutura editorial;
- exigia Ollama/modelo local e aumentava custo operacional.

## Observação sobre os JSONs

Os arquivos `Informativo1214.json`, `Informativo1215.json`, `Informativo1216.json` e `Informativo1217.json` são resultados históricos desta versão.

Eles não devem ser usados como referência final do projeto.

A saída de referência atual deve ser gerada pelo pipeline principal em `../../src/`.
