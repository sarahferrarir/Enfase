# Fontes oficiais de concursos — guia de monitoramento

| Item | Valor |
|---|---|
| Data da verificação inicial | 29 de julho de 2026 |
| Data da revisão | 3 de agosto de 2026 |
| Base estruturada equivalente | `fontes-oficiais-concursos.json` |
| Base de entidades vinculada | `inventario-banco-questoes.json` |
| Relatório humano do inventário | `inventario-banco-questoes.md` |
| Rastreabilidade das questões | `rastreabilidade-agrupamentos-questoes.json` |

## 1. Para que serve este documento

Ele existe para que outra pessoa — ou um agente automatizado — consiga acompanhar concursos das trilhas cobertas pelo banco de questões do Ênfase **sem depender de contexto verbal**, consultando apenas fontes primárias oficiais. O documento irmão, `inventario-banco-questoes.md`, descreve o que já existe no acervo interno; este descreve onde buscar o que acontece fora dele.

## 2. Terminologia

Este mapa usa a mesma terminologia do inventário: 'agrupamento técnico de prova' (485 na base) para a combinação interna Órgão × Banca × Ano × Cargo × Curso; 'família de concurso' (187) para a série histórica Órgão + Cargo; e 'concurso oficial' apenas para o certame identificado por evidência externa. Nenhum registro interno está hoje vinculado a um concurso oficial. As siglas JDMP, PGE, DEFENSORIAS, ENAM e afins são cursos/trilhas internas do Ênfase, não carreiras oficiais.

## 3. Regra de admissão de fontes

Somente fontes primárias oficiais: sites do órgão promotor, sites da banca organizadora contratada, diários oficiais e documentos oficiais (editais, comunicados). Agregadores, portais de notícias de concurso, cursinhos e sites de questões foram usados apenas como pista de busca e NUNCA registrados como fonte.

Na prática, isso significa que sites como PCI Concursos, JC Concursos, Qconcursos, Tec Concursos, Gran, Estratégia, MEGE, Magistrar e afins **não entram neste mapa**, nem mesmo como fonte secundária. Eles foram usados apenas como pista para localizar o endereço oficial, e o que ficou registrado foi sempre o endereço oficial.

## 4. Classificação de datas

- **`confirmada`** — existe ato oficial que declara a data de realização do evento — não basta um edital que anuncie a data como provável ou prevista. Exige URL e data de verificação registradas
- **`prevista`** — o certame está em curso ou anunciado oficialmente e pode haver data anunciada em ato oficial como provável ou prevista, mas não há ato que declare a data de realização efetiva
- **`sem_data`** — não há ato oficial localizado; qualquer data que circule vem de fonte não oficial e não é registrada aqui

**Realização e data são coisas distintas.** Quando existe ato oficial provando a realização mas nenhum que declare a data, a data permanece 'prevista' e a realização é registrada nos campos 'realizacao_confirmada', 'tipo_confirmacao' e 'url_evidencia_realizacao'.

**Sobre o vínculo com a base.** O campo 'presente_na_base_enfase' indica que existe um agrupamento técnico com o mesmo órgão, cargo e ano — não que o material da base tenha sido confirmadamente extraído daquele certame específico. Essa vinculação depende de campos de edital que a base ainda não possui (INC-009).

## 5. Fontes verificadas

São 16 fontes. Cobrem o Diário Oficial da União, o diretório oficial de tribunais, as seis bancas responsáveis pelo maior volume da base e três órgãos ou exames com página própria de certames.

| ID | Entidade | Tipo | URL | Publica | Periodicidade |
|---|---|---|---|---|---|
| FONTE-DOU-001 | Imprensa Nacional (DOU) | diario_oficial | https://www.in.gov.br/leiturajornal | edital, retificacao, convocacao, homologacao | diaria |
| FONTE-DOU-002 | Imprensa Nacional (DOU) | diario_oficial | https://www.in.gov.br/servicos/diario-oficial-da-uniao | indice de servicos, base de dados de publicacoes, concursos e selecoes | mensal |
| FONTE-CNJ-001 | Conselho Nacional de Justiça | orgao_de_controle | https://www.cnj.jus.br/poder-judiciario/tribunais/ | diretorio oficial de tribunais e seus sites | semestral |
| FONTE-BANCA-CEBRASPE | Cebraspe | banca | https://www.cebraspe.org.br/concursos/ | edital, cronograma, gabarito, resultado | semanal |
| FONTE-BANCA-FGV | FGV Conhecimento | banca | https://conhecimento.fgv.br/concursos | edital, cronograma, gabarito, resultado | semanal |
| FONTE-BANCA-FCC | Fundação Carlos Chagas | banca | https://www.concursosfcc.com.br/ | edital, inscricoes, cronograma, gabarito | semanal |
| FONTE-BANCA-FCC-INST | Fundação Carlos Chagas | banca | https://www.fcc.org.br/concursos/ | institucional, concursos em andamento, instituicoes atendidas | mensal |
| FONTE-BANCA-VUNESP | Fundação Vunesp | banca | https://www.vunesp.com.br/concursos.html | edital, cronograma, gabarito, resultado | semanal |
| FONTE-BANCA-CESGRANRIO | Fundação Cesgranrio | banca | https://www.cesgranrio.org.br/concursos/ | edital, cronograma, gabarito, resultado | mensal |
| FONTE-BANCA-FUNDATEC | Fundatec | banca | https://www.fundatec.org.br/portal/concursos/ | edital, cronograma, gabarito, resultado | mensal |
| FONTE-ENFAM-001 | ENFAM — Escola Nacional de Formação e Aperfeiçoamento de Magistrados | orgao | https://www.enfam.jus.br/enam/normativos/ | edital, comunicado, resultado, normativos | semanal |
| FONTE-ENAM-FGV-5 | FGV Conhecimento (executora) / ENFAM (instituidora) | banca | https://conhecimento.fgv.br/exames/enam/5exame | edital, cronograma, gabarito, resultado | semanal |
| FONTE-ENAM-EDITAL-2026-1 | ENFAM / FGV | edital | https://conhecimento.fgv.br/sites/default/files/concursos/edital-enam-2026_1.v2.1-1_0.pdf | edital de abertura, cronograma, conteudo programatico, estrutura da prova | pontual |
| FONTE-ENAM-RESULT-2026-1 | ENFAM | edital | https://hdl.handle.net/20.500.14782/593 | relacao de habilitados, resultado da prova objetiva | pontual |
| FONTE-MPF-001 | Ministério Público Federal / PGR | orgao | https://www.mpf.mp.br/o-mpf/concursos | edital, regulamento, cronograma, gabarito | mensal |
| FONTE-AGU-001 | Advocacia-Geral da União | orgao | https://www.gov.br/agu/pt-br/concursos | edital, comunicado, resultado, orientacoes aos aprovados | mensal |

### 5.1 Detalhamento

#### FONTE-DOU-001 — Imprensa Nacional (DOU)
- **URL:** https://www.in.gov.br/leiturajornal
- **Tipo de informação:** edital, retificacao, convocacao, homologacao, resultado, nomeacao
- **Concursos relacionados:** todos os concursos federais e todos os certames cujos atos são publicados no DOU, incluindo o ENAM
- **Periodicidade sugerida:** diaria
- **Verificação:** resultado de busca no domínio oficial in.gov.br — 2026-07-31
- **Evidência:** Página oficial de leitura do DOU da Imprensa Nacional.
- **Observações:** Edição do dia. Para busca retroativa use https://www.in.gov.br/consulta/. A Seção 3 concentra editais de concurso público; a Seção 2, atos de provimento.

#### FONTE-DOU-002 — Imprensa Nacional (DOU)
- **URL:** https://www.in.gov.br/servicos/diario-oficial-da-uniao
- **Tipo de informação:** indice de servicos, base de dados de publicacoes, concursos e selecoes
- **Concursos relacionados:** transversal
- **Periodicidade sugerida:** mensal
- **Verificação:** resultado de busca no domínio oficial in.gov.br — 2026-07-31
- **Evidência:** Página de serviços do DOU; lista o serviço 'Concursos e Seleções' e a base de dados de publicações.
- **Observações:** Porta de entrada para os serviços estruturados do DOU, úteis para automação futura.

#### FONTE-CNJ-001 — Conselho Nacional de Justiça
- **URL:** https://www.cnj.jus.br/poder-judiciario/tribunais/
- **Tipo de informação:** diretorio oficial de tribunais e seus sites
- **Concursos relacionados:** todos os concursos de TJ, TRF e TRT presentes na base
- **Periodicidade sugerida:** semestral
- **Verificação:** URL retornada em busca; conteúdo confirmado em snippet oficial do CNJ — 2026-07-31
- **Evidência:** Página do CNJ que relaciona TRFs 1 a 6 e os tribunais estaduais e militares.
- **Observações:** ATENÇÃO: o acesso automatizado a cnj.jus.br foi bloqueado por proteção anti-bot em 31/07/2026. A leitura precisa ser feita por navegador. Esta é a fonte oficial recomendada para resolver os domínios de todos os tribunais ainda pendentes.

#### FONTE-BANCA-CEBRASPE — Cebraspe
- **URL:** https://www.cebraspe.org.br/concursos/
- **Tipo de informação:** edital, cronograma, gabarito, resultado, provas aplicadas
- **Concursos relacionados:** AGU — Advogado da União, AGU — Procurador Federal, PGFN — Procurador da Fazenda Nacional, PF — Delegado de Polícia Federal, PGE/PR, PGE/ES, PGE/PI, demais certames CESPE/CEBRASPE da base
- **Periodicidade sugerida:** semanal
- **Verificação:** acesso direto (HTTP 200) em 31/07/2026 — 2026-07-31
- **Evidência:** Página oficial de concursos do Cebraspe.
- **Observações:** Cobre também o histórico das provas aplicadas sob a marca CESPE (ID interno 4).

#### FONTE-BANCA-FGV — FGV Conhecimento
- **URL:** https://conhecimento.fgv.br/concursos
- **Tipo de informação:** edital, cronograma, gabarito, resultado, recursos
- **Concursos relacionados:** ENAM (todas as edições), TJ/BA 2026, TJ/PE, TJ/SC, TJ/CE, TJ/TO, TJ/MT, TJ/SE, TRF1, TRF2, TRF3, TRF5, TRF6, MP/ES, MP/RJ, DPE/PE, DPE/RJ, PC/PR
- **Periodicidade sugerida:** semanal
- **Verificação:** resultado de busca no domínio oficial conhecimento.fgv.br — 2026-07-31
- **Evidência:** Página oficial de concursos da FGV Conhecimento, listando certames em andamento.
- **Observações:** É a banca com maior participação nas provas recentes da base (2024–2026).

#### FONTE-BANCA-FCC — Fundação Carlos Chagas
- **URL:** https://www.concursosfcc.com.br/
- **Tipo de informação:** edital, inscricoes, cronograma, gabarito, resultado
- **Concursos relacionados:** DPE/AM, DPE/RS, PGE/MT, PGE/TO, PGE/GO, PGM Manaus/AM, demais certames FCC da base
- **Periodicidade sugerida:** semanal
- **Verificação:** resultado de busca no domínio oficial concursosfcc.com.br — 2026-07-31
- **Evidência:** Portal oficial de concursos da FCC, com a relação de inscrições abertas.
- **Observações:** Em 31/07/2026 constava inscrição aberta para Procurador do Município de 3ª Classe da Procuradoria-Geral do Município de Manaus — órgão presente na base (PGM Manaus/AM).

#### FONTE-BANCA-FCC-INST — Fundação Carlos Chagas
- **URL:** https://www.fcc.org.br/concursos/
- **Tipo de informação:** institucional, concursos em andamento, instituicoes atendidas
- **Concursos relacionados:** transversal FCC
- **Periodicidade sugerida:** mensal
- **Verificação:** resultado de busca no domínio oficial fcc.org.br — 2026-07-31
- **Evidência:** Página institucional de concursos da FCC.

#### FONTE-BANCA-VUNESP — Fundação Vunesp
- **URL:** https://www.vunesp.com.br/concursos.html
- **Tipo de informação:** edital, cronograma, gabarito, resultado
- **Concursos relacionados:** TJ/SP — Juiz de Direito, TJ/RJ — Juiz de Direito 2024, PGM Campinas/SP, demais certames VUNESP da base
- **Periodicidade sugerida:** semanal
- **Verificação:** resultado de busca no domínio oficial vunesp.com.br — 2026-07-31
- **Evidência:** Portal oficial da Vunesp, com filtros por Próximos / Inscrições abertas / Em andamento / Encerrados.
- **Observações:** A estrutura de filtros por situação facilita a distinção entre concursos realizados e futuros.

#### FONTE-BANCA-CESGRANRIO — Fundação Cesgranrio
- **URL:** https://www.cesgranrio.org.br/concursos/
- **Tipo de informação:** edital, cronograma, gabarito, resultado
- **Concursos relacionados:** PETROBRAS, CEF, BNDES, demais certames CESGRANRIO da base
- **Periodicidade sugerida:** mensal
- **Verificação:** resultado de busca no domínio oficial cesgranrio.org.br — 2026-07-31
- **Evidência:** Página oficial de concursos da Fundação Cesgranrio.
- **Observações:** Concursos históricos ficam em https://www.cesgranrio.org.br/concursos/principal.aspx

#### FONTE-BANCA-FUNDATEC — Fundatec
- **URL:** https://www.fundatec.org.br/portal/concursos/
- **Tipo de informação:** edital, cronograma, gabarito, resultado
- **Concursos relacionados:** DPE/SC 2024, demais certames FUNDATEC da base
- **Periodicidade sugerida:** mensal
- **Verificação:** resultado de busca no domínio oficial fundatec.org.br — 2026-07-31
- **Evidência:** Portal oficial de concursos da Fundatec.

#### FONTE-ENFAM-001 — ENFAM — Escola Nacional de Formação e Aperfeiçoamento de Magistrados
- **URL:** https://www.enfam.jus.br/enam/normativos/
- **Tipo de informação:** edital, comunicado, resultado, normativos
- **Concursos relacionados:** ENAM 2024.1, ENAM 2024.2, ENAM 2025.1, ENAM 2026.1, ENAM 2026.2
- **Periodicidade sugerida:** semanal
- **Verificação:** resultado de busca no domínio oficial enfam.jus.br — 2026-07-31
- **Evidência:** Página oficial de editais e normativos do ENAM, mantida pela ENFAM.
- **Observações:** A ENFAM é a instituidora do exame; a FGV é a executora. Ambas publicam os mesmos atos, e os resultados também saem no DOU.

#### FONTE-ENAM-FGV-5 — FGV Conhecimento (executora) / ENFAM (instituidora)
- **URL:** https://conhecimento.fgv.br/exames/enam/5exame
- **Tipo de informação:** edital, cronograma, gabarito, resultado, cartao de respostas
- **Concursos relacionados:** ENAM 2026.1 (5º Exame)
- **Periodicidade sugerida:** semanal
- **Verificação:** resultado de busca no domínio oficial conhecimento.fgv.br, corroborado pelo edital — 2026-07-31
- **Evidência:** Sítio eletrônico indicado no item 1.1.1 do Edital de Abertura n. 01/2026 como canal oficial de divulgação.

#### FONTE-ENAM-EDITAL-2026-1 — ENFAM / FGV
- **URL:** https://conhecimento.fgv.br/sites/default/files/concursos/edital-enam-2026_1.v2.1-1_0.pdf
- **Tipo de informação:** edital de abertura, cronograma, conteudo programatico, estrutura da prova
- **Concursos relacionados:** ENAM 2026.1 (5º Exame)
- **Periodicidade sugerida:** pontual
- **Verificação:** acesso direto ao PDF e leitura integral em 31/07/2026 — 2026-07-31
- **Evidência:** Edital de Abertura n. 01/2026, assinado em 02/03/2026 pelo Presidente da Comissão de Exame. Item 8.1 fixa a prova para 07/06/2026 e o item 8.5 fixa 80 questões objetivas.
- **Observações:** É a evidência oficial que sustenta a data confirmada do ENAM 2026.1 e confirma a estrutura de 80 questões — exatamente o volume registrado na base do Ênfase para ENAM/2026.

#### FONTE-ENAM-RESULT-2026-1 — ENFAM
- **URL:** https://hdl.handle.net/20.500.14782/593
- **Tipo de informação:** relacao de habilitados, resultado da prova objetiva
- **Concursos relacionados:** ENAM 2026.1 (5º Exame)
- **Periodicidade sugerida:** pontual
- **Verificação:** leitura direta da página oficial de normativos da ENFAM em 03/08/2026 — 2026-07-31
- **Evidência:** Edital de 20 de julho de 2026, listado na página oficial de normativos da ENFAM: torna pública a relação das examinandas habilitadas e dos examinandos habilitados na 5ª Edição do ENAM (2026.1).
- **Observações:** Este ato comprova oficialmente que a prova do ENAM 2026.1 FOI REALIZADA e teve resultado divulgado. Ele NÃO declara, porém, a data em que a prova foi aplicada — por isso a data de 07/06/2026 permanece classificada como 'prevista' (ver FUT-001).

#### FONTE-MPF-001 — Ministério Público Federal / PGR
- **URL:** https://www.mpf.mp.br/o-mpf/concursos
- **Tipo de informação:** edital, regulamento, cronograma, gabarito, resultado
- **Concursos relacionados:** MPF — Procurador da República (30º e 31º concursos)
- **Periodicidade sugerida:** mensal
- **Verificação:** resultado de busca no domínio oficial mpf.mp.br — 2026-07-31
- **Evidência:** Área de concursos do MPF. O Edital PGR/MPF n. 1 do 31º concurso indica, no item 9.4, que as divulgações ocorrem no DOU e em mpf.mp.br/concursos/concursos/procuradores.
- **Observações:** O MPF organiza o certame com banca própria — o que explica o rótulo 'BANCA PRÓPRIA' nos registros de MPF na base do Ênfase.

#### FONTE-AGU-001 — Advocacia-Geral da União
- **URL:** https://www.gov.br/agu/pt-br/concursos
- **Tipo de informação:** edital, comunicado, resultado, orientacoes aos aprovados
- **Concursos relacionados:** AGU — Advogado da União, AGU — Procurador Federal, PGFN — Procurador da Fazenda Nacional
- **Periodicidade sugerida:** mensal
- **Verificação:** resultado de busca no domínio oficial gov.br/agu — 2026-07-31
- **Evidência:** Página oficial 'Concursos e Processos Seletivos' da AGU.
- **Observações:** A AGU divulga o certame, mas a execução recente ficou com o Cebraspe — monitorar as duas fontes em conjunto.

## 6. Concursos recentes e futuros

| ID | Concurso | Órgão | Banca | Status da data | Data confirmada | Data prevista | Realização comprovada |
|---|---|---|---|---|---|---|---|
| FUT-001 | ENAM 2026.1 — 5º Exame Nacional da Magistratura | ENFAM | FGV | `prevista` | — | 2026-06-07 | sim |
| FUT-002 | ENAM 2026.2 — 6º Exame Nacional da Magistratura | ENFAM | FGV | `sem_data` | — | — | não comprovada |
| FUT-003 | PGM Manaus/AM — Procurador do Município de 3ª Classe | PGM Manaus/AM | FCC | `prevista` | — | — | não comprovada |
| FUT-004 | MPF — 31º Concurso para Procurador da República | MPF | BANCA PRÓPRIA (MPF) | `prevista` | — | 2025-06-29 | não comprovada |

### 6.1 Detalhamento

#### FUT-001 — ENAM 2026.1 — 5º Exame Nacional da Magistratura
- **Situação:** prova realizada e relação de habilitados publicada por ato oficial da ENFAM em 20/07/2026; a data exata de aplicação não consta do ato de resultado.
- **Evidência oficial:** Edital de Abertura n. 01/2026 (ENFAM), item 8.1: a prova 'será realizada na data provável de 07 de junho de 2026'. O Edital de 20 de julho de 2026, na página de normativos da ENFAM, torna pública a relação de habilitados na 5ª edição — o que comprova a realização, mas não fixa a data de aplicação.
- **URL:** https://conhecimento.fgv.br/sites/default/files/concursos/edital-enam-2026_1.v2.1-1_0.pdf
- **Evidência da realização:** https://hdl.handle.net/20.500.14782/593
- **Verificado em:** 2026-08-03
- **Observações:** Correção da revisão de 03/08/2026: a versão anterior classificava a data como 'confirmada' apoiada apenas no edital de abertura, que usa a expressão 'data provável'. Isso era incoerente com a própria regra de classificação. Nesta versão a data permanece 'prevista' e a realização do evento é registrada em campo separado, com evidência oficial. Para promover a data a 'confirmada' é preciso um ato oficial que declare a data de aplicação — por exemplo a publicação do resultado no DOU com referência à data da prova. A base do Ênfase contém 80 questões de ENAM/2026, compatíveis com a estrutura de 80 questões fixada no edital.

#### FUT-002 — ENAM 2026.2 — 6º Exame Nacional da Magistratura
- **Situação:** edição seguinte esperada pelo histórico semestral do exame; sem edital localizado em fonte oficial nesta verificação.
- **Evidência oficial:** nenhuma localizada
- **URL:** https://www.enfam.jus.br/enam/normativos/
- **Verificado em:** 2026-07-31
- **Observações:** Circulam em veículos de terceiros previsões de publicação do edital em julho de 2026. Não é fonte oficial e NÃO foi adotada. Monitorar a página de normativos da ENFAM e o DOU.

#### FUT-003 — PGM Manaus/AM — Procurador do Município de 3ª Classe
- **Situação:** inscrições abertas em 31/07/2026 conforme portal da FCC; data da prova não confirmada nesta verificação.
- **Evidência oficial:** Listagem 'Inscrições Abertas' do portal oficial da FCC.
- **URL:** https://www.concursosfcc.com.br/concursoInscricaoAberta.html
- **Verificado em:** 2026-07-31
- **Observações:** O órgão já existe na base (PGM Manaus/AM, 150 questões, prova de 2018). Nova prova gerará material inédito. Confirmar a data no edital.

#### FUT-004 — MPF — 31º Concurso para Procurador da República
- **Situação:** prova objetiva já aplicada; etapas subjetivas e orais posteriores.
- **Evidência oficial:** Notícia oficial da PGR sobre a abertura das inscrições do 31º concurso, informando prova objetiva em 29 de junho.
- **URL:** https://www.mpf.mp.br/o-mpf/unidades/procuradoria-geral-da-republica-pgr/noticias/inscricoes-abertas-para-o-31o-concurso-para-procurador-da-republica
- **Verificado em:** 2026-08-03
- **Observações:** Correção da revisão de 03/08/2026: a notícia oficial da PGR anuncia a prova objetiva para 29 de junho e ressalva expressamente que as datas previstas podem ser alteradas. Não foi localizado ato oficial posterior declarando a realização na data. Por isso a classificação é 'prevista'. A base contém 120 questões de MPF/2025, mas nada nela permite afirmar que pertencem a este certame específico.

## 7. Pendências e como resolvê-las

Este mapa cobre as fontes de maior alcance, não todas as entidades da base. As pendências abaixo estão registradas de forma explícita, com protocolo de resolução, justamente para que ninguém preencha as lacunas por dedução. Elas correspondem aos itens 7 do roadmap em `inventario-banco-questoes.md`.

### PEND-001
**O que falta:** 179 dos 182 órgãos com questões na base ainda não têm fonte oficial verificada e registrada aqui (TJs, MPs, DPEs, PGEs, PGMs, Polícias Civis, TRFs, TRTs e demais).

**Por que ainda não foi feito:** A verificação individual de cada domínio exige uma consulta por entidade; nesta etapa foram verificadas apenas as fontes de maior cobertura. Nenhum domínio foi presumido por padrão de nomenclatura.

**Como resolver:**
1. Para tribunais (TJ, TRF, TRT): partir do diretório oficial do CNJ (FONTE-CNJ-001) e extrair o domínio de cada tribunal.
2. Para Ministérios Públicos estaduais: partir do diretório oficial do CNMP.
3. Para PGEs e Polícias Civis: partir do portal oficial do governo do estado (dominio .gov.br do ente federado).
4. Para PGMs: partir do portal oficial da prefeitura do município.
5. Em cada domínio, localizar a seção de concursos e registrar a URL profunda (não a home), o tipo de informação publicada e a data de verificação.
6. Registrar também o Diário Oficial do respectivo ente (estadual ou municipal), que é a fonte primária dos atos, e não o site institucional.

**Bloqueio conhecido:** cnj.jus.br respondeu com bloqueio anti-bot a acesso automatizado em 31/07/2026; usar navegador.

### PEND-002
**O que falta:** 23 das 30 bancas com questões na base ainda não têm fonte oficial verificada (ESAF, PUCPR, AOCP, FUNCAB, FUMARC, UEPA, FAURGS, FAPEC, UNIVERSA, COPSUEL, NCUFPR, CSUFG, FEPESE, IESES, UFMT, INSTITUTO CIDADES, CONSULPLAN, IBGP, FUNDAÇÃO CEPERJ, FUNDEP, FMP CONCURSOS e demais).

**Por que ainda não foi feito:** Mesma restrição de escopo da PEND-001.

**Como resolver:**
1. Localizar o domínio institucional de cada banca e a sua página de concursos.
2. Para bancas ligadas a universidades (NC-UFPR, CS-UFG, COPS-UEL, UFMT, UEPA, FAURGS), a fonte oficial é a página da universidade.
3. Registrar bancas extintas ou inativas explicitamente — a ESAF, por exemplo, precisa ser confirmada quanto à existência atual antes de virar fonte de monitoramento.

### PEND-003
**O que falta:** A base não permite casar automaticamente um registro interno com um edital externo: falta data da prova, número do edital e URL.

**Por que ainda não foi feito:** Limitação estrutural do banco de questões (ver INC-009 no inventário).

**Como resolver:**
1. Criar os campos data_prova, numero_edital e url_edital no banco de origem.
2. Fazer o retrofit começando pelas provas de 2023 em diante, onde os editais ainda estão disponíveis nos sites das bancas.

## 8. Rotina de monitoramento sugerida

| Frequência | O que consultar | Por quê |
|---|---|---|
| Diária | DOU — leitura do jornal (FONTE-DOU-001), Seções 2 e 3 | É onde o edital nasce; tudo o mais é replicação |
| Semanal | Cebraspe, FGV, FCC, Vunesp, ENFAM | Concentram os certames das trilhas de maior peso na base |
| Mensal | Cesgranrio, Fundatec, MPF, AGU | Volume menor ou ciclo mais longo |
| Semestral | Diretório de tribunais do CNJ | Verificar mudanças de domínio e novos tribunais |
| A cada certame | Edital em PDF no site da banca | É a evidência que sustenta a data e a única via para preencher `concurso_oficial_id` |

Para cada verificação, o agente deve registrar: URL consultada, data e hora, o que mudou desde a última consulta e — quando encontrar um edital — órgão, cargo, banca, número do edital, data da prova e o status da data segundo a seção 4. Quando o certame for concluído, registrar também o ato oficial que comprove a realização, que é o que permite promover a data de `prevista` para `confirmada`.

## 9. Fora do escopo desta etapa

- Construção do agente de monitoramento.
- Automação de coleta e alertas.
- Preenchimento de lacunas com fontes não oficiais.
- Vinculação de agrupamentos técnicos internos a concursos oficiais, que depende dos campos de edital ainda ausentes na base (INC-009).
