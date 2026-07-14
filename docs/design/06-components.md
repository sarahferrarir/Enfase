---
title: "06 - Componentes"
version: "2.1"
---

# Componentes

## Papel

A biblioteca de componentes define padrões reutilizáveis. Componentes específicos de produto devem ser tratados como variantes, composições ou exemplos, não como fundação universal do sistema.

Estrutura recomendada por componente:

- Objetivo;
- Quando usar;
- Quando evitar;
- Anatomia;
- Variantes;
- Estados;
- Regras visuais;
- Responsividade;
- Acessibilidade;
- Exemplo mínimo;
- Referência de implementação.

## Reuse Policy

Antes de criar componente novo, verificar:

1. já existe componente equivalente?
2. existe variante suficiente?
3. o componente atual pode ser composto?
4. o problema é de conteúdo ou de componente?
5. a nova solução será usada em mais de um lugar?

Somente criar componente novo quando:

- houver responsabilidade própria;
- houver uso recorrente ou potencial real;
- a composição existente não resolver;
- a nova abstração reduzir duplicação;
- a acessibilidade puder ser mantida.

Evitar:

- `HomePinkButton`;
- `NdcjPinkButton`;
- `DefensoriaCardEspecial`;
- componentes nomeados por página quando a responsabilidade é genérica.

Preferir:

- `Button` com variantes;
- `Card` com composição;
- `ProductCard`;
- `MediaCard`;
- `StatusCard`.

## Button

Objetivo: executar ação, iniciar fluxo, enviar formulário ou navegar para destino prioritário.

Quando usar: ações claras e acionáveis.

Quando evitar: navegação textual simples ou conteúdo não interativo.

Anatomia:

- label específico;
- ícone opcional;
- estado visual;
- foco visível;
- loading quando assíncrono.

Variantes:

- primary;
- secondary;
- outline on dark;
- outline on light;
- ghost;
- icon-only;
- destructive, apenas quando necessário.

Estados:

- default;
- hover;
- focus-visible;
- active;
- disabled;
- loading.

Regras visuais:

- primary usa rosa principal;
- hover usa rosa escuro;
- altura confortável;
- texto em Montserrat;
- disabled não depende apenas de cor.

Acessibilidade:

- usar `<button>` para ação e `<a>` para navegação;
- botão com ícone sem texto precisa de `aria-label`;
- loading deve prevenir envio duplicado.

Exemplo mínimo:

```html
<button type="button" class="button button--primary">
  Salvar plano
</button>
```

Referência de implementação: ver [Implementação Atual](17-current-implementation.md).

## Card

Objetivo: agrupar conteúdo relacionado em uma unidade escaneável.

Quando usar: listas, produtos, artigos, métricas, status e blocos de explicação.

Quando evitar: quando o conteúdo precisa ser fluxo contínuo de leitura ou quando criaria card dentro de card.

Anatomia:

- container;
- mídia opcional;
- ícone ou badge opcional;
- título;
- descrição;
- metadados opcionais;
- ação opcional.

Variantes:

- editorial;
- funcional;
- produto;
- mídia;
- status;
- métrica;
- artigo.

Regras visuais:

- fundo branco ou soft;
- borda sutil;
- sombra apenas quando houver elevação real;
- padding generoso;
- título claro;
- descrição específica.

Acessibilidade:

- card inteiro clicável apenas quando representar navegação única;
- foco deve estar no link ou controle principal;
- imagem decorativa usa `alt=""`.

Composições de produto: Career Card, card de curso, card de professor e card de pricing devem reutilizar Card ou ProductCard quando possível.

## Input E Textarea

Objetivo: coletar dados com clareza e baixo atrito.

Anatomia:

- label visível;
- campo;
- placeholder opcional;
- texto de ajuda opcional;
- mensagem de erro ou sucesso;
- estado disabled ou readonly quando aplicável.

Estados:

- default;
- hover;
- focus;
- filled;
- error;
- success;
- disabled;
- readonly;
- loading quando aplicável.

Regras:

- placeholder não substitui label;
- erro não depende apenas de vermelho;
- altura mínima de toque de `44px`;
- mensagens devem ser específicas;
- prevenir envio duplicado.

Acessibilidade:

- associar label ao campo;
- usar `aria-describedby` para ajuda e erro.

## Select E Combobox

Objetivo: escolher entre opções controladas.

Quando usar:

- select nativo para listas simples;
- combobox para busca, listas longas ou necessidade operacional real.

Regras:

- label visível;
- opção atual clara;
- navegação por teclado;
- Escape fecha menu customizado;
- estados de erro e disabled;
- menu não pode ser cortado por containers.

## Accordion

Objetivo: revelar conteúdo secundário sem alongar excessivamente a página.

Quando usar: FAQ, detalhes de seção, ajuda contextual.

Quando evitar: conteúdo essencial que precisa ficar sempre visível.

Anatomia:

- pergunta ou título;
- botão ocupando o cabeçalho inteiro;
- ícone de expansão;
- painel;
- resposta.

Exemplo mínimo:

```html
<button aria-expanded="false" aria-controls="panel-id">
  Pergunta
</button>
```

Regras:

- todo o cabeçalho clicável;
- não depender apenas do ícone;
- animação suave;
- reduced motion respeitado;
- comportamento de item único ou múltiplos itens deve ser consistente.

## Badge

Objetivo: sinalizar categoria, status, recomendação ou metadado curto.

Variantes:

- neutral;
- premium;
- active;
- warning;
- success;
- status.

Regras:

- usar caixa alta com moderação;
- manter contraste;
- dourado reservado a autoridade, premium ou recomendação;
- não transformar badge em decoração repetitiva.

## Modal E Dialog

Objetivo: solicitar decisão ou exibir fluxo temporário sem trocar de página.

Regras:

- usar `role="dialog"` ou elemento semântico equivalente;
- associar título com `aria-labelledby`;
- prender foco dentro do modal;
- fechar com Escape quando seguro;
- retornar foco ao acionador;
- incluir botão de fechar acessível;
- não usar modal para conteúdo longo que deveria ser página.

## Table

Objetivo: comparar dados estruturados.

Regras:

- usar `<table>` para dados tabulares reais;
- cabeçalhos claros;
- alinhamento consistente;
- ordenação e filtros quando necessário;
- estados vazios;
- overflow horizontal controlado em mobile;
- não usar tabela para layout.

## Breadcrumb

Objetivo: mostrar localização e permitir retorno hierárquico.

Regras:

- usar em páginas profundas;
- labels curtos;
- último item representa página atual;
- incluir `aria-current="page"` no item atual;
- não substituir navegação principal.

## Progress

Objetivo: indicar avanço em fluxo, trilha, checklist, planner ou tarefa.

Variantes:

- barra linear;
- steps;
- circular apenas para métrica compacta;
- checklist.

Regras:

- estado atual claro;
- label textual quando necessário;
- não depender apenas de cor;
- valores devem ser reais.

## Tabs

Objetivo: alternar visões relacionadas no mesmo contexto.

Regras:

- usar quando os painéis forem paralelos;
- navegação por teclado com setas quando implementado como tabs ARIA;
- indicar tab ativa;
- não usar tabs para esconder conteúdo essencial de SEO em páginas públicas sem critério.

## Timeline

Objetivo: representar sequência temporal, etapas de curso, cronograma ou processo.

Regras:

- cada etapa precisa de título;
- datas devem ser verificadas;
- status visual deve ter texto;
- mobile deve manter leitura linear.

## Empty State

Objetivo: orientar o usuário quando não houver dados, resultados ou conteúdo.

Anatomia:

- título curto;
- explicação objetiva;
- ação recomendada quando existir;
- ícone discreto opcional.

Evitar tom informal excessivo. Empty state deve ajudar, não decorar.

## Tooltip

Objetivo: explicar controle, abreviação ou metadado auxiliar.

Regras:

- não conter informação essencial;
- funcionar com teclado e hover;
- manter texto curto;
- não usar para mensagens de erro;
- não esconder CTAs dentro de tooltip.

## Header, Navigation E Footer

Header público orienta deslocamento global e expõe ações de alto valor. Ferramentas e áreas internas podem usar navegação compacta, sidebar, app shell ou topbar funcional.

Footer público encerra páginas com contexto institucional, links úteis e informações legais. Ferramentas e áreas internas podem usar footer mínimo ou omitir footer, desde que a navegação operacional continue clara.

Navigation pode aparecer como menu horizontal, sidebar, tabs, breadcrumbs ou app shell. Escolher pela árvore de decisão em [18-decision-tree.md](18-decision-tree.md).

## Page Header

Objetivo: introduzir contexto, proposta principal e ação prioritária quando a página exigir entrada editorial.

Hero é uma variante editorial de Page Header, não uma obrigação.

Usar quando:

- a página precisa de posicionamento editorial;
- existe proposta comercial ou institucional;
- a primeira dobra precisa orientar decisão.

Evitar quando:

- a interface é uma ferramenta;
- o usuário já está em fluxo operacional;
- a tela precisa priorizar dados, filtros ou tarefas.

## Carousel

Objetivo: permitir navegação horizontal quando o conteúdo excede a largura disponível.

Regras:

- viewport com overflow controlado;
- navegação anterior/próximo;
- estado `disabled`;
- labels acessíveis;
- não depender apenas de swipe;
- não usar autoplay;
- preservar conteúdo no DOM;
- suportar teclado;
- usar apenas quando grid responsivo não resolver melhor.

## Alert E Toast

Objetivo: comunicar estado, erro, sucesso ou aviso.

Alert deve ficar no fluxo da página quando a informação precisa permanecer visível. Toast deve ser temporário e não conter informação essencial.

Regras:

- texto objetivo;
- severidade clara;
- não depender apenas de cor;
- ação de correção quando aplicável;
- região anunciável para tecnologias assistivas quando necessário.

## Pagination

Objetivo: navegar entre páginas de resultados.

Regras:

- estado atual claro;
- labels acessíveis;
- links ou botões coerentes com a ação;
- não esconder paginação em mobile sem alternativa.

## Search E Filter Bar

Objetivo: reduzir conjunto de resultados, localizar conteúdo ou operar tabelas.

Regras:

- label ou placeholder claro;
- filtros aplicados visíveis;
- ação para limpar filtros;
- estados vazios úteis;
- debounce quando necessário;
- não remover resultados sem feedback.

## Componentes De Produto

Pricing, Career Card, card de curso e card de professor são composições de produto. Devem referenciar:

- [Tipos de Página](11-page-types.md);
- [Business Rules](13-business-rules.md);
- [Implementação Atual](17-current-implementation.md), quando houver classe ou estrutura existente.
