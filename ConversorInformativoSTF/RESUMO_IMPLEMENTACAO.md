# Resumo de Implementacao

Este arquivo registra a evolucao do `ConversorInformativoSTF` e as principais decisoes tecnicas. Instrucoes de execucao ficam no `README.md` e no `GUIA_TESTE.md`.

## Evolucao das Versoes

### Versao regex inicial

A primeira versao separava julgados e extraia campos principalmente por regex. Ela foi preservada em `versionamento/old_converter/`.

Problemas observados:

- separacao incorreta de julgados;
- alta dependencia da estrutura textual exata;
- dificuldade para lidar com variacoes entre informativos;
- falsos positivos com processos citados em precedentes.

### Experimento LLM/Ollama

Foi criada uma arquitetura experimental com LLM, prompts e chunking. Essa abordagem ficou preservada em `versionamento/llm_chunk_pipeline/`.

Motivo para nao seguir como fluxo principal:

- duplicacao de julgados;
- processos citados como precedentes eram confundidos com julgados principais;
- chunking por tamanho podia fragmentar itens editoriais;
- maior custo operacional e menor previsibilidade.

### Versao deterministica atual

A versao ativa voltou a ser deterministica, mas com uma arquitetura mais clara e com leitura mais rica do DOCX.

Decisoes principais:

- ler o DOCX diretamente via XML;
- preservar paragrafos, runs, estilos simples e hyperlinks;
- isolar a secao `1 Plenario` antes da extracao;
- separar itens editoriais por marcadores juridicos e estrutura do informativo;
- extrair campos estruturados por regras pequenas e localizadas;
- gerar HTML dos campos textuais a partir do conteudo real do DOCX;
- manter versoes antigas apenas como historico em `versionamento/`.

## Arquitetura Atual

```text
DOCX
  -> document_reader.py
  -> metadata_extractor.py
  -> section_extractor.py
  -> editorial_item_splitter.py
  -> field_extractor.py
  -> html_formatter.py
  -> converter.py
  -> JSON final
```

Responsabilidades:

- `document_reader.py`: le `word/document.xml` e `word/_rels/document.xml.rels`, gerando paragrafos com runs e links.
- `metadata_extractor.py`: identifica numero, ano e data do informativo.
- `section_extractor.py`: limita o processamento ao Plenario.
- `editorial_item_splitter.py`: separa itens editoriais reais.
- `field_extractor.py`: extrai processo, titulo, ramo, materia, resumo, noticia, ODS, legislacao, relator, julgamento e tema RG.
- `html_formatter.py`: converte paragrafos e runs para HTML seguro.
- `schemas.py`: define os modelos Pydantic de entrada intermediaria e saida.
- `validator.py`: emite avisos simples de validacao.

## Campos Atualmente Cobertos

Campos estruturais principais:

- `informativo`
- `data_informativo`
- `classe_processo`
- `numero_processo`
- `uf`
- `titulo`
- `ramo_direito`
- `materia`
- `ods_onu2030`
- `legislacao`
- `tema_rg`
- `repercussao_geral`
- `relator`
- `redator_acordao`
- `data_julgamento`
- `situacao_julgamento`

Campos textuais:

- `resumo`
- `noticia`
- `noticia_completa`
- `html`
- `tese_julgado`

O HTML preserva, quando o DOCX fornece esses dados:

- paragrafos;
- negrito;
- italico;
- sublinhado;
- links;
- listas;
- linhas finais de processo como lista.

## Limitações Atuais

- A extracao ainda depende de padroes editoriais dos Informativos STF.
- O parser de legislacao cobre padroes comuns, nao todos os possiveis.
- Links so sao preservados quando existem como hyperlinks reais no DOCX.
- Estilos visuais complexos do Word nao sao reproduzidos.
- Turmas, inovacoes normativas e outras secoes nao sao objetivo do pipeline atual.
- O schema tem campos futuros ainda nao preenchidos automaticamente.

## Proximos Passos Possiveis

Melhorias deterministicas:

- ampliar testes de regressao com mais informativos;
- adicionar snapshots controlados dos campos principais;
- melhorar cobertura de legislacao e referencias normativas;
- revisar a documentacao quando novos informativos forem adicionados.

Uso futuro de IA em campos especificos, sem voltar ao chunking como fluxo principal:

- gerar `questao`;
- gerar `comentario`;
- sugerir `classificacao`;
- sugerir `conteudo_fixacao`;
- apoiar revisao humana de campos complexos.

A decisao recomendada e manter a extracao estrutural deterministica e usar IA apenas como etapa complementar, isolada e opcional, para campos interpretativos.
