---
title: "09 - Acessibilidade"
version: "2.1"
---

# Acessibilidade

## Semântica

- um H1 por página;
- hierarquia correta;
- `<nav>` para navegação;
- `<main>` para conteúdo;
- `<section>` com heading;
- `<article>` para cards independentes;
- `<button>` para ações;
- `<a>` para navegação;
- não usar `<div>` clicável.

## Teclado

Suportar:

- Tab;
- Shift+Tab;
- Enter;
- Espaço;
- Escape;
- setas quando o padrão do componente exigir.

## Focus Visible

Fundo claro:

```css
outline: 3px solid #3a0a6e;
outline-offset: 3px;
```

Fundo escuro:

```css
outline: 3px solid #ffffff;
outline-offset: 3px;
```

## ARIA

Usar ARIA para complementar semântica, não para corrigir markup inadequado.

Regras:

- `aria-label` em botões apenas com ícone;
- `aria-expanded` em disclosure, menu e accordion;
- `aria-controls` quando houver painel controlado;
- `aria-current="page"` em item atual;
- `aria-describedby` para ajuda e erro em campos;
- não usar roles desnecessárias quando HTML nativo resolve.

## Contraste

Atender WCAG AA:

- texto normal: 4.5:1;
- texto grande: 3:1;
- componentes gráficos essenciais: 3:1.

## Touch Target

Área mínima aproximada: `44px` por `44px`.

## Skip Link

Manter "Pular para o conteúdo" como primeiro link focável em páginas com navegação global.

## Imagens

Imagem decorativa:

```html
<div aria-hidden="true">
  <img alt="">
</div>
```

Imagem informativa deve ter alt descritivo e objetivo.

## Movimento

Respeitar `prefers-reduced-motion`. Nenhuma informação pode depender exclusivamente de animação.

## Auditoria

Não afirmar acessibilidade sem evidência. Para auditoria formal, usar [15-audit.md](15-audit.md).
