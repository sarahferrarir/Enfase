# Contrato e uso das referências

## Fontes do contrato

Leia `../conversor/src/schemas.py` para os modelos e valores padrão. `schema.json` foi gerado desses modelos com Pydantic e documenta o formato atual; não é um novo schema da aplicação.

A raiz é um objeto com `julgado_stf`, uma lista de registros `JulgadoSTF`. Não substitua a raiz por uma lista simples.

Os campos textuais aceitam texto ou `null`. `comments` e `metadata` são objetos; `is_extraordinary` é booleano; `modified_by_users` aceita lista de textos ou `null`. Os campos de conteúdo podem conter HTML. Confira a relação completa de campos no schema.

O modelo permite omissões, coerção de números para texto e campos extras que podem ser descartados. Por isso, além da validação pelo modelo, confira as chaves e os tipos do JSON bruto contra o schema e preserve todos os campos emitidos pelo conversor. Uma validação estrutural bem-sucedida não comprova fidelidade documental.

Não invente valores para preencher campos nulos. Preserve defaults operacionais, incluindo `status`, sem interpretá-los como resultado da auditoria. Não copie IDs ou outros valores de registros de exemplo.

## Notícia única e completa

Por decisão do usuário, cada julgado possui um único campo `noticia` textual. Não use uma lista de notícias nem campos novos de citação por resumo. Separe os campos sem duplicar o bloco de `resumo` em `noticia`:

- **Caso comum:** o primeiro enunciado fica em `resumo`; o restante fica em `noticia`, incluindo eventuais enunciados seguintes em negrito, explicações, notas e rodapés. Não acrescente o primeiro enunciado ao início da notícia. Exemplo: no ARE 1.477.280, o primeiro enunciado fica em `resumo` e o segundo continua em negrito em `noticia`, na posição original.
- **Caso específico “Resumo (artigo por artigo):”:** `resumo` é exatamente `<p><strong>Resumo (artigo por artigo):</strong></p>`. Todos os blocos abaixo do marcador ficam em `noticia`, na ordem original, com títulos, todos os enunciados em negrito conforme o DOCX, explicações, notas e rodapés. Não repita o marcador na notícia. No caso ADI 7.156/7.236, o primeiro enunciado é parte de `noticia`, assim como os demais, e não é o valor de `resumo`.

Confira a cobertura e a ausência de duplicação entre esses dois campos usando os blocos da fonte. Não elimine trechos distintos apenas por semelhança textual. Corrija o JSON sem alterar o conversor.

`noticia_completa` e `html` já existem no contrato e podem incluir elementos editoriais adicionais; revise esses campos segundo o conversor e a fonte. Não renomeie campos nem elimine `resumo`.

## Exemplo do informativo 1225

`Informativo1225_exemplo_nao_validado.json` é uma cópia integral do exemplo existente no projeto. Contém dois registros e serve para observar nomes, tipos e HTML; não é uma resposta correta certificada e pode reproduzir as limitações do conversor.

Não use esse exemplo como gabarito, nem substitua os documentos originais por ele. Para testar o caso 1225, o usuário deve fornecer os documentos desse informativo na conversa. Para outros informativos, não reutilize seu conteúdo.

As referências de conferência e as correções ficam no relatório separado. Não as acrescente arbitrariamente a `metadata` ou `comments`.
