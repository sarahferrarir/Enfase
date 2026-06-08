# Resultados da Versão LLM Chunk Pipeline

Este arquivo resume os resultados históricos da versão baseada em chunking + LLM/Ollama.

## Resultados salvos

JSONs históricos preservados nesta pasta:

- `Informativo1214.json`: 25 registros no arquivo salvo.
- `Informativo1215.json`: 7 registros no arquivo salvo.
- `Informativo1216.json`: 0 registros no arquivo salvo.
- `Informativo1217.json`: 10 registros no arquivo salvo.

Esses números representam a saída do experimento, não a qualidade final esperada.

## Problemas observados

Apesar de alguns ganhos aparentes de quantidade em certos arquivos, a qualidade estrutural não era confiável.

Falhas recorrentes:

- registros duplicados do mesmo caso;
- processos citados em precedentes viravam julgados independentes;
- julgados principais eram fragmentados em entradas parciais;
- algumas entradas tinham título/matéria, mas não tinham processo ou resumo;
- outras tinham processo/data/relator, mas não tinham conteúdo do julgado;
- o chunking podia cortar o contexto necessário para a LLM;
- a validação precisava corrigir muitos erros gerados pela própria extração.

## Exemplo de falha relevante

No `Informativo1214`, processos citados dentro de outro julgado podiam ser extraídos como se fossem julgados principais.

Esse tipo de erro foi decisivo para abandonar a LLM como núcleo da extração estrutural.

## Comparação com a versão atual

A versão atual do projeto usa abordagem determinística:

- leitura XML do DOCX;
- preservação de parágrafos, runs e links;
- isolamento da seção Plenário;
- separação determinística de itens editoriais;
- extração estruturada por regras pequenas;
- geração de HTML para campos textuais.

A LLM pode voltar futuramente como etapa auxiliar para campos interpretativos, como `questao`, `comentario`, `classificacao` ou `conteudo_fixacao`, mas não como mecanismo principal de separação e extração dos julgados.
