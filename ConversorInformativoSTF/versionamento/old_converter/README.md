# Old Converter

Esta pasta preserva a primeira versão funcional do `ConversorInformativoSTF`.

Ela é histórica. A versão atual correta está em `../../src/`.

## O que era

Pipeline inicial para converter Informativos STF em DOCX para JSON usando uma abordagem majoritariamente determinística:

1. converter o DOCX para markdown/texto;
2. limpar o texto;
3. separar blocos de julgados;
4. extrair campos por regras e regex;
5. validar campos mínimos;
6. gerar JSON.

O arquivo `llm_processor.py` tem nome herdado, mas nesta versão a extração era feita por regex e parsing em Python, não por chamada real a LLM.

## Principais arquivos

- `converter.py`: orquestra o pipeline antigo.
- `document_converter.py`: converte DOCX para markdown.
- `text_cleaner.py`: aplica limpeza textual básica.
- `text_splitter.py`: tenta separar blocos de julgados e extrair metadados.
- `llm_processor.py`: extrai campos por regras/regex.
- `models.py`: modelos Pydantic antigos.

## Limitações principais

- Separação de julgados dependia fortemente de linhas como `DIREITO ...`.
- Blocos sem `Resumo:` literal podiam ser descartados.
- Regex de processo, título, ODS e legislação era frágil diante de variações editoriais.
- Processos citados, precedentes e rodapés podiam afetar a extração.
- O formato textual/HTML era limitado.
- A manutenção ficava difícil porque pequenas variações exigiam novas regex.

## Por que foi substituída

Esta versão ajudou a mapear o problema e definir os campos esperados, mas foi substituída por baixa robustez e dificuldade de manutenção.

A versão atual usa leitura XML do DOCX, preserva runs/links, isola a seção Plenário, separa itens editoriais de forma mais estável e gera HTML para campos textuais.

Veja:

- `../../README.md`
- `../../RESUMO_IMPLEMENTACAO.md`
