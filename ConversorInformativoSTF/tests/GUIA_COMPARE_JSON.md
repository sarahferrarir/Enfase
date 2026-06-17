# Comparação de Acurácia

O `compare_json.py` valida a acurácia do ConversorInformativoSTF comparando o JSON gerado pelo conversor com um JSON esperado de referência.

Use esta ferramenta quando quiser conferir se a extração do DOCX produziu os mesmos julgados e campos relevantes esperados para um informativo.

## Fluxo de Uso

O teste compara:

- JSON gerado pelo conversor;
- JSON de referência.

O JSON de referência pode conter vários informativos no mesmo arquivo. A comparação filtra apenas os itens cujo campo `informativo` corresponde ao número informado na CLI.

## Exemplo Básico

```bash
python -m tests.compare_json \
  --generated exemplos/Informativo1214.json \
  --expected exemplos/julgado-stf.json \
  --informativo 1214
```

Parâmetros:

- `--generated`: caminho do JSON gerado pelo conversor.
- `--expected`: caminho do JSON esperado/referência.
- `--informativo`: número do informativo a comparar.

## Resultado no Terminal

O relatório mostra:

- `Itens esperados`: quantidade de itens no JSON de referência após filtro por informativo.
- `Itens gerados`: quantidade de itens no JSON gerado após filtro por informativo.
- `Itens casados`: itens encontrados nos dois arquivos pelo identificador principal.
- `Itens faltando`: itens esperados que não foram encontrados no JSON gerado.
- `Itens extras`: itens gerados que não existem no JSON esperado.
- `Diferenças por campo`: divergências encontradas nos campos comparados.
- `PASSOU` / `FALHOU`: resumo final da comparação.

## Campos Ignorados

O objetivo é validar a extração do DOCX. Por isso, campos gerados posteriormente por IA ou por etapas de workflow não entram na comparação.

Exemplos de campos ignorados por padrão:

- `questao`
- `comentario`
- `classificacao`
- `conteudo_fixacao`

## Ignore Fields

Use `--ignore-fields` para remover campos adicionais da comparação.

Exemplo ignorando `legislacao`:

```bash
python -m tests.compare_json \
  --generated exemplos/Informativo1214.json \
  --expected exemplos/julgado-stf.json \
  --informativo 1214 \
  --ignore-fields legislacao
```

Exemplo ignorando mais de um campo:

```bash
python -m tests.compare_json \
  --generated exemplos/Informativo1211.json \
  --expected exemplos/sample.json \
  --informativo 1211 \
  --ignore-fields legislacao,situacao_julgamento
```

Isso é útil quando:

- existe divergência conhecida;
- o campo ainda está em desenvolvimento;
- a regra de negócio ainda não foi definida.

Caso especial: `legislacao`.

Atualmente existem JSONs de referência que armazenam URLs de legislação, enquanto o conversor extrai referências textuais. Pode ser útil ignorar esse campo durante a comparação.

## Relatório JSON

Toda execução salva automaticamente um relatório JSON com o resultado completo da comparação.

Por padrão, o arquivo é salvo em:

```text
reports/compare_<informativo>.json
```


Exemplo: ao comparar o informativo `1214`, o caminho padrão será `reports/compare_1214.json`.

A pasta `reports/` guarda os resultados dos testes de acurácia e é criada automaticamente quando necessário.

Use `--report-json` apenas se quiser escolher outro caminho.

```bash
python -m tests.compare_json \
  --generated exemplos/Informativo1214.json \
  --expected exemplos/julgado-stf.json \
  --informativo 1214 \
  --ignore-fields legislacao \
  --report-json reports/meu_teste.json
```

Quando `--report-json` é informado, o relatório é salvo nesse caminho customizado em vez do caminho padrão. As pastas necessárias também são criadas automaticamente.

A estrutura geral inclui:

- timestamp do teste;
- caminhos dos arquivos comparados;
- contagens de itens esperados, gerados, casados, faltando e extras;
- total de diferenças por campo;
- campos ignorados;
- listas de itens faltando, extras e diferenças detalhadas;
- status `passed`.

## Interpretação dos Resultados

`PASSOU` significa:

- nenhum item faltando;
- nenhum item extra;
- nenhuma diferença por campo.

`FALHOU` significa que existe ao menos uma divergência.

## Limitações

- A comparação é strict depois da normalização.
- Diferenças textuais reais serão reportadas.
- A ordem dos itens no array não importa.
- O matching é feito por `classe_processo + numero_processo + uf`.
