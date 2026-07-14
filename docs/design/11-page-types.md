---
title: "11 - Tipos de Página"
version: "2.1"
---

# Tipos De Página

Templates são orientações, não receitas obrigatórias. Cada tipo deve reutilizar tokens, layout, componentes, conteúdo, acessibilidade e responsividade já definidos.

## Landing Page

Objetivo: apresentar campanha, produto ou oferta específica.

Estrutura típica:

- page header ou hero;
- contexto factual;
- proposta;
- público;
- método;
- conteúdo;
- diferenciais;
- prova social, se verificável;
- investimento;
- FAQ;
- CTA final;
- footer.

Componentes recomendados: Page Header, Button, Card, Accordion, Footer.

Componentes opcionais: Pricing, Timeline, Carousel, Badge.

Normalmente N/A: app shell, sidebar operacional, tabelas densas.

Riscos comuns: identidade paralela, promessas sem fonte, preços desatualizados.

## Página Institucional

Objetivo: apresentar marca, história, método, equipe ou posicionamento.

Estrutura típica:

- page header;
- história;
- proposta;
- método;
- números verificáveis;
- equipe;
- CTA;
- footer.

Normalmente N/A: pricing, filtros operacionais, app shell.

## Página De Curso

Objetivo: apresentar produto educacional específico.

Estrutura típica:

- page header;
- para quem é;
- proposta;
- método;
- conteúdo;
- professores;
- materiais;
- diferenciais;
- resultados verificáveis;
- FAQ;
- investimento;
- CTA;
- footer.

Componentes recomendados: Page Header, ProductCard, Card, Accordion, Button.

Componentes opcionais: Pricing, Timeline, Carousel, Tabs.

Riscos comuns: generalizar conteúdo entre produtos, inventar condição comercial, misturar regras de carreira.

## Blog

Objetivo: listar conteúdo editorial.

Deve priorizar:

- categorias;
- busca;
- cards de artigo;
- metadados;
- paginação;
- leitura limpa;
- SEO.

Normalmente N/A: pricing e CTA de venda central.

## Página De Artigo

Objetivo: leitura longa e indexável.

Deve conter:

- H1 claro;
- autor ou fonte quando aplicável;
- data;
- corpo com largura confortável;
- headings coerentes;
- links relacionados;
- imagens otimizadas;
- compartilhamento quando fizer sentido.

Riscos comuns: largura de texto excessiva, heading por aparência, imagem sem alt.

## Dashboard

Objetivo: acompanhamento, métricas, desempenho ou operação.

Deve priorizar:

- tarefas principais;
- métricas;
- filtros;
- tabelas;
- estados vazios;
- carregamento;
- densidade controlada;
- clareza operacional.

Normalmente N/A:

- hero comercial;
- pricing;
- prova social;
- CTA de venda;
- footer institucional completo.

## Ferramenta

Objetivo: execução de tarefa.

Deve conter:

- cabeçalho funcional;
- estado atual;
- controles principais;
- feedback;
- salvamento ou exportação quando aplicável;
- acessibilidade de formulário;
- responsividade orientada ao uso.

## Planner E Tracker

Objetivo: planejamento, acompanhamento ou progresso.

Componentes recomendados: Progress, Tabs, Table, Empty State, Filter Bar, Button, Toast.

Normalmente N/A: hero comercial, prova social, pricing.

## Portal

Objetivo: ambiente autenticado ou área interna.

Pode usar:

- app shell;
- sidebar;
- topbar compacta;
- breadcrumbs;
- tabs;
- filtros;
- tabelas;
- cards de status.

## Login

Deve conter:

- marca;
- formulário simples;
- labels visíveis;
- erro claro;
- recuperação de acesso;
- termos ou privacidade quando aplicável;
- segurança sem excesso de texto.

## Erro

Deve conter:

- mensagem clara;
- explicação breve;
- ação de retorno;
- contato ou ajuda quando aplicável;
- tom sóbrio.

## Documentação

Deve priorizar:

- navegação lateral ou índice;
- headings estáveis;
- exemplos;
- blocos de código;
- busca quando necessário;
- versão ou contexto;
- leitura longa confortável.

## Exemplos De Decisão

- Se a página vende curso, considerar Página de Curso ou Landing Page e consultar Business Rules.
- Se a tela executa tarefa, usar Ferramenta, Planner, Tracker ou Dashboard.
- Se o usuário já está autenticado, considerar Portal ou app shell.
- Se pricing não faz sentido no contexto, marcar como `N/A`.
