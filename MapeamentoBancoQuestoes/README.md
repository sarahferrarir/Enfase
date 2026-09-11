# Banco de Questões

Análise da base de questões do Ênfase, com inventário, fontes oficiais de concursos e rastreabilidade dos agrupamentos.

## Estrutura

- `scripts/`: extração e inspeção de XLSX e análise de metadados.
- `scripts/legacy/`: gerador histórico `build_deliverables.py`.
- `data/analysis/`: dados intermediários `metadata.jsonl`, `lista.jsonl` e `summary.json`.
- Entregáveis nesta pasta: `inventario-banco-questoes.{json,md}`, `fontes-oficiais-concursos.{json,md}` e `rastreabilidade-agrupamentos-questoes.json`.

Os dados intermediários são preservados porque os entregáveis finais atuais não são totalmente regeneráveis pelo script legado. A planilha XLSX de origem não está incluída no repositório.

## Caminhos e execução

Os caminhos abaixo são relativos a esta pasta:

- `python3 scripts/extract_xlsx.py <planilha.xlsx>` imprime uma inspeção da planilha.
- `python3 scripts/extract_metadata.py <planilha.xlsx> [diretorio_de_saida]` grava `metadata.jsonl` e `lista.jsonl`. Sem destino explícito, usa `data/analysis/`, localizado a partir do script.
- `python3 scripts/analyze_metadata.py` lê `data/analysis/metadata.jsonl` e sobrescreve `data/analysis/summary.json`, independentemente do diretório de execução.
- `node scripts/inspect_workbook.mjs <planilha.xlsx>` imprime a inspeção e grava o marcador `data/analysis/workbook-inspected.ok`, localizado a partir do script.

Argumentos de entrada e destinos explícitos relativos continuam relativos ao diretório de execução. Os scripts Python desta análise usam somente a biblioteca padrão.

O script Node depende de `@oai/artifact-tool`, atualmente resolvido pelo link `node_modules` na raiz do repositório para um runtime externo. Não há `package.json` próprio neste projeto; a execução depende desse ambiente local.

O gerador legado lê os metadados da nova localização, mas preserva a lógica histórica e grava seus quatro arquivos no diretório de execução. Não o execute na pasta dos entregáveis atuais; qualquer uso futuro deve ocorrer em um diretório de saída separado.
