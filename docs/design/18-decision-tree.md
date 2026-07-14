---
title: "18 - Árvore de Decisão"
version: "2.1"
---

# Árvore De Decisão

Use esta árvore para escolher estrutura, componentes aplicáveis e regras N/A antes de criar ou auditar uma interface.

## Primeira Decisão

```text
É uma interface pública?
├── Sim
│   ├── É comercial?
│   │   ├── Sim -> Landing Page / Página de Curso
│   │   └── Não -> Institucional / Blog / Artigo / Documentação
│   └── Precisa de navegação global?
│       ├── Sim -> Header e Footer públicos
│       └── Não -> Estrutura reduzida
└── Não
    ├── É autenticada?
    │   ├── Sim -> Portal / Dashboard / App Shell
    │   └── Não -> Ferramenta standalone
    ├── É operacional?
    │   ├── Sim -> Cabeçalho funcional, controles, estados
    │   └── Não -> Page Header simples
    └── Hero comercial?
        └── N/A
```

## Header

Usar header público quando:

- interface é pública;
- navegação institucional ou comercial é necessária;
- usuário precisa acessar páginas principais.

Usar topbar funcional, app shell ou sidebar quando:

- interface é autenticada;
- fluxo é operacional;
- usuário alterna entre áreas internas.

Marcar header comercial como `N/A` quando a ferramenta não precisa dele.

## Footer

Usar footer público quando:

- página é institucional, comercial, blog ou artigo;
- links legais e institucionais são relevantes.

Footer completo pode ser `N/A` em:

- dashboards;
- planners;
- trackers;
- portais autenticados;
- ferramentas standalone.

## Hero E Page Header

Usar hero editorial quando:

- página precisa de posicionamento forte;
- existe proposta institucional ou comercial;
- a primeira dobra precisa orientar decisão.

Usar page header simples quando:

- página é interna;
- contexto é mais importante que venda;
- há ação principal clara, mas sem narrativa comercial.

Marcar hero comercial como `N/A` quando:

- tela é operacional;
- usuário já está em fluxo;
- dados, filtros ou tarefa principal devem aparecer primeiro.

## Pricing

Usar pricing quando:

- há oferta comercial;
- preço e condições foram confirmados;
- comparação de planos é necessária.

Marcar pricing como `N/A` quando:

- dashboard;
- ferramenta;
- portal interno;
- documentação;
- artigo editorial sem oferta.

## Prova Social

Usar apenas quando houver dados, depoimentos ou resultados verificáveis.

Marcar como `N/A` em:

- ferramentas internas;
- dashboards;
- fluxos administrativos;
- documentação técnica.

## CTA Comercial

Usar CTA comercial quando a página busca conversão.

Usar ação funcional quando a interface executa tarefa:

- salvar;
- filtrar;
- exportar;
- abrir relatório;
- montar plano.

## Sidebar, Breadcrumbs E App Shell

Usar sidebar ou app shell quando:

- ambiente é autenticado;
- há múltiplas áreas internas;
- o usuário alterna tarefas com frequência.

Usar breadcrumbs quando:

- página é profunda;
- há hierarquia clara;
- retorno contextual é útil.

## Filtros, Busca E Tabelas

Usar quando:

- conteúdo é grande;
- usuário compara dados;
- operação exige recorte por status, categoria, período ou responsável.

Evitar quando:

- página é principalmente editorial;
- lista é curta;
- filtro adiciona complexidade sem ganho.

## Densidade

Usar densidade maior em:

- dashboards;
- trackers;
- sistemas administrativos;
- tabelas;
- portais internos.

Usar respiro maior em:

- páginas institucionais;
- landing pages;
- páginas de curso;
- artigos;
- documentação de leitura longa.

## Checklist De Decisão

Antes de começar:

- qual é o tipo de interface?
- é pública ou interna?
- é comercial, editorial ou operacional?
- qual ação principal?
- quais componentes são obrigatórios?
- quais componentes são opcionais?
- quais regras são `N/A`?
- quais dados precisam de confirmação?
