---
title: "15 - Auditoria"
version: "2.1"
---

# Auditoria

Este arquivo orienta auditorias de páginas, componentes, ferramentas e fluxos.

## Escala De Conformidade

Cada requisito avaliado deve receber uma destas classificações:

- Atendido;
- Parcial;
- Não atendido;
- Não aplicável (N/A).

Nem toda regra vale para toda interface. Se uma regra não fizer sentido para aquele tipo de aplicação, marcar como `N/A`, nunca como `Não atendido`.

Exemplos:

- pricing em dashboard interno: `N/A`;
- hero comercial em planner: `N/A`;
- footer institucional completo em app autenticado: `N/A`;
- navegação por teclado em qualquer interface interativa: deve ser avaliada.

## Severidade

Cada problema encontrado deve receber severidade:

- Crítico: impede uso, viola regra legal/comercial relevante, quebra fluxo principal ou cria risco grave de acessibilidade;
- Alto: prejudica conversão, compreensão, navegação, responsividade ou acessibilidade importante;
- Médio: desalinhamento perceptível com o Design System ou problema que afeta parte dos usuários;
- Baixo: refinamento visual, inconsistência pequena ou melhoria de manutenção;
- N/A: não há problema aplicável.

## Evidência Obrigatória

Cada achado deve incluir, quando disponível:

- arquivo;
- linha ou seletor;
- screenshot ou viewport;
- regra do Design System relacionada;
- recomendação objetiva.

Sem evidência, classificar como inferência e explicar a limitação.

## Categorias

Avaliar, quando aplicável:

- marca e linguagem visual;
- tokens;
- tipografia;
- layout;
- componentes;
- conteúdo;
- acessibilidade;
- responsividade;
- performance visual;
- regras de negócio;
- implementação.

## Formato Recomendado

| Requisito | Status | Severidade | Evidência | Recomendação |
| --- | --- | --- | --- | --- |
| Usa tokens oficiais | Atendido | N/A | Cores derivam de tokens | Manter |
| Pricing presente em ferramenta interna | N/A | N/A | Tela não é comercial | Nenhuma |
| Botão sem focus visível | Não atendido | Alto | Seletor `.button-primary` sem `:focus-visible` | Adicionar estado de foco |

## Score

O resumo final deve incluir:

- Visual;
- Código;
- Acessibilidade;
- Responsividade;
- Design System;
- Score Geral.

Regras:

- itens `N/A` não entram no cálculo;
- problemas críticos devem limitar o score máximo;
- não gerar precisão falsa sem evidência;
- score deve ser explicado;
- separar validação estática de validação em navegador;
- não afirmar responsividade visual sem teste real;
- não afirmar fonte carregada apenas porque `font-family` foi declarado.

Referência:

- 90-100: excelente aderência;
- 75-89: bom, com ajustes;
- 60-74: parcial, requer correções;
- abaixo de 60: desalinhado ou arriscado.

## Checklist Base

Conteúdo:

- o H1 descreve claramente a página?
- produto, carreira e contexto estão corretos?
- preços e condições foram confirmados quando aparecem?
- links foram confirmados?
- não existem promessas indevidas?
- CTAs são específicos?

Visual:

- cores usam tokens oficiais?
- PT Serif e Montserrat estão nos papéis corretos?
- conteúdo usa container oficial?
- espaçamento segue o sistema?
- imagens seguem a direção de arte?
- dourado não está excessivo?
- rosa está reservado a ações e destaque?

Componentes:

- componentes existentes foram reutilizados?
- hover existe?
- focus-visible existe?
- disabled existe?
- loading existe quando necessário?
- cards clicáveis têm foco adequado?
- accordions usam semântica correta?
- carrossel, se aplicável, tem controles acessíveis?

Responsividade:

- desktop revisado?
- tablet revisado?
- mobile revisado?
- botões não quebram?
- headings não transbordam?
- imagens mantêm foco?
- tabelas não cortam conteúdo?
- menu mobile funciona quando existe?

Acessibilidade:

- há um único H1?
- hierarquia de headings está correta?
- navegação por teclado funciona?
- foco visível?
- contraste AA?
- reduced motion?
- alt texts corretos?
- touch targets adequados?

Regressão:

- componentes compartilhados foram verificados?
- nenhum link oficial foi removido?
- Portal de Entrada e Portal da Pós foram preservados quando aplicáveis?
- não houve alteração acidental em outra página?
