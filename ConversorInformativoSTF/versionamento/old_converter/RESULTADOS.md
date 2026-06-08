# Resultados da Versão Old Converter

Este arquivo resume os resultados observados na versão inicial baseada em conversão DOCX/markdown e extração por regras.

## Resultado mais relevante

No teste documentado com `Informativo1214.docx`, a versão antiga gerou aproximadamente:

- `4` julgados válidos;
- JSON com campos estruturais básicos;
- preenchimento parcial de campos adicionais;
- descarte de blocos considerados incompletos.

Uma análise comparativa antiga indicava que o JSON de referência usado na época tinha cerca de `30` julgados, enquanto a saída gerada possuía apenas `4`.

## Problemas observados

- Muitos itens não eram separados como julgados.
- O parser dependia demais de cabeçalhos e marcadores textuais específicos.
- Campos como `resumo`, `noticia`, `noticia_completa`, `legislacao` e `ods_onu2030` tinham formatação ou cobertura incompleta.
- O ajuste de uma regex frequentemente resolvia um caso e quebrava outro.
- A documentação antiga misturava análise, código colado, relatório de mudança e instruções operacionais.

## Comparação com o esperado

Esta versão serviu como prova de conceito, mas não era robusta o suficiente para novos informativos.

Ela foi útil para:

- identificar campos necessários;
- testar o formato JSON;
- mapear limitações da extração por regex.

Ela não deve ser usada como referência final de saída. A referência atual do projeto está no pipeline principal em `../../src/`.
