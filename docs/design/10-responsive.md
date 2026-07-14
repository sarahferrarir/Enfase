---
title: "10 - Responsividade"
version: "2.1"
---

# Responsividade

## Princípio

Mobile não é desktop reduzido. A interface deve reorganizar prioridade, densidade e fluxo.

Revisar:

- header;
- navegação;
- page header ou hero;
- cards;
- grids;
- tabelas;
- formulários;
- CTAs;
- dashboards;
- modais.

## Desktop

Desktop pode usar:

- grids de 3 ou 4 colunas;
- navegação horizontal;
- tabelas completas;
- painéis lado a lado;
- espaço negativo amplo;
- imagens editoriais maiores.

## Tablet

Tablet deve:

- reduzir colunas;
- preservar padding;
- evitar textos espremidos;
- manter controles confortáveis;
- considerar orientação retrato e paisagem.

## Mobile

Mobile deve:

- priorizar leitura linear;
- empilhar CTAs quando necessário;
- usar botões full-width quando fizer sentido;
- evitar altura fixa em hero;
- esconder ou reordenar imagens que competem com a tarefa;
- permitir overflow horizontal controlado em tabelas;
- remover quebras manuais de desktop.

## Cards E Grids

- uma coluna para cards grandes;
- duas colunas apenas com largura suficiente;
- carrossel apenas quando o componente existente exigir;
- preservar padding interno;
- não reduzir tipografia a ponto de perder leitura.

## Tabelas

Em mobile:

- usar scroll horizontal controlado;
- ou transformar linhas em cards quando a comparação não exigir colunas simultâneas;
- manter cabeçalhos ou labels visíveis;
- não cortar conteúdo.

## Quebras Manuais

Quebras como `.desktop-break` devem ser removidas ou ocultadas em mobile. Não depender de `<br>` para layout responsivo.

## Evidência

Não afirmar responsividade visual sem teste real em viewport compatível. Quando não houver teste, declarar como inferência.
