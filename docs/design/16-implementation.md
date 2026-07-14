---
title: "16 - Implementação"
version: "2.1"
---

# Implementação

Este arquivo define práticas de implementação do Design System. O estado atual confirmado do site/código fica em [17-current-implementation.md](17-current-implementation.md).

## Tokens

Reutilizar tokens globais. Não hardcodar a mesma cor, espaço, sombra ou radius em vários componentes.

## Componentes

Criar variantes controladas.

Bom:

- `Button`;
- `ButtonPrimary`;
- `ButtonOutline`;
- `SectionHeading`;
- `Card`;
- `ProductCard`;
- `MediaCard`;
- `StatusCard`;
- `Accordion`;
- `PageHeader`;
- `Tabs`;
- `Table`.

Ruim:

- `HomePinkButton`;
- `DefensoriaPinkButton`;
- `NdcjPinkButton`;
- `OtherPinkButton`;
- `DefensoriaCardEspecial`.

## Dados

Centralizar quando possível:

- links;
- cursos;
- FAQs;
- preços;
- informações institucionais;
- professores;
- CTAs;
- carreiras;
- contatos.

Não alterar dados de negócio sem confirmação. Ver [Business Rules](13-business-rules.md).

## Componentes Compartilhados

Antes de alterar:

- verificar todas as páginas impactadas;
- revisar responsividade;
- revisar estados;
- revisar acessibilidade;
- não corrigir uma página quebrando outras.

## Figma E Ativos

O Figma deve ser usado para:

- fotos de professores;
- heroes;
- ícones;
- templates sociais;
- componentes ainda não formalizados no código;
- nomenclatura visual.

O agente deve:

1. procurar o ativo oficial;
2. evitar recriar algo já existente;
3. manter nomes consistentes;
4. exportar no formato correto;
5. preservar proporção;
6. documentar novo ativo.

## Imagens E Performance

- definir dimensões;
- evitar CLS;
- lazy load abaixo da dobra;
- usar `sizes`;
- otimizar formato;
- priorizar imagem crítica;
- usar `object-fit: cover`;
- ajustar `object-position`.

## Redes Sociais

O Figma possui referências de:

- edital + demanda;
- prova/questão;
- resposta;
- diagnóstico;
- plano de estudo;
- execução guiada;
- resposta rápida.

Esses materiais ajudam a manter consistência de paleta, tipografia, hierarquia, ícones, CTA e linguagem de dados.

Não copiar layouts de Instagram diretamente para a web. Adaptar a lógica, não a proporção.
