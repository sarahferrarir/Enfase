# Inventário do banco de questões de prova — Curso Ênfase

| Item | Valor |
|---|---|
| Data da extração | 29 de julho de 2026 |
| Data da revisão de modelagem | 3 de agosto de 2026 |
| Arquivo de origem | `Base_Questo_es_Concurso_Completa_para_Adriano_13_07_26.xlsx` |
| Base estruturada equivalente | `inventario-banco-questoes.json` |
| Rastreabilidade questão a questão | `rastreabilidade-agrupamentos-questoes.json` |
| Mapa de fontes externas | `fontes-oficiais-concursos.md` / `.json` |

**Conjunto completo de entregáveis**

| Arquivo | Conteúdo | Público |
|---|---|---|
| `inventario-banco-questoes.md` | Este documento: relatório humano e catálogo descritivo | Gestão e time técnico |
| `inventario-banco-questoes.json` | Base estruturada: catálogos, agrupamentos, famílias, inconsistências, métricas | Consumo por sistema ou por outro agente |
| `fontes-oficiais-concursos.md` | Guia de monitoramento e metodologia de fontes | Quem for operar o acompanhamento |
| `fontes-oficiais-concursos.json` | Fontes oficiais vinculadas a entidades e certames | Consumo por sistema ou por outro agente |
| `rastreabilidade-agrupamentos-questoes.json` | Vínculo de cada uma das 51.190 questões ao seu agrupamento e à linha de origem | Auditoria e reconstrução da base |

---

## Resumo executivo

**Objetivo.** Estabelecer uma base confiável sobre o que o banco de questões de prova do Ênfase efetivamente cobre — quais órgãos, bancas, cargos, trilhas e anos estão representados — e mapear as fontes oficiais que precisam ser acompanhadas para identificar certames já realizados e futuros. O trabalho é de inventário e diagnóstico, não de correção da base.

**Origem dos dados.** Uma única planilha, `Base_Questo_es_Concurso_Completa_para_Adriano_13_07_26.xlsx`, com três abas: `Base_sem duplic` (tabela-fato, 51.190 questões × 44 colunas), `HC` (dimensão de temas) e `Lista` (tabela de domínio de todas as demais dimensões). Não houve acesso ao sistema de origem nem a dicionário de dados — o modelo foi reconstruído a partir da própria planilha.

### Números da cobertura

| Métrica | Valor | Observação |
|---|---|---|
| Questões | **51.190** | todas objetivas, todas do produto *Questões de Concursos* |
| Agrupamentos técnicos de prova | **485** | combinações de campos internos, não provas oficiais |
| Famílias de concurso (órgão + cargo) | **187** | séries históricas, não certames individuais |
| Concursos oficiais identificados | **0** | a base não tem edital, data nem URL |
| Órgãos | **182** referenciados | de 301 cadastrados |
| Bancas | **30** referenciadas | de 49 cadastradas |
| Cargos | **23** referenciados | de 76 cadastrados; 1 é chave órfã |
| Cursos / trilhas internas | **12** referenciados | de 22 cadastrados |
| Carreiras oficiais mapeadas | **0** | depende de validação humana |
| Intervalo de anos | **2004 a 2026** | 22 anos com questões; 2005 vazio |
| Fontes oficiais verificadas | **16** | DOU, CNJ, 6 bancas, ENFAM/ENAM, MPF, AGU |
| Inconsistências documentadas | **17** | 4 de severidade alta |

### Principais inconsistências

1. **Três chaves quebradas afetando 1.490 questões.** O campo de banca aponta para um registro de teste em 1.090 questões (INC-003); o campo de órgão aponta para um cadastro do tipo errado em 200 (INC-004); e 200 questões têm um ID de cargo que simplesmente não existe no cadastro (INC-002).
2. **O rótulo `BANCA PRÓPRIA` não tem significado documentado**, e cobre 9.510 questões em 87 agrupamentos (INC-007).
3. **Ausência total de campos de certame** — sem data de prova, número de edital ou URL (INC-009). É a limitação que impede vincular a base a qualquer fonte externa.
4. **Confusão de modelagem na versão anterior deste inventário** (INC-016), corrigida: agrupamentos de campos internos estavam sendo tratados como provas oficiais.
5. **23,2% das questões sem classificação temática** e 988 sem gabarito (INC-010, INC-011).

### Principais limitações do banco

- Não é possível afirmar, a partir da base, que um agrupamento corresponde a uma prova oficial específica.
- Não há como distinguir dois certames do mesmo órgão e cargo no mesmo ano.
- A dimensão de banca mistura organizadoras de mercado, siglas de órgãos e um rótulo genérico.
- Não há questões discursivas nem orais, embora o modelo preveja os dois tipos.
- O cadastro é maior que a cobertura: 119 órgãos, 19 bancas e 53 cargos nunca foram usados.

### Conclusão

O banco tem **massa e amplitude relevantes** — 51.190 questões objetivas, cobertura praticamente completa de TJs, MPs, DPEs e PGEs nas 27 unidades da federação, e uma série histórica de 22 anos que continua sendo alimentada (2026 já tem registros). O acervo é sólido como material de estudo.

O que ele **não** é, hoje, é uma base rastreável até certames oficiais. Faltam os três campos que fariam essa ponte — data da prova, número do edital e URL — e sem eles nenhum registro interno pode ser vinculado a um concurso específico, nem alimentado automaticamente por monitoramento externo. Somando isso às três chaves quebradas e ao rótulo `BANCA PRÓPRIA` não documentado, há **11.000 questões cuja procedência não é confirmável** sem intervenção humana.

A recomendação central é tratar a inclusão dos campos de edital como pré-requisito de qualquer automação. Enquanto ela não existir, o mapa de fontes oficiais entregue aqui serve para monitoramento manual assistido, mas não para casamento automático com o acervo.

---

## 1. Três conceitos que não devem ser confundidos

A base não contém identificador de prova nem de concurso. Tudo o que se pode construir a partir dela são **agrupamentos derivados dos campos internos**, que não equivalem a entidades oficiais. Esta distinção governa todo o restante do documento.

| Conceito | Como é obtido | Total | O que NÃO é |
|---|---|---|---|
| **Agrupamento técnico de prova** | Combinação distinta de `ID Órgão × ID Banca × ID Ano × ID Cargo × ID Curso` | **485** | Não comprova a existência de uma prova oficial individual, nem equivale necessariamente a um caderno, fase, edição ou aplicação oficial |
| **Família de concurso** | Combinação de Órgão + Cargo (série histórica) | **187** | Não é um concurso individual: uma família reúne vários concursos oficiais realizados em anos diferentes, cada um com edital próprio |
| **Concurso oficial** | Certame identificado por edital ou publicação em diário oficial | **0** | Permanece `null` em toda a base — nenhum registro interno tem número de edital, data de prova ou URL que permita a vinculação |

Um mesmo concurso oficial pode gerar mais de um agrupamento técnico — por exemplo, se as questões de um único certame estiverem distribuídas entre dois cursos internos. E um mesmo agrupamento pode, em tese, reunir questões de mais de uma aplicação, já que a base só registra o ano. Por isso o número 485 mede **combinações de campos internos**, não provas realizadas.

---

## 2. Panorama quantitativo

O banco contém **51.190 questões de prova**, consolidadas em **485 agrupamentos técnicos de prova** e **187 famílias de concurso (órgão + cargo)**, cobrindo **22 anos** (2004 e 2006 a 2026). Todas as questões são objetivas e todas pertencem ao produto *Questões de Concursos* — não há, nesta extração, questões inéditas, discursivas ou orais.

| Dimensão | Cadastrado | Referenciado na base | Cobertura |
|---|---|---|---|
| Órgãos | 301 | 182 | 60,5% |
| Bancas | 49 | 30 | 61,2% |
| Cargos | 76 | 23 (22 resolvíveis) | 30,3% |
| Cursos / trilhas internas | 22 | 12 | 54,5% |
| Anos | 25 | 22 | 88,0% |
| Carreiras normalizadas | — | 0 | pendente de validação |

Duas leituras importantes. Primeiro: **o cadastro é bem maior do que a cobertura real** — cerca de 40% dos órgãos cadastrados não têm nenhuma questão. Segundo: **nenhuma carreira oficial foi mapeada**, porque a base só tem a trilha comercial interna e mapear uma na outra por dedução produziria taxonomia inventada.

### 2.1 Volume por ano

| Ano | Questões | Agrupamentos técnicos |
|---|---|---|
| 2004 | 120 | 1 |
| 2006 | 550 | 5 |
| 2007 | 1460 | 12 |
| 2008 | 1650 | 17 |
| 2009 | 2190 | 20 |
| 2010 | 2150 | 20 |
| 2011 | 2560 | 27 |
| 2012 | 4098 | 41 |
| 2013 | 4088 | 38 |
| 2014 | 4685 | 45 |
| 2015 | 3738 | 36 |
| 2016 | 2845 | 24 |
| 2017 | 2940 | 29 |
| 2018 | 3188 | 31 |
| 2019 | 2060 | 17 |
| 2020 | 100 | 1 |
| 2021 | 3650 | 33 |
| 2022 | 3288 | 32 |
| 2023 | 1950 | 19 |
| 2024 | 1400 | 13 |
| 2025 | 2300 | 22 |
| 2026 | 180 | 2 |

A concentração está em 2012–2018 (mais de 24 mil questões). A queda em 2019–2020 acompanha a paralisação de certames no período; 2020 tem apenas 100 questões. **2026 já aparece com 180 questões**, o que indica que a base vem sendo alimentada de forma corrente.

### 2.2 Volume por curso / trilha interna do Ênfase

As siglas abaixo são **classificação comercial interna do Ênfase**, não carreiras oficiais. JDMP, por exemplo, agrega magistratura estadual e Ministério Público estadual — duas carreiras distintas sob um rótulo só.

| Curso / trilha interna | Questões | Agrupamentos | Intervalo de anos | Carreira oficial |
|---|---|---|---|---|
| JDMP | 19685 | 187 | 2006–2026 | não mapeada |
| DEFENSORIAS | 8830 | 78 | 2007–2025 | não mapeada |
| PGE | 6440 | 61 | 2006–2025 | não mapeada |
| DELEGADO | 4380 | 46 | 2004–2025 | não mapeada |
| JFMPF | 3620 | 35 | 2010–2025 | não mapeada |
| PGM | 2315 | 24 | 2007–2025 | não mapeada |
| JTMPT | 2300 | 23 | 2006–2024 | não mapeada |
| AGU | 1800 | 12 | 2007–2022 | não mapeada |
| ADVOGADO DE ESTATAIS | 740 | 9 | 2006–2015 | não mapeada |
| ANALISTA | 500 | 6 | 2007–2018 | não mapeada |
| ENAM | 480 | 3 | 2024–2026 | não mapeada |
| ADVOGADO DO SENADO | 100 | 1 | 2022–2022 | não mapeada |

### 2.3 Volume por banca (valor original registrado)

| Valor no campo Banca | Questões | Agrupamentos | Status |
|---|---|---|---|
| CESPE | 13185 | 108 | `resolvido_no_cadastro_interno` |
| BANCA PRÓPRIA | 9510 | 87 | `pendente_validacao` |
| FCC | 8890 | 90 | `resolvido_no_cadastro_interno` |
| FGV | 4440 | 43 | `resolvido_no_cadastro_interno` |
| CEBRASPE | 3920 | 34 | `resolvido_no_cadastro_interno` |
| VUNESP | 3845 | 40 | `resolvido_no_cadastro_interno` |
| FUNDEP | 1120 | 13 | `resolvido_no_cadastro_interno` |
| (TESTE) Cargo XY | 1090 | 13 | `invalido_registro_de_teste` |
| FUNDATEC | 730 | 7 | `resolvido_no_cadastro_interno` |
| FMP CONCURSOS | 600 | 6 | `resolvido_no_cadastro_interno` |
| CESGRANRIO | 530 | 7 | `resolvido_no_cadastro_interno` |
| ESAF | 400 | 4 | `resolvido_no_cadastro_interno` |
| PUCPR | 300 | 3 | `resolvido_no_cadastro_interno` |
| AOCP | 300 | 3 | `resolvido_no_cadastro_interno` |
| FUNCAB | 260 | 3 | `resolvido_no_cadastro_interno` |
| FUMARC | 220 | 3 | `resolvido_no_cadastro_interno` |
| UEPA | 210 | 3 | `resolvido_no_cadastro_interno` |
| FAPEC | 200 | 2 | `resolvido_no_cadastro_interno` |
| FAURGS | 200 | 2 | `resolvido_no_cadastro_interno` |
| UNIVERSA | 180 | 2 | `resolvido_no_cadastro_interno` |
| COPSUEL | 180 | 2 | `resolvido_no_cadastro_interno` |
| NCUFPR | 160 | 2 | `resolvido_no_cadastro_interno` |
| IESES | 100 | 1 | `resolvido_no_cadastro_interno` |
| FEPESE | 100 | 1 | `resolvido_no_cadastro_interno` |
| CSUFG | 100 | 1 | `resolvido_no_cadastro_interno` |
| INSTITUTO CIDADES | 100 | 1 | `resolvido_no_cadastro_interno` |
| UFMT | 100 | 1 | `resolvido_no_cadastro_interno` |
| CONSULPLAN | 80 | 1 | `resolvido_no_cadastro_interno` |
| IBGP | 80 | 1 | `resolvido_no_cadastro_interno` |
| FUNDAÇÃO CEPERJ | 60 | 1 | `resolvido_no_cadastro_interno` |

Três observações sobre esta tabela:

- **CESPE e CEBRASPE não foram somados.** São a mesma instituição em cadastros de períodos diferentes, mas os dois IDs permanecem separados. Existe apenas uma sugestão de agrupamento lógico (`NORM-001`) que não altera o dado de origem.
- **`BANCA PRÓPRIA` não recebeu interpretação.** É um rótulo genérico cujo significado não está documentado em nenhum lugar da base. Não se assume que esses certames tenham sido elaborados ou organizados pelo próprio órgão — todos os 87 agrupamentos com esse valor estão marcados como `pendente_validacao`, com o valor original preservado.
- **`(TESTE) Cargo XY`** é um registro de teste que aparece no campo de banca de 1.090 questões. Ver INC-003.

### 2.4 Volume por cargo

| Cargo | Questões | Agrupamentos |
|---|---|---|
| Promotor de Justiça | 10005 | 89 |
| Juiz de Direito | 9680 | 98 |
| Defensor Público | 8030 | 74 |
| Procurador do Estado | 6440 | 61 |
| Delegado de Polícia Civil | 3900 | 42 |
| Juiz Federal | 2900 | 29 |
| Procurador Municipal | 2315 | 24 |
| Juiz do Trabalho | 1700 | 17 |
| Defensor Público Federal | 800 | 4 |
| Advogado de Estatais | 740 | 9 |
| Procurador da República | 720 | 6 |
| Procurador Federal | 700 | 4 |
| Advogado da União | 700 | 4 |
| Procurador do Trabalho | 600 | 6 |
| ENAM | 480 | 3 |
| Delegado de Polícia Federal | 480 | 4 |
| Procurador da Fazenda Nacional | 400 | 4 |
| (não identificado — ID interno 620) | 200 | 2 |
| Advogado do Senado | 100 | 1 |
| Investigador de Polícia | 100 | 1 |
| Analista Judiciário - Área Judiciária | 80 | 1 |
| Escrevente Técnico Judiciário | 60 | 1 |
| Técnico Judiciário | 60 | 1 |

### 2.5 Qualidade do conteúdo das questões

| Campo | Preenchido | Ausente / observação |
|---|---|---|
| Tipo de questão | 51.190 objetivas | 0 discursivas, 0 orais |
| Gabarito | 49.588 | 988 ausentes + 614 marcadas ANULADA |
| Enunciado | 51.177 | 13 ausentes |
| Comentário / resposta discursiva | 4.152 | 47.038 ausentes |
| Tema | 39.309 | 11.881 ausentes (23,2%) |
| Bloco | 15.383 | 35.807 ausentes |
| Edição | 2.280 | 48.910 ausentes |
| Classificação predominante | 9.453 | 41.737 ausentes |
| Simulado | 0 | 51.190 ausentes — coluna 100% vazia |
| Produto | 51.190 em *Questões de Concursos* | 0 em *Questões Inéditas* |

---

## 3. Metodologia

1. Leitura direta das três abas do arquivo com `openpyxl`/`pandas`, sem passar pelas colunas calculadas.
2. As colunas `NM ...`, `Tema`, `Disciplina`, `IDs Lista`, `Nome Resumido` e `Tema Pai II` **não foram usadas como fonte**: são fórmulas `PROCV`/`CONCAT` da própria planilha. Todas as junções foram refeitas a partir das chaves numéricas contra a aba `Lista`.
3. O grão do inventário é o **agrupamento técnico de prova**, definido na seção 1. A escolha de grão é uma construção desta análise, e não uma entidade que exista no sistema de origem.
4. Acima dele existe a **família de concurso** (órgão + cargo), uma série histórica.
5. O **concurso oficial** só seria preenchido mediante evidência externa individual — edital ou publicação em diário oficial que identifique unicamente o certame.
6. O campo `Curso` foi tratado como **trilha interna do Ênfase** (`curso_enfase_*`), com os campos de carreira normalizada existindo mas vazios.
7. O campo de banca preserva sempre o valor original em `banca_nome_original`.
8. Toda chave que não resolveu contra a aba `Lista`, ou que resolveu para um registro de tipo incompatível, foi mantida como `null` e documentada.
9. As fontes externas foram verificadas em 31/07/2026, com verificação adicional em 03/08/2026, e estão em `fontes-oficiais-concursos.md` / `.json`.

---

## 4. Limitações metodológicas

Esta seção existe para que ninguém use os números deste inventário com mais confiança do que eles suportam. Cinco decisões foram tomadas de forma deliberada, e todas restringem o que se pode concluir a partir do material.

### 4.1 Agrupamentos técnicos não são provas oficiais

Os 485 agrupamentos são combinações distintas de cinco campos internos. Não existe, na base, nada que comprove que cada combinação corresponde a uma prova aplicada. Um certame pode estar dividido em dois agrupamentos (se suas questões foram atribuídas a cursos internos diferentes), e um agrupamento pode conter mais de uma aplicação do mesmo ano. Contagens por agrupamento medem organização interna do acervo, não atividade do mercado de concursos.

### 4.2 Famílias não são concursos individuais

As 187 famílias agrupam órgão + cargo ao longo de todo o histórico. Uma linha como "TJ/SP — Juiz de Direito" abrange todos os certames desse cargo naquele tribunal, de anos distintos e com editais distintos. É uma série histórica, útil para medir cobertura longitudinal, e não uma contagem de certames.

### 4.3 `concurso_oficial_id` é null por decisão, não por falha

Nenhum registro interno traz número de edital, data de prova ou URL. Preencher o identificador de concurso oficial exigiria adivinhar qual certame originou cada bloco de questões — e uma adivinhação parece um dado. Os 485 agrupamentos carregam `status_validacao_concurso: "nao_validado_externamente"` justamente para tornar essa lacuna explícita e auditável. **O processamento funcionou; a informação não existe na origem.**

### 4.4 Cursos internos não foram convertidos em carreiras

JDMP, JFMPF, JTMPT, PGE, PGM, DEFENSORIAS, DELEGADO, AGU, ENAM, ANALISTA, ADVOGADO DE ESTATAIS e ADVOGADO DO SENADO são trilhas comerciais do Ênfase. Algumas agregam mais de uma carreira oficial; outras nomeiam um exame e não uma carreira. Converter automaticamente produziria uma taxonomia que não corresponde nem ao Ênfase nem ao serviço público. Os campos `carreira_normalizada_id` e `carreira_normalizada_nome` existem, estão `null`, e aguardam mapeamento validado com regra e evidência registradas.

### 4.5 Nada foi inferido sem evidência documental

Onde a informação não existe ou não pôde ser confirmada, o valor é `null` e a lacuna está explicada em `observacoes`. Nenhuma entidade foi fundida: CESPE e CEBRASPE, o ID duplicado 793 e os dois cadastros de TJ/PR permanecem separados, com sugestões de normalização registradas à parte e todas marcadas como não aplicadas. Nas fontes externas, agregadores e portais de notícia foram usados apenas como pista de busca e nunca registrados como fonte.

---

## 5. Estrutura do arquivo e dicionário de entidades

| Aba | Linhas | Colunas | Papel |
|---|---|---|---|
| `Base_sem duplic` | 51.190 | 44 | Tabela-fato: uma linha por questão |
| `HC` | 8.715 | 6 | Dimensão de conteúdo: tema → tema raiz → disciplina |
| `Lista` | 509 | 4 | Tabela de domínio única e polimórfica para todas as demais dimensões |

O ponto estrutural mais relevante é a aba `Lista`: ela é **uma única tabela de domínio para dez dimensões diferentes**, discriminadas pela coluna `Tipo` (Orgão, Banca, Cargo, Ano, Curso, Edição, Bloco, Classificação Predominante, Simulado, Produto). Órgãos, bancas e cargos compartilham a mesma sequência de IDs. Como não há restrição de tipo na ligação, nada impede que a coluna `ID Banca` aponte para um cargo — e é exatamente isso que acontece em 1.090 questões.

### 5.1 Dicionário de entidades

- **questao** — Unidade atômica. Identificada por 'Id da Questao' (único, sem duplicidade nas 51.190 linhas). Carrega enunciado, alternativas, gabarito e classificações.
- **orgao** — Instituição para a qual o certame foi realizado (TJ/SP, MP/SC, AGU...). Na aba Lista, Tipo='Orgão'. 301 cadastrados, 182 com questões.
- **banca** — Valor registrado no campo de banca. Na Lista, Tipo='Banca'. 49 cadastradas, 30 referenciadas. Inclui bancas de mercado, o rótulo genérico 'BANCA PRÓPRIA' e siglas de órgãos. O valor original é sempre preservado em banca_nome_original.
- **cargo** — Cargo disputado no certame (Juiz de Direito, Promotor de Justiça...). Tipo='Cargo'. 76 cadastrados, 23 referenciados (22 resolvíveis).
- **ano** — Ano registrado para a prova. Tipo='Ano'. 25 cadastrados (2002–2026), 22 referenciados. É a única informação temporal existente — não há data de prova.
- **curso_enfase** — Trilha comercial interna do Ênfase (JDMP, PGE, DEFENSORIAS, DELEGADO...). Tipo='Curso'. 22 cadastrados, 12 com questões. Tratado exclusivamente como classificação interna, nunca como carreira oficial.
- **bloco** — Subdivisão registrada para a prova (I a VI, Único). Presente em 15.383 questões.
- **edicao** — Qualificador adicional da aplicação (1ª/2ª Edição, mês, cidade, turno). Presente em 2.280 questões.
- **classificacao_predominante** — Natureza do conteúdo cobrado (Legislação, Jurisprudência, Teoria e combinações). Presente em 9.453 questões.
- **produto** — Origem do item: 'Questões de Concursos' (792) ou 'Questões Inéditas' (791). Toda a extração é 792.
- **tema** — Assunto da questão, na aba HC, com hierarquia tema → tema raiz → disciplina. Ausente em 11.881 questões.
- **relacionamento** — Base_sem duplic é a tabela-fato; Lista é uma tabela de domínio única e polimórfica (uma linha por valor de qualquer dimensão, discriminada pela coluna Tipo); HC é a dimensão de conteúdo. A ligação é feita por PROCV, sem integridade referencial garantida — daí as inconsistências INC-002 a INC-004.

---

## 6. Catálogo de entidades

Os catálogos completos, com ID interno e situação (Ativo/Inativo), estão no JSON em `catalogos`. Resumo dos valores efetivamente referenciados:

### 6.1 Valores no campo Banca

(TESTE) Cargo XY, AOCP, BANCA PRÓPRIA, CEBRASPE, CESGRANRIO, CESPE, CONSULPLAN, COPSUEL, CSUFG, ESAF, FAPEC, FAURGS, FCC, FEPESE, FGV, FMP CONCURSOS, FUMARC, FUNCAB, FUNDATEC, FUNDAÇÃO CEPERJ, FUNDEP, IBGP, IESES, INSTITUTO CIDADES, NCUFPR, PUCPR, UEPA, UFMT, UNIVERSA, VUNESP.

### 6.2 Cursos / trilhas internas do Ênfase

ADVOGADO DE ESTATAIS, ADVOGADO DO SENADO, AGU, ANALISTA, DEFENSORIAS, DELEGADO, ENAM, JDMP, JFMPF, JTMPT, PGE, PGM.

### 6.3 Cargos

Advogado da União, Advogado de Estatais, Advogado do Senado, Analista Judiciário - Área Judiciária, Defensor Público, Defensor Público Federal, Delegado de Polícia Civil, Delegado de Polícia Federal, ENAM, Escrevente Técnico Judiciário, Investigador de Polícia, Juiz Federal, Juiz de Direito, Juiz do Trabalho, Procurador Federal, Procurador Municipal, Procurador da Fazenda Nacional, Procurador da República, Procurador do Estado, Procurador do Trabalho, Promotor de Justiça, Técnico Judiciário, além de 200 questões cujo ID de cargo (620) não existe no cadastro.

### 6.4 Órgãos referenciados (182)

MP/SC (1800), AGU (1500), MP/SP (900), MP/MG (800), DPU (800), TJ/SC (800), TJ/SP (800), MPF (720), TRF3 (700), TJ/PR (680), MPT (600), DPE/RS (600), TRF2 (600), TJ/GO (560), MP/PR (525), DPE/AM (500), MP/GO (500), TJ/MS (500), TJ/MT (500), TRF1 (500), PG/DF (500), TJ/PE (500), TRF4 (500), TRF5 (500), ENAM (480), PF (480), TJ/RJ (480), TJ/MG (460), PGE/PA (460), DPE/ES (450), DPE/SP (440), PGE/RS (420), TJ/DF (400), TJ/CE (400), TJ/RS (400), PGE/GO (400), MP/RS (400), DPE/PR (400), DPE/CE (400), DPE/DF (400), MP/BA (400), TJ/PA (400), DPE/MS (400), MP/DFT (400), PGE/SP (380), DPE/PE (350), PGE/ES (350), PGE/AM (350), DPE/BA (350), MP/RO (300), DPE/MA (300), DPE/MT (300), DPE/AL (300), PC/ES (300), PGE/MT (300), PGE/PI (300), PGFN (300), PGE/AC (300), TJ/BA (300), PC/GO (300), PC/BA (300), TRT1 (300), TJ/AP (300), TJ/MA (300), TJ/AL (300), MP/MS (300), MP/PE (300), MP/MT (300), MP/RR (300), DPE/RO (300), DPE/SC (300), MP/AM (300), MP/CE (300), MP/ES (300), PGE/PR (280), MP/RJ (280), CEF (270), DPE/MG (260), PETROBRAS (260), PC/RS (240), BNDES (210), PC/MG (210), DPE/GO (200), DPE/AP (200), DPE/AC (200), TST (200), TJ/TO (200), TJ/SE (200), TJ/AC (200), TJ/AM (200), TJ/ES (200), MP/AP (200), MP/PI (200), DPE/TO (200), MP/AC (200), DPE/SE (200), DPE/RR (200), DPE/PB (200), DPE/PA (200), MP/PA (200), MP/PB (200), PGE/SE (200), PGE/PE (200), PGE/CE (200), PGE/PB (200), PGE/BA (200), PGE/RO (200), PGE/SC (200), PGE/RN (200), PGM Campinas/SP (200), PGE/AL (200), PGE/MS (200), MP/SE (200), PC/MA (200), PC/MS (200), MP/TO (200), PC/SP (200), TJ/PI (200), TJ/PB (200), PGM Fortaleza/CE (200), TRT2 (200), TRT3 (200), TJ/RO (200), PGE/TO (200), DPE/RJ (180), PC/DF (180), PC/TO (180), PC/PI (180), PC/PR (160), PC/RJ (160), PC/SE (150), PGM Manaus/AM (150), PGM São Paulo/SP (140), PC/AP (140), PC/SC (120), PC/AL (120), PGM Vitória/ES (120), PGM Boa Vista/RR (120), AGE/MG (100), DPE/RN (100), DPE/PI (100), MP/MA (100), MP/AL (100), PC/CE (100), PC/PA (100), PC/RN (100), PC/AC (100), PGM Cuiabá/MT (100), PGM Caruaru/PE (100), TRT18 (100), TRT15 (100), TRT4 (100), TRT23 (100), PGE/AP (100), PC/PE (100), TCE/PA (100), SF (100), PGM Salvador/BA (100), PGM Niterói/RJ (100), PGM São Luís/MA (100), PGM Curitiba/PR (100), PGM Natal/RN (100), PGM Maceió/AL (100), PGM João Pessoa/PB (100), TCE/RS (100), TRT8 (100), TRT6 (100), TRT9 (100), TRF6 (100), TRT5 (100), TJ/RN (100), TJ/RR (100), PGM Sorocaba/SP (95), PGM Porto Alegre/RS (90), PGM Belo Horizonte/MG (85), PC/PB (80), PC/RO (80), PGM Goiânia/GO (70), PGM Palmas/TO (60), PGM Blumenau/SC (50), PGM Palhoça/SC (35).

*(valor entre parênteses = questões na base)*

---

## 7. Famílias de concurso, agrupamentos e anos

A tabela completa está no JSON (`familias_concurso` e `agrupamentos_tecnicos`). Abaixo, as 30 famílias com maior volume. Cada linha é uma **série histórica órgão + cargo**, que pode reunir vários concursos oficiais distintos.

| Família (órgão + cargo) | Curso interno | Anos com agrupamento | Agrupamentos | Questões | Valores de banca | Concurso oficial |
|---|---|---|---|---|---|---|
| MP/SC — Promotor de Justiça | JDMP | 2014, 2016, 2019, 2021, 2023 | 5 | 1800 | BANCA PRÓPRIA, CEBRASPE | não validado |
| MP/SP — Promotor de Justiça | JDMP | 2011, 2012, 2013, 2015, 2017, 2019, 2022, 2023, 2024 | 9 | 900 | BANCA PRÓPRIA, VUNESP | não validado |
| DPU — Defensor Público Federal | DEFENSORIAS | 2007, 2010, 2015, 2017 | 4 | 800 | CESPE | não validado |
| MP/MG — Promotor de Justiça | JDMP | 2012, 2013, 2014, 2017, 2018, 2019, 2021, 2022, 2023, 2024 | 10 | 800 | CONSULPLAN, FUNDEP, IBGP | não validado |
| TJ/SC — Juiz de Direito | JDMP | 2013, 2015, 2017, 2019, 2022, 2023, 2024, 2025 | 8 | 800 | BANCA PRÓPRIA, FCC, CEBRASPE, FGV | não validado |
| TJ/SP — Juiz de Direito | JDMP | 2014, 2015, 2017, 2018, 2021, 2023, 2024, 2025 | 8 | 800 | VUNESP | não validado |
| MPF — Procurador da República | JFMPF | 2012, 2013, 2015, 2016, 2022, 2025 | 6 | 720 | BANCA PRÓPRIA | não validado |
| AGU — Procurador Federal | AGU | 2007, 2010, 2013, 2022 | 4 | 700 | CESPE, CEBRASPE | não validado |
| AGU — Advogado da União | AGU | 2009, 2012, 2015, 2022 | 4 | 700 | CESPE | não validado |
| TRF3 — Juiz Federal | JFMPF | 2010, 2011, 2013, 2016, 2018, 2021, 2025 | 7 | 700 | BANCA PRÓPRIA, CESPE, VUNESP, FGV | não validado |
| DPE/RS — Defensor Público | DEFENSORIAS | 2010, 2014, 2018, 2021, 2025 | 5 | 600 | FCC, CEBRASPE | não validado |
| MPT — Procurador do Trabalho | JTMPT | 2013, 2014, 2017, 2019, 2022, 2024 | 6 | 600 | BANCA PRÓPRIA | não validado |
| TJ/PR — Juiz de Direito | JDMP | 2013, 2014, 2016, 2018, 2021, 2023 | 6 | 600 | BANCA PRÓPRIA, CESPE, FGV | não validado |
| TRF2 — Juiz Federal | JFMPF | 2011, 2013, 2014, 2017, 2018, 2025 | 6 | 600 | CESPE, BANCA PRÓPRIA, FGV | não validado |
| MP/PR — Promotor de Justiça | JDMP | 2013, 2016, 2017, 2018, 2021 | 5 | 525 | BANCA PRÓPRIA | não validado |
| DPE/AM — Defensor Público | DEFENSORIAS | 2011, 2012, 2017, 2021, 2025 | 5 | 500 | INSTITUTO CIDADES, FCC | não validado |
| MP/GO — Promotor de Justiça | JDMP | 2013, 2014, 2016, 2019, 2021 | 5 | 500 | BANCA PRÓPRIA, FGV | não validado |
| PG/DF — Procurador do Estado | PGE | 2006, 2013, 2022 | 3 | 500 | ESAF, CESPE | não validado |
| TJ/GO — Juiz de Direito | JDMP | 2009, 2012, 2014, 2021, 2023 | 5 | 500 | FCC, FGV | não validado |
| TJ/MS — Juiz de Direito | JDMP | 2009, 2012, 2015, 2019, 2023 | 5 | 500 | FCC, PUCPR, VUNESP, FGV | não validado |
| TJ/MT — Juiz de Direito | JDMP | 2006, 2011, 2013, 2018, 2024 | 5 | 500 | VUNESP, FMP CONCURSOS, FGV | não validado |
| TJ/PE — Juiz de Direito | JDMP | 2010, 2012, 2014, 2022, 2024 | 5 | 500 | FCC, FGV | não validado |
| TRF1 — Juiz Federal | JFMPF | 2011, 2013, 2015, 2023, 2025 | 5 | 500 | CESPE, FGV | não validado |
| TRF4 — Juiz Federal | JFMPF | 2010, 2012, 2014, 2016, 2022 | 5 | 500 | BANCA PRÓPRIA | não validado |
| TRF5 — Juiz Federal | JFMPF | 2011, 2013, 2015, 2017, 2025 | 5 | 500 | CESPE, FGV | não validado |
| ENAM — ENAM | ENAM | 2024, 2025, 2026 | 3 | 480 | FGV | não validado |
| PF — Delegado de Polícia Federal | DELEGADO | 2004, 2013, 2018, 2025 | 4 | 480 | CESPE, CEBRASPE | não validado |
| TJ/RJ — Juiz de Direito | JDMP | 2013, 2014, 2015, 2019, 2023, 2024 | 6 | 480 | VUNESP | não validado |
| PGE/PA — Procurador do Estado | PGE | 2011, 2012, 2015, 2022, 2023 | 5 | 460 | BANCA PRÓPRIA, UEPA, CEBRASPE | não validado |
| DPE/ES — Defensor Público | DEFENSORIAS | 2009, 2012, 2016 | 3 | 450 | CESPE, FCC | não validado |

### 7.1 Cobertura por curso interno e ano

| Curso interno | 2004 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADVOGADO DE ESTATAIS | — | 150 | — | 70 | — | 180 | 70 | 60 | 70 | — | 140 | — | — | — | — | — | — | — | — | — | — | — |
| ADVOGADO DO SENADO | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 100 | — | — | — | — |
| AGU | — | — | 300 | — | 200 | 200 | — | 300 | 200 | — | 300 | — | — | — | — | — | — | 300 | — | — | — | — |
| ANALISTA | — | — | 60 | — | 80 | — | 100 | 60 | 100 | — | — | — | — | 100 | — | — | — | — | — | — | — | — |
| DEFENSORIAS | — | — | 400 | 180 | 700 | 450 | 200 | 1038 | 288 | 830 | 488 | 300 | 1000 | 188 | 300 | — | 1290 | 688 | 90 | 100 | 300 | — |
| DELEGADO | 120 | 100 | 180 | 350 | 340 | 200 | 70 | 470 | 450 | 560 | — | 200 | 360 | 860 | — | — | — | — | — | — | 120 | — |
| ENAM | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 240 | 160 | 80 |
| JDMP | — | 100 | 200 | 600 | 400 | 700 | 1200 | 1480 | 1460 | 1960 | 1580 | 800 | 880 | 1105 | 1660 | 100 | 1560 | 1180 | 1260 | 760 | 600 | 100 |
| JFMPF | — | — | — | — | — | 200 | 400 | 220 | 520 | 200 | 320 | 320 | 200 | 200 | — | — | 100 | 220 | 100 | — | 620 | — |
| JTMPT | — | 100 | — | — | — | — | — | — | 200 | 500 | 500 | 400 | 200 | — | 100 | — | — | 100 | 100 | 100 | — | — |
| PGE | — | 100 | 200 | 350 | 420 | 100 | 480 | 270 | 700 | 400 | 80 | 250 | 300 | 390 | — | — | 700 | 700 | 400 | 200 | 400 | — |
| PGM | — | — | 120 | 100 | 50 | 120 | 40 | 200 | 100 | 235 | 330 | 575 | — | 345 | — | — | — | — | — | — | 100 | — |

Onde há zero, não existe agrupamento daquela trilha naquele ano. Os buracos mais visíveis: **ENAM só a partir de 2024** (o exame foi criado em 2023), **AGU sem registros desde 2022**, **ADVOGADO DE ESTATAIS desde 2015**, **ANALISTA desde 2018** e **ADVOGADO DO SENADO com uma única aparição, em 2022**.

---

## 8. Lacunas e inconsistências

São 17 achados registrados. Panorama por severidade:

| Severidade | Quantidade | IDs |
|---|---|---|
| alta | 5 | INC-002, INC-003, INC-004, INC-009, INC-016 |
| media | 6 | INC-001, INC-007, INC-008, INC-010, INC-011, INC-017 |
| baixa | 2 | INC-005, INC-006 |
| informativa | 4 | INC-012, INC-013, INC-014, INC-015 |

Os de severidade alta são os que exigem decisão humana antes de qualquer uso analítico da base.

### INC-001 — O ID 793 ('IBGP', Tipo=Banca) aparece duas vezes na aba Lista, com conteúdo idêntico.
- **Tipo:** chave_duplicada · **Severidade:** media
- **Onde:** Lista, ID 793
- **O quê:** O ID 793 ('IBGP', Tipo=Banca) aparece duas vezes na aba Lista, com conteúdo idêntico.
- **Impacto:** Qualquer VLOOKUP retorna a primeira ocorrência; não há divergência de valor, mas a chave deixa de ser única.
- **Sugestão:** Remover a linha duplicada e adicionar restrição de unicidade em Lista.ID.
- **Suposições feitas:** nenhuma

### INC-002 — O valor 620 na coluna 'ID Cargo' não existe na aba Lista.
- **Tipo:** chave_estrangeira_orfa · **Severidade:** alta
- **Onde:** Base_sem duplic, ID Cargo = 620 (200 questões)
- **O quê:** O valor 620 na coluna 'ID Cargo' não existe na aba Lista.
- **Impacto:** 200 questões ficam sem cargo identificável: TCE/RS 2013 (banca registrada como 'BANCA PRÓPRIA') e TCE/PA 2011 (AOCP), ambas na trilha interna ANALISTA.
- **Sugestão:** Consultar o sistema de origem para recuperar o cadastro do ID 620.
- **Suposições feitas:** nenhuma — o cargo NÃO foi inferido

### INC-003 — A coluna 'ID Banca' aponta para o ID 3, que na Lista é '(TESTE) Cargo XY', cadastrado com Tipo='Cargo' e claramente um registro de teste.
- **Tipo:** chave_estrangeira_tipo_incorreto · **Severidade:** alta
- **Onde:** Base_sem duplic, ID Banca = 3 (1.090 questões)
- **O quê:** A coluna 'ID Banca' aponta para o ID 3, que na Lista é '(TESTE) Cargo XY', cadastrado com Tipo='Cargo' e claramente um registro de teste.
- **Impacto:** 1.090 questões em 13 agrupamentos técnicos ficam sem banca confiável — cargos de Delegado de Polícia Civil, Investigador de Polícia e cargos de tribunais, nos anos 2006, 2007, 2008, 2009, 2012, 2014, 2017 e 2018.
- **Sugestão:** Reatribuir a banca correta agrupamento a agrupamento, a partir dos editais originais.
- **Suposições feitas:** nenhuma

### INC-004 — A coluna 'ID Órgão' aponta para o ID 20 ('TJ/PR'), cadastrado na Lista com Tipo='Banca'.
- **Tipo:** chave_estrangeira_tipo_incorreto · **Severidade:** alta
- **Onde:** Base_sem duplic, ID Órgão = 20 (200 questões)
- **O quê:** A coluna 'ID Órgão' aponta para o ID 20 ('TJ/PR'), cadastrado na Lista com Tipo='Banca'. O TJ/PR também existe como órgão sob o ID 155.
- **Impacto:** 200 questões (Juiz de Direito, FGV, 2021 e 2023, trilha interna JDMP) ficam vinculadas ao cadastro errado; risco de dupla contagem entre os IDs 20 e 155.
- **Sugestão:** Redirecionar para o ID 155 após confirmação com a área responsável.
- **Suposições feitas:** nenhuma — a correção NÃO foi aplicada nesta base

### INC-005 — Dois cargos distintos com o mesmo nome 'Simulado Procurador da Fazenda Nacional' (ambos Inativos).
- **Tipo:** nomes_duplicados · **Severidade:** baixa
- **Onde:** Lista, IDs 610 e 611
- **O quê:** Dois cargos distintos com o mesmo nome 'Simulado Procurador da Fazenda Nacional' (ambos Inativos).
- **Impacto:** Nenhum sobre a base atual (nenhum dos dois é usado em questões).
- **Sugestão:** Consolidar ou diferenciar os nomes.
- **Suposições feitas:** nenhuma

### INC-006 — Cinco órgãos distintos com o nome idêntico 'Simulado TJ-RJ-Simulado TJ-RJ' (todos Inativos).
- **Tipo:** nomes_duplicados · **Severidade:** baixa
- **Onde:** Lista, IDs 363 a 367
- **O quê:** Cinco órgãos distintos com o nome idêntico 'Simulado TJ-RJ-Simulado TJ-RJ' (todos Inativos).
- **Impacto:** Nenhum sobre a base atual (nenhum é usado em questões).
- **Sugestão:** Consolidar em um único registro ou nomear por edição.
- **Suposições feitas:** nenhuma

### INC-007 — A dimensão 'Banca' mistura três coisas: bancas de mercado (FGV, FCC), o rótulo genérico 'BANCA PRÓPRIA' e siglas de órgãos (TJ/BA, MP/BA, DPE/BA, TJ/PR, MP/PR, DPE/PR) cadastradas como se fossem bancas.
- **Tipo:** nomenclatura_inconsistente · **Severidade:** media
- **Onde:** Lista, Tipo='Banca'
- **O quê:** A dimensão 'Banca' mistura três coisas: bancas de mercado (FGV, FCC), o rótulo genérico 'BANCA PRÓPRIA' e siglas de órgãos (TJ/BA, MP/BA, DPE/BA, TJ/PR, MP/PR, DPE/PR) cadastradas como se fossem bancas.
- **Impacto:** Impede contagem confiável por banca organizadora e cria ambiguidade com a dimensão Órgão. O significado exato de 'BANCA PRÓPRIA' não está documentado em lugar algum da base.
- **Sugestão:** Documentar formalmente o que 'BANCA PRÓPRIA' significa no sistema de origem e, só depois, decidir como normalizar. Não interpretar caso a caso sem evidência oficial.
- **Suposições feitas:** nenhuma — nenhum registro 'BANCA PRÓPRIA' recebeu interpretação

### INC-008 — Mesma instituição em dois cadastros, referentes a períodos diferentes (13.
- **Tipo:** entidade_duplicada_logicamente · **Severidade:** media
- **Onde:** Lista, IDs 4 (CESPE) e 46 (CEBRASPE)
- **O quê:** Mesma instituição em dois cadastros, referentes a períodos diferentes (13.185 e 3.920 questões respectivamente).
- **Impacto:** Qualquer análise por banca subestima o volume do Cebraspe se não somar os dois IDs.
- **Sugestão:** Manter os dois IDs por rastreabilidade histórica e usar o agrupador lógico sugerido em 'sugestoes_de_normalizacao'. Nenhuma fusão foi aplicada.
- **Suposições feitas:** nenhuma

### INC-009 — A base não possui data da prova, número/ano do edital, identificador do certame, nem link para o edital.
- **Tipo:** campo_ausente · **Severidade:** alta
- **Onde:** Base_sem duplic (estrutura)
- **O quê:** A base não possui data da prova, número/ano do edital, identificador do certame, nem link para o edital. O ano é a única âncora temporal.
- **Impacto:** Impossível distinguir dois concursos oficiais do mesmo órgão/cargo no mesmo ano, nem casar registros com fontes oficiais. É a razão pela qual 'concurso_oficial_id' permanece null em todos os 485 agrupamentos.
- **Sugestão:** Incluir os campos data_prova, numero_edital e url_edital.
- **Suposições feitas:** nenhuma — data_prova foi preenchida com null em todos os registros

### INC-010 — 11.
- **Tipo:** lacuna_de_preenchimento · **Severidade:** media
- **Onde:** Base_sem duplic, coluna ID TEMA
- **O quê:** 11.881 de 51.190 questões (23,2%) estão sem ID TEMA e, por consequência, sem Tema, Tema Pai e Disciplina.
- **Impacto:** Reduz a cobertura de qualquer análise por disciplina.
- **Sugestão:** Priorizar classificação temática das provas mais recentes.
- **Suposições feitas:** nenhuma

### INC-011 — 988 questões estão sem gabarito e 614 estão marcadas como 'ANULADA'.
- **Tipo:** lacuna_de_preenchimento · **Severidade:** media
- **Onde:** Base_sem duplic, coluna Certa
- **O quê:** 988 questões estão sem gabarito e 614 estão marcadas como 'ANULADA'. 13 questões estão sem enunciado.
- **Impacto:** Questões sem gabarito não são utilizáveis; anuladas precisam de tratamento próprio.
- **Sugestão:** Revisar as 988 sem gabarito e as 13 sem enunciado.
- **Suposições feitas:** nenhuma

### INC-012 — Todas as colunas 'NM .
- **Tipo:** colunas_derivadas · **Severidade:** informativa
- **Onde:** Base_sem duplic, colunas W a AR
- **O quê:** Todas as colunas 'NM ...', 'Tema', 'Disciplina', 'IDs Lista', 'Nome Resumido' e 'Tema Pai II' são fórmulas (PROCV/CONCAT) sobre as abas Lista e HC, e não dados armazenados.
- **Impacto:** São reproduzíveis, mas quebram se a ordem das abas mudar; não devem ser tratadas como fonte primária.
- **Sugestão:** Materializar as junções no banco de origem em vez de na planilha.
- **Suposições feitas:** nenhuma

### INC-013 — 119 dos 301 órgãos, 19 das 49 bancas e 53 dos 76 cargos cadastrados não possuem nenhuma questão vinculada nesta extração.
- **Tipo:** cadastro_sem_uso · **Severidade:** informativa
- **Onde:** Lista
- **O quê:** 119 dos 301 órgãos, 19 das 49 bancas e 53 dos 76 cargos cadastrados não possuem nenhuma questão vinculada nesta extração.
- **Impacto:** Cadastro maior que a cobertura real; pode indicar planejamento futuro ou resíduo.
- **Sugestão:** Confirmar com a área quais são backlog e quais são obsoletos.
- **Suposições feitas:** nenhuma

### INC-014 — Todas as 51.
- **Tipo:** escopo_da_extracao · **Severidade:** informativa
- **Onde:** Base_sem duplic, coluna ID Base Produto Vinculado
- **O quê:** Todas as 51.190 questões pertencem ao produto 'Questões de Concursos' (ID 792). O produto 'Questões Inéditas' (ID 791) existe no cadastro mas não aparece nesta extração; as colunas ID Simulado e NM Tutor estão 100% vazias.
- **Impacto:** Esta extração cobre apenas questões atribuídas a provas de concurso, não o acervo inteiro do Ênfase.
- **Sugestão:** Confirmar se existe uma segunda base com as questões inéditas e simulados.
- **Suposições feitas:** nenhuma

### INC-015 — A coluna admite Objetiva, Discursiva e Oral, mas as 51.
- **Tipo:** dominio_subutilizado · **Severidade:** informativa
- **Onde:** Base_sem duplic, coluna Tipo (O/D/R)
- **O quê:** A coluna admite Objetiva, Discursiva e Oral, mas as 51.190 questões são objetivas.
- **Impacto:** Não há cobertura de 2ª fase (discursiva) nem de prova oral no banco.
- **Sugestão:** Definir se discursivas/orais entrarão nesta base ou em outra.
- **Suposições feitas:** nenhuma

### INC-016 — A combinação Órgão × Banca × Ano × Cargo × Curso não comprova a existência de uma prova oficial individual, e a combinação Órgão + Cargo não equivale a um concurso oficial individual.
- **Tipo:** modelagem · **Severidade:** alta
- **Onde:** Interpretação da base (achado da revisão de 03/08/2026)
- **O quê:** A combinação Órgão × Banca × Ano × Cargo × Curso não comprova a existência de uma prova oficial individual, e a combinação Órgão + Cargo não equivale a um concurso oficial individual.
- **Impacto:** Tratar os 485 agrupamentos como 'provas' e as 187 famílias como 'concursos' produziria contagens falsamente precisas. Um mesmo concurso oficial pode gerar mais de um agrupamento, e uma família reúne vários concursos oficiais de anos diferentes.
- **Sugestão:** Manter a distinção entre agrupamento técnico, família e concurso oficial. Só preencher concurso_oficial_id ao vincular um edital específico.
- **Suposições feitas:** nenhuma

### INC-017 — O campo Curso (JDMP, JFMPF, JTMPT, PGE, AGU, ENAM, DEFENSORIAS, DELEGADO, PGM, ANALISTA, ADVOGADO DE ESTATAIS, ADVOGADO DO SENADO) é uma trilha comercial interna do Ênfase, não uma carreira oficial.
- **Tipo:** classificacao_interna_vs_oficial · **Severidade:** media
- **Onde:** Base_sem duplic, colunas ID/NM Curso
- **O quê:** O campo Curso (JDMP, JFMPF, JTMPT, PGE, AGU, ENAM, DEFENSORIAS, DELEGADO, PGM, ANALISTA, ADVOGADO DE ESTATAIS, ADVOGADO DO SENADO) é uma trilha comercial interna do Ênfase, não uma carreira oficial.
- **Impacto:** Siglas como JDMP agregam mais de uma carreira (magistratura estadual e Ministério Público estadual). Tratá-las como carreira oficial produziria uma taxonomia inventada.
- **Sugestão:** Construir um mapeamento curso → carreira oficial validado pela área, com regra e evidência registradas, e preencher carreira_normalizada_* só então.
- **Suposições feitas:** nenhuma — carreira_normalizada_id e _nome permanecem null em 100% dos registros

### Sugestões de normalização (nenhuma aplicada)

Registradas em `sugestoes_de_normalizacao`, sem apagar nenhuma origem:

| ID | Tipo | Descrição | Agrupador sugerido | IDs internos | Aplicada? |
|---|---|---|---|---|---|
| NORM-001 | agrupamento_logico_de_banca | CESPE (ID interno 4) e CEBRASPE (ID interno 46) referem-se à mesma instituição em períodos diferentes. | INST-CESPE-CEBRASPE | 4, 46 | não |
| NORM-002 | deduplicacao_de_chave | ID 793 (IBGP) duplicado na aba Lista. | — | 793 | não |
| NORM-003 | conflito_de_cadastro | TJ/PR existe como ID 20 (cadastrado com Tipo='Banca') e como ID 155 (Tipo='Orgão'). | ORG-TJ-PR | 20, 155 | não |

---

## 9. Resumo de cobertura

### 9.1 O que já existe na base

| Item | Situação |
|---|---|
| Questões | 51.190, todas objetivas, sem duplicidade de `Id da Questao` |
| Agrupamentos técnicos de prova | 485, todos com chave composta de origem |
| Famílias de concurso | 187 séries históricas órgão + cargo |
| Órgãos | 182 referenciados, cobrindo TJs, MPs, DPEs, PGEs, PGMs, PCs, TRFs, TRTs, TCEs |
| Bancas | 30 valores distintos no campo de banca |
| Cargos | 22 cargos resolvíveis no cadastro |
| Cursos internos | 12 trilhas do Ênfase com questões |
| Anos | 22 anos com questões, de 2004 a 2026 |
| Blocos | 15.383 questões com bloco atribuído |
| Edições | 2.280 questões com edição atribuída |
| Classificação predominante | 9.453 questões classificadas |
| Temas | 39.309 questões com tema, disciplina e tema raiz via aba HC |
| Gabaritos | 49.588 preenchidos |
| Rastreabilidade | 51.190 vínculos questão → agrupamento → linha de origem |
| Fontes oficiais | 16 verificadas, com URL direta e data de verificação |

### 9.2 O que ainda não existe na base

Campos e entidades que **simplesmente não estão na origem** — nenhuma quantidade de processamento os produziria.

| Ausente | Consequência | Referência |
|---|---|---|
| Identificador de concurso oficial | Nenhum registro pode ser vinculado a um certame | INC-009 |
| Data da prova | Só existe o ano; dois certames do mesmo ano são indistinguíveis | INC-009 |
| Número e ano do edital | Impossível casar com publicação em diário oficial | INC-009 |
| URL do edital | Nenhum caminho automático para a evidência oficial | INC-009 |
| Carreira oficial | Só existe a trilha comercial interna | INC-017 |
| Questões discursivas | 0 registros, embora o modelo preveja o tipo | INC-015 |
| Questões orais | 0 registros, embora o modelo preveja o tipo | INC-015 |
| Vínculo com simulado | Coluna `ID Simulado` 100% vazia | INC-014 |
| Questões inéditas | Produto 791 existe no cadastro mas não nesta extração | INC-014 |
| Tutor responsável | Colunas de tutor 100% vazias | INC-014 |
| Dicionário de dados do sistema | Modelo reconstruído a partir da planilha | seção 3 |

### 9.3 O que ainda depende de validação

Itens que existem, mas cuja interpretação exige confirmação humana ou pesquisa individual.

| Pendência | Volume afetado | Quem resolve | Referência |
|---|---|---|---|
| Significado do rótulo `BANCA PRÓPRIA` | 9.510 questões / 87 agrupamentos | área responsável pelo cadastro | INC-007 |
| Banca real das questões com ID 3 (registro de teste) | 1.090 questões / 13 agrupamentos | consulta aos editais originais | INC-003 |
| Cargo do ID interno 620 (chave órfã) | 200 questões | sistema de origem | INC-002 |
| Órgão TJ/PR: ID 20 ou ID 155 | 200 questões | área responsável | INC-004 |
| Mapeamento curso interno → carreira oficial | todas as 51.190 | área pedagógica | INC-017 |
| ID 793 (IBGP) duplicado | cadastro | área responsável | INC-001 / NORM-002 |
| Agrupar ou não CESPE e CEBRASPE | 17.105 questões | decisão de modelagem | INC-008 / NORM-001 |
| 119 órgãos, 19 bancas e 53 cargos sem uso | cadastro | área responsável | INC-013 |
| Fontes oficiais de 179 órgãos | monitoramento externo | pesquisa individual | PEND-001 |
| Fontes oficiais de 23 bancas | monitoramento externo | pesquisa individual | PEND-002 |
| Data efetiva do ENAM 2026.1 e do concurso do MPF | 2 certames | ato oficial de realização | FUT-001 / FUT-004 |

---

## 10. Rastreabilidade e o arquivo auxiliar

### 10.1 Por que ele existe

O critério de aceitação exige que cada registro estruturado seja rastreável até a origem interna. Faixas de ID e amostras não cumprem isso: se alguém precisar auditar uma questão específica, ou reconstruir um agrupamento a partir da planilha bruta, precisa do vínculo individual. O arquivo `rastreabilidade-agrupamentos-questoes.json` guarda esse vínculo para **todas as 51.190 questões**, sem exceção e sem amostragem.

### 10.2 Como se relaciona com o inventário

Cada agrupamento no inventário mantém, em `origem_interna`: o arquivo e a aba de origem, a chave composta com os cinco IDs internos, a quantidade de questões, as faixas de ID e de linha, e a referência explícita a este arquivo auxiliar. O campo `agrupamento_tecnico_id` é a chave que liga os dois lados.

```json
{
  "agrupamento_tecnico_id": "AGR-...",
  "questao_id": 1571,
  "linha_origem": 2
}
```

`linha_origem` é a linha física na aba `Base_sem duplic`: a linha 1 é o cabeçalho, a primeira questão está na linha 2.

### 10.3 Quando usá-lo

- Auditar a procedência de uma questão específica.
- Reconstruir integralmente um agrupamento a partir da planilha original.
- Conferir que nenhuma questão foi perdida ou contada duas vezes.
- Aplicar correções em lote depois que as chaves quebradas forem resolvidas.
- Servir de tabela de ligação ao migrar o inventário para um banco relacional.

### 10.4 Por que foi separado

São 51.190 vínculos. Embutidos no inventário, eles multiplicariam seu tamanho por cerca de quatro e enterrariam catálogos, métricas e inconsistências no meio de listas de IDs — tornando o arquivo principal desconfortável de abrir e de revisar. A separação é apenas física: o auxiliar é parte integrante do conjunto de entregáveis e está referenciado nos quatro demais arquivos.

---

## 11. Próximos passos recomendados

Em ordem de prioridade. Os quatro primeiros são pré-requisitos dos demais: sem eles, qualquer automação herdará os problemas atuais.

| # | Ação | Por quê | Referência |
|---|---|---|---|
| 1 | **Validar as inconsistências internas com a área responsável** | 17 achados estão documentados, mas nenhum pode ser corrigido sem confirmação — corrigir por conta própria substituiria um erro conhecido por uma suposição invisível | INC-001 a INC-017 |
| 2 | **Resolver as três chaves quebradas** | 1.490 questões estão hoje com banca, cargo ou órgão não confiáveis; qualquer relatório por banca ou por órgão já sai errado nessa fatia | INC-002, INC-003, INC-004 |
| 3 | **Documentar formalmente o que significa `BANCA PRÓPRIA`** | São 9.510 questões em 87 agrupamentos sob um rótulo sem definição. Normalizar antes de definir seria escolher um significado no lugar de quem sabe | INC-007 |
| 4 | **Construir o mapeamento curso interno → carreira oficial** | Permite falar com o mercado na linguagem do mercado; precisa de regra e evidência por linha, não de dedução automática | INC-017 |
| 5 | **Incluir `data_prova`, `numero_edital` e `url_edital` na base e fazer o retrofit** | É a ponte que falta entre acervo interno e mundo externo; começar por 2023 em diante, enquanto os editais ainda estão publicados nos sites das bancas | INC-009 |
| 6 | **Identificar os concursos oficiais e preencher `concurso_oficial_id`** | Só se torna possível depois do passo 5; é o que transforma 485 agrupamentos técnicos em certames identificados | seção 4.3 |
| 7 | **Completar o mapa de fontes oficiais** | 179 órgãos e 23 bancas ainda sem fonte verificada; o protocolo passo a passo já está escrito no guia de fontes | PEND-001, PEND-002 |
| 8 | **Impor unicidade e integridade referencial no sistema de origem** | Evita que novas chaves quebradas apareçam; hoje nada impede que o campo de banca aponte para um cargo | INC-001, INC-007 |
| 9 | **Classificar os cadastros sem uso entre backlog e obsoleto** | 119 órgãos, 19 bancas e 53 cargos nunca usados; sem essa triagem, o monitoramento externo perseguiria alvos irrelevantes | INC-013 |
| 10 | **Iniciar a automação do monitoramento** | Último da fila por dependência: um agente automático só agrega valor quando existir campo de edital para casar o que ele encontra com o que já está na base | guia de fontes, seção 8 |

---

## 12. Critérios de aceitação

Os oito critérios definidos na abertura do trabalho, com avaliação individual.

**1. Todos os concursos, carreiras, bancas e provas identificáveis no banco foram considerados.**  
*Situação:* **Atendido, com ressalva de terminologia**  
As 51.190 questões foram processadas sem amostragem, gerando 485 agrupamentos técnicos e 187 famílias, com catálogo completo de 301 órgãos, 49 bancas, 76 cargos e 22 cursos internos — inclusive os cadastrados sem uso. **Ressalva:** o critério fala em 'concursos', 'carreiras' e 'provas', e o inventário demonstra que essas três entidades não são identificáveis na base como tais. O que existe são agrupamentos, famílias e trilhas internas. A terminologia foi ajustada em vez de forçar os dados a caberem no vocabulário original.

**2. Markdown e JSON representam a mesma base, sem divergências relevantes.**  
*Situação:* **Atendido**  
Este Markdown é gerado programaticamente a partir do JSON, o que elimina divergência por construção. A validação automática confere as três quantidades estruturais (51.190 / 485 / 187), as definições dos três conceitos e a contagem de fontes entre os dois formatos.

**3. Cada registro estruturado possui rastreabilidade até a origem interna.**  
*Situação:* **Atendido**  
Os 485 agrupamentos trazem arquivo, aba, chave composta com os cinco IDs internos, quantidade de questões e faixas de ID e de linha. Além disso, as 51.190 questões têm vínculo individual no arquivo auxiliar, com a linha física da planilha — rastreabilidade completa, não amostral.

**4. Cada fonte externa é oficial e possui URL direta; agregadores e portais não oficiais não são aceitos como fonte primária.**  
*Situação:* **Atendido, com cobertura parcial**  
As 16 fontes registradas são todas oficiais, com URL direta, método de verificação e data. Agregadores foram usados apenas como pista de busca. **Limitação:** a cobertura não é exaustiva — 179 órgãos e 23 bancas seguem sem fonte verificada, registrados como PEND-001 e PEND-002 com protocolo de resolução. Preferiu-se deixar a lacuna explícita a preenchê-la por padrão de nomenclatura.

**5. Datas futuras distinguem claramente `confirmada`, `prevista` e `sem data`.**  
*Situação:* **Atendido**  
As três classes estão definidas no guia de fontes e aplicadas aos quatro certames registrados. A revisão acrescentou a distinção entre confirmar que um evento ocorreu e confirmar a data em que ocorreu, com campos próprios para a primeira.

**6. Toda data confirmada possui evidência oficial e data de verificação.**  
*Situação:* **Atendido por vacuidade**  
**Não há nenhuma data classificada como `confirmada`.** O ENAM 2026.1 e o concurso do MPF foram rebaixados para `prevista` porque as fontes localizadas anunciam as datas como prováveis. No caso do ENAM existe ato oficial da ENFAM comprovando a realização, mas ele não declara a data de aplicação — a realização foi registrada em campo separado, com URL e data de verificação.

**7. Duplicidades, conflitos e lacunas estão documentados sem suposições.**  
*Situação:* **Atendido**  
17 inconsistências, cada uma com local, impacto, ação sugerida e um campo explícito de suposições — preenchido com 'nenhuma' em todas. Nenhuma entidade foi fundida; as três sugestões de normalização estão marcadas como não aplicadas.

**8. O material final permite que outro agente continue o monitoramento sem depender de contexto oral.**  
*Situação:* **Atendido**  
O guia de fontes traz critério de admissão, classificação de datas, rotina de monitoramento por periodicidade, protocolo passo a passo para as pendências e o registro do bloqueio anti-bot do CNJ. Este documento traz modelo de dados, limitações metodológicas e roadmap priorizado. Ambos são gerados a partir dos JSON, que são legíveis por máquina.

**Resultado:** 8 de 8 critérios atendidos — 3 deles com limitação explicitada acima (terminologia ajustada, cobertura parcial de fontes e ausência de datas confirmadas).
