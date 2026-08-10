# Roadmap de Criação dos Templates do Instagram do Curso Ênfase

## Introdução

Este roadmap define a ordem mais eficiente para implementar do zero os nove templates aprovados. Seu objetivo é transformar a arquitetura consolidada em uma sequência de trabalho que maximize cobertura progressiva, reaproveitamento de componentes e estabilidade do sistema.

Prioridade editorial e ordem de implementação são critérios diferentes. A prioridade editorial indica a importância do template para a comunicação; a ordem de implementação considera também dependências, complexidade, parametrização e capacidade de uma estrutura reduzir o esforço das seguintes. Por isso, templates com a mesma prioridade podem aparecer em fases distintas.

O roadmap deve orientar planejamento, construção, validação e liberação progressiva. Ele não altera famílias, códigos, prioridades ou especificações do catálogo oficial.

# Princípios adotados

- **Maior cobertura editorial:** Estruturas que atendem mais ocorrências e famílias entram cedo quando também estabelecem fundamentos reutilizáveis.
- **Maior potencial de reutilização:** Templates avaliados como “Muito alto” formam a base antes das estruturas mais específicas.
- **Dependência entre estruturas:** Sistemas unitários e componentes-base precedem sequências compostas, painéis e variações que podem reutilizá-los.
- **Impacto operacional:** Conteúdos comerciais, educacionais, em vídeo, eventos, notícias e catálogos foram ordenados para reduzir rapidamente a produção manual recorrente.
- **Parametrização:** Templates com muitos cenários exigem convenções de campos e estados antes que estruturas dependentes sejam implementadas.
- **Frequência observada:** A recorrência define o ganho prático de antecipar uma implementação, sem substituir os demais critérios.
- **Complexidade de implementação:** Estruturas complexas entram cedo quando funcionam como fundação; entram depois quando dependem de componentes já estabilizados.
- **Facilidade de manutenção:** Componentes compartilhados devem ser definidos uma vez e reaproveitados, evitando implementações paralelas.

# Roadmap de implementação

## Fase 1 — Fundação multiformato

### Objetivo da fase

Estabelecer os três sistemas-base de maior abrangência: comunicação comercial modular, vídeo vertical e conteúdo educacional. Ao final, a equipe terá convenções para campos, componentes, sequências, CTAs, áreas seguras e adaptação entre Feed, Carrossel, Reel e Story.

### Templates incluídos

1. T01 — Oferta Modular de Produto.
2. T04 — Vídeo Vertical de Especialista ou Trajetória.
3. T08 — Conteúdo Educacional Modular.

### Justificativa

T01 possui a maior cobertura documentada, com 57 ocorrências, e define a lógica modular de abertura, desenvolvimento, síntese e conversão. T04 estabelece a infraestrutura específica de Reel — vídeo, legendas, identificação, capas e encerramento — necessária para versões faladas de várias famílias. T08 usa a base estática e sequencial de T01 e a configuração de vídeo de T04 para cobrir 27 ocorrências educacionais e de relacionamento.

### Benefícios obtidos ao concluir esta fase

- Cobertura imediata das principais demandas comerciais, educacionais e de vídeo.
- Convenções comuns de parametrização e hierarquia.
- Componentes de CTA, autoria, abertura, desenvolvimento e fechamento reutilizáveis.
- Base consistente para os quatro formatos suportados.
- Redução do risco de criar sistemas paralelos para Reel e conteúdo estático.

### Dependências

- T01 não depende de outro template; inaugura o sistema modular.
- T04 depende apenas das convenções gerais de marca e campos estabelecidas na fundação, não de outro template funcional.
- T08 reutiliza convenções estáticas e sequenciais de T01 e a estrutura de Reel de T04.

### Riscos de não implementá-la primeiro

- Duplicação de componentes de CTA, títulos, identificação e sequências em templates posteriores.
- Criação de Reels sem regras comuns de legenda, área segura e identificação.
- Painéis, catálogos e eventos desenvolvidos antes da estabilização dos componentes-base.
- Maior custo de refatoração quando os templates de maior cobertura forem finalmente implementados.

## Fase 2 — Operação editorial recorrente

### Objetivo da fase

Transformar em sistemas reutilizáveis três operações frequentes: divulgação temporal, atualização de concursos e distribuição de acervos. A fase amplia a cobertura para rotinas com dados, agenda, especialistas, links e conjuntos repetitivos de itens.

### Templates incluídos

4. T03 — Chamada de Evento ou Conteúdo com Data.
5. T06 — Boletim de Status de Concurso.
6. T09 — Catálogo de Recursos e Acervo.

### Justificativa

T03 reutiliza CTAs, identificação de especialistas e suporte a Reel da fase anterior. T06 cria componentes estruturados para status, datas, fontes e dados oficiais, que serão necessários no painel multitemático da fase seguinte. T09 aproveita a lógica de sequência do T01 e os padrões de destino externo e identificação de conteúdo do T03 para organizar 26 ocorrências de acervos e materiais.

### Benefícios obtidos ao concluir esta fase

- Padronização de eventos, entrevistas, lembretes e captação.
- Redução do trabalho manual em notícias de concursos e mudanças de status.
- Estrutura consistente para catálogos extensos em Story e Carrossel.
- Componentes reutilizáveis de data, status, especialista, link e item de acervo.
- Cobertura das rotinas editoriais mais dependentes de atualização frequente.

### Dependências

- T03 reutiliza componentes e regras de T01 e T04.
- T06 reutiliza convenções modulares e de hierarquia estabelecidas em T01.
- T09 reutiliza abertura, repetição e encerramento de sequências do T01 e padrões de CTA externo do T03.

### Riscos de não implementá-la depois da fundação

- Eventos e catálogos podem recriar componentes já previstos no sistema comercial.
- Boletins podem definir campos de dados incompatíveis com os painéis posteriores.
- Links, especialistas, datas e estados temporais podem receber tratamentos diferentes entre produtos, eventos e acervos.
- A implementação isolada do catálogo pode produzir uma segunda lógica de sequência e navegação.

## Fase 3 — Estruturas compostas e evidência

### Objetivo da fase

Implementar estruturas que dependem de dados já organizados: painéis com múltiplos itens e prova social quantificada. A fase consolida componentes de status, números, fontes, recortes e repetição modular.

### Templates incluídos

7. T07 — Painel Editorial Multitópico.
8. T05 — Prova Social Quantificada.

### Justificativa

T07 deve ser implementado após T06 porque transforma componentes de um boletim unitário em uma edição com vários itens, categorias e estados. Também pode reutilizar a lógica educacional de T08 quando um item exige síntese explicativa. T05 vem depois da estabilização dos campos quantitativos e de contexto do T06, permitindo tratar números, unidades, períodos e fontes com maior consistência.

### Benefícios obtidos ao concluir esta fase

- Reutilização dos componentes de status e dados em estruturas mais densas.
- Consistência entre notícia unitária, panorama e resultado institucional.
- Menor esforço para criar edições recorrentes com vários itens.
- Melhor manutenção de unidades, períodos, fontes e notas.
- Cobertura das famílias de panorama, atualidades e resultados quantificados.

### Dependências

- T07 depende dos componentes de status e dados do T06 e reutiliza convenções editoriais do T08.
- T05 reutiliza regras de dados, unidade, período e fonte estabilizadas no T06, além da lógica sequencial do T01.

### Riscos de implementá-la antes das fases anteriores

- Criação de um painel monolítico sem componentes reutilizáveis de item.
- Divergência entre o boletim de um concurso e o mesmo conteúdo dentro de um panorama.
- Tratamento inconsistente de números entre prova social, notícias e ofertas.
- Necessidade de refazer hierarquias, estados e validações depois da implementação de T06.

## Fase 4 — Fechamento institucional

### Objetivo da fase

Completar a cobertura com a estrutura de baixa densidade destinada a teaser, posicionamento e anúncio institucional, reutilizando o sistema já consolidado sem antecipar componentes isolados.

### Templates incluídos

9. T02 — Anúncio Institucional de Alto Impacto.

### Justificativa

T02 tem prioridade editorial Importante, 9 ocorrências e potencial de reutilização Alto. Sua implementação é mais eficiente após T01 e T04, pois pode reutilizar estruturas de peça unitária, identificação, CTA e vídeo curto. Como atende mensagens de baixa densidade e inclui uma família isolada, não deve definir os fundamentos do sistema.

### Benefícios obtidos ao concluir esta fase

- Cobertura integral das 18 famílias.
- Padronização de teaser, save the date, posicionamento e nova coordenação.
- Reutilização dos componentes já validados, sem ampliar a arquitetura.
- Encerramento do sistema com menor risco de criar exceções institucionais.

### Dependências

- T02 reutiliza a estrutura de peça unitária e CTA do T01.
- A configuração em Reel reutiliza convenções de vídeo e áreas seguras do T04.
- Apresentações de pessoas reutilizam padrões de identificação já presentes em T03 e T04.

### Riscos de implementá-la antes

- Uma estrutura de baixa densidade pode ser tomada indevidamente como base para ofertas, eventos ou conteúdo educacional mais complexo.
- Componentes de pessoa, data e CTA podem ser duplicados antes de seus usos principais estarem estabilizados.
- O caso isolado de nova coordenação pode influenciar excessivamente as decisões gerais do sistema.

# Ordem consolidada

| Ordem | Template | Motivo da posição | Dependências | Esforço |
|---:|---|---|---|---|
| 1 | T01 — Oferta Modular de Produto | Maior cobertura; estabelece modularidade, sequências, CTAs e adaptação multiformato. | Nenhuma dependência de outro template. | Alto |
| 2 | T04 — Vídeo Vertical de Especialista ou Trajetória | Cria a infraestrutura de Reel usada por conteúdo, eventos e posicionamento. | Convenções gerais iniciadas em T01. | Alto |
| 3 | T08 — Conteúdo Educacional Modular | Amplia cobertura usando a base estática do T01 e a base de vídeo do T04. | T01 para estruturas modulares; T04 para Reel. | Alto |
| 4 | T03 — Chamada de Evento ou Conteúdo com Data | Reutiliza pessoa, CTA, vídeo e campos temporais para uma operação recorrente. | T01 e T04. | Médio |
| 5 | T06 — Boletim de Status de Concurso | Estrutura dados e estados que serão reutilizados em painéis e resultados. | Convenções modulares de T01. | Médio |
| 6 | T09 — Catálogo de Recursos e Acervo | Consolida sequências repetitivas e destinos externos após os padrões-base. | T01 para sequência; T03 para CTA e identificação. | Alto |
| 7 | T07 — Painel Editorial Multitópico | Compõe vários itens a partir dos estados e campos definidos no boletim. | T06 e convenções de T08. | Alto |
| 8 | T05 — Prova Social Quantificada | Especializa o tratamento de números após estabilização de dados e fontes. | T06 para dados; T01 para sequência. | Médio |
| 9 | T02 — Anúncio Institucional de Alto Impacto | Fecha a cobertura com baixa densidade, reutilizando componentes já maduros. | T01, T04 e padrões de identificação de T03. | Médio |

# Critérios para conclusão de cada fase

## Fase 1 — Fundação multiformato

- T01, T04 e T08 implementados nos formatos previstos no catálogo.
- Campos obrigatórios e variáveis parametrizados.
- Componentes compartilhados de título, autoria, CTA, sequência e identificação documentados.
- Regras de Reel, legendas e áreas seguras validadas.
- Variações comerciais e educacionais essenciais testadas com exemplos documentados.
- Documentação de uso e manutenção concluída.

## Fase 2 — Operação editorial recorrente

- T03, T06 e T09 implementados em todos os formatos previstos.
- Estados de evento, lembrete e status de concurso parametrizados.
- Componentes repetíveis de catálogo, abertura, item e encerramento concluídos.
- Campos de data, link, especialista, fonte e pendência validados.
- Variações com um item e com sequências extensas testadas.
- Documentação integrada aos componentes da Fase 1.

## Fase 3 — Estruturas compostas e evidência

- T07 e T05 implementados nos formatos previstos.
- Componentes de item do T06 reutilizados no T07 sem duplicação.
- Unidades, períodos, fontes, notas e estados quantitativos parametrizados.
- Painéis com diferentes quantidades de itens validados.
- Indicadores isolados e sequências de resultados testados.
- Documentação de governança de dados concluída.

## Fase 4 — Fechamento institucional

- T02 implementado em Feed, Reel, Carrossel e Story.
- Configurações de teaser, posicionamento e nova coordenação concluídas.
- Componentes compartilhados reutilizados sem criar variantes paralelas.
- Mensagens de baixa densidade testadas com os exemplos documentados.
- Cobertura final das 18 famílias verificada.
- Documentação geral do sistema atualizada e validada.

# Ganhos esperados por fase

## Fase 1

Entrega o núcleo de maior cobertura e estabelece padrões para os quatro formatos. O ganho principal é evitar retrabalho: oferta, conteúdo educacional e vídeo passam a compartilhar convenções antes que novos sistemas sejam adicionados.

## Fase 2

Transforma operações recorrentes em fluxos parametrizados. Eventos, notícias e acervos deixam de depender de soluções pontuais e passam a reutilizar componentes da fundação, aumentando velocidade e previsibilidade de manutenção.

## Fase 3

Amplia o sistema para estruturas densas e orientadas por dados. A reutilização do boletim dentro do painel e das regras quantitativas dentro da prova social reduz inconsistências e facilita atualizações.

## Fase 4

Completa a cobertura institucional com baixo custo incremental. Como os componentes já estão maduros, teaser, posicionamento e apresentação de pessoa podem ser implementados como configurações controladas, sem criar exceções.

# Riscos de implementação fora da ordem

- **T07 antes de T06:** O painel pode criar componentes próprios de status, órgão, fonte e data, duplicando a estrutura do boletim.
- **T08 antes de T04:** A versão Reel do conteúdo educacional pode adotar regras diferentes de legenda, identificação e área segura.
- **T09 antes de T01 e T03:** O catálogo pode criar uma segunda lógica de sequência, CTA externo e identificação de especialista.
- **T05 antes de T06:** Números, unidades, períodos e fontes podem ser modelados sem coerência com os demais conteúdos orientados por dados.
- **T03 antes de T01 e T04:** Chamadas de evento podem duplicar componentes de CTA, pessoa e vídeo.
- **T02 como fundação:** Uma estrutura curta e pouco densa pode impor limitações inadequadas aos templates comerciais e educacionais.
- **Implementações paralelas sem componentes compartilhados:** A equipe pode criar variações incompatíveis de títulos, CTAs, datas, autoria, cards e encerramentos, elevando manutenção e refação.

# Conclusão

A ordem recomendada começa pelos sistemas de maior cobertura e capacidade de fundamentar os demais: T01, T04 e T08. Em seguida, transforma eventos, boletins e catálogos em operações recorrentes; depois implementa estruturas compostas e quantitativas; por fim, fecha a cobertura com anúncios institucionais de baixa densidade.

Essa sequência reduz esforço porque cada fase reutiliza decisões já validadas. Também maximiza a reutilização, evita componentes paralelos e permite que estruturas complexas sejam construídas sobre unidades mais simples. O resultado é um sistema progressivamente utilizável, com cobertura crescente e base preparada para futuras expansões sem alteração da arquitetura aprovada.
