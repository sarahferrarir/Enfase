---
title: "17 - Implementação Atual"
version: "2.1"
---

# Implementação Atual

Este arquivo registra valores e estruturas confirmados ou consolidados pela documentação anterior. Ele descreve o estado atual observado ou preservado, não necessariamente a regra universal do Design System.

## Valores Confirmados Pelo Site

- cores;
- fontes;
- container;
- topbar;
- header;
- hero editorial;
- sombra;
- H1;
- H2;
- espaçamento de seção;
- fundo claro;
- fundo escuro institucional;
- divisor dourado;
- animação fade-up;
- transição padrão;
- estrutura semântica de hero;
- estrutura dos cards de carreira;
- breakpoints do carrossel de carreira.

## Valores Consolidados Que Podem Ser Refinados

- escala completa de body;
- escala de card titles;
- altura exata de todos os botões;
- padding de todos os cards;
- hover exato de todos os componentes;
- grids de páginas internas;
- breakpoints globais;
- estados de formulário;
- estrutura de todas as páginas;
- padrões específicos de dashboards e ferramentas.

Quando o código oficial fornecer valor mais preciso, atualizar este arquivo.

## Ativos Documentados

- logo oficial adicionada à documentação em [`assets/logo-enfase.avif`](assets/logo-enfase.avif).

Este registro indica que o ativo está disponível no Design System. Ele não substitui inspeção de variantes oficiais de marca no Figma ou no código quando a tarefa exigir confirmação.

## Classes E Estruturas Existentes

### Hero Editorial

Estrutura semântica preservada:

```html
<section class="hero" aria-labelledby="hero-title">
  <div class="hero__inner">
    <div class="hero__copy">
      <h1 id="hero-title">...</h1>
      <div class="hero__divider" aria-hidden="true"></div>
      <p>...</p>
      <div class="hero__actions" aria-label="Ações principais">
        ...
      </div>
    </div>
  </div>
</section>
```

Layout consolidado:

```css
.hero {
  min-height: 600px;
  color: #fff;
  isolation: isolate;
  position: relative;
  overflow: hidden;
}

.hero__inner {
  z-index: 1;
  width: min(100% - 40px, 1200px);
  min-height: 600px;
  display: flex;
  align-items: center;
  margin: 0 auto;
  padding: 72px 0;
  position: relative;
}
```

Hero não é obrigatório para ferramentas e aplicações. Ver [Application Pages](12-application-pages.md).

### Career Card

Estrutura preservada:

```html
<article class="career-card">
  <a class="career-card__link" href="...">
    <div class="career-card__media" aria-hidden="true">
      <img alt="" ...>
    </div>
    <div class="career-card__body">
      <span class="career-card__icon">...</span>
      <h3 class="career-card__title">...</h3>
      <p class="career-card__description">...</p>
    </div>
  </a>
</article>
```

Responsividade consolidada:

```html
sizes="
  (max-width: 720px) 78vw,
  (max-width: 1024px) 33vw,
  20vw
"
```

Career Card deve ser tratado como composição de produto, não como componente universal. Ver [Componentes](06-components.md).

## Tokens De Estrutura

```css
--topbar-height: 5px;
--header-height: 80px;
--hero-height: 600px;
```

Âncoras:

```css
[id] {
  scroll-margin-top: calc(
    var(--topbar-height) +
    var(--header-height) +
    19px
  );
}
```

Valor aproximado: `104px`.

## Fundos Existentes

Bloco escuro institucional:

```css
background-image:
  radial-gradient(
    circle at 52% 45%,
    rgba(77, 36, 16, 0.42),
    transparent 36%
  ),
  linear-gradient(
    90deg,
    #0d001b 0%,
    #12001f 24%,
    #15011c 50%,
    #100018 76%,
    #09000f 100%
  );
```

Seção clara institucional:

```css
.section--light {
  background:
    linear-gradient(
      rgba(255, 255, 255, 0.86),
      rgba(255, 255, 255, 0.96)
    ),
    url("/images/bg-white.webp") center / cover no-repeat;
}
```

## Pendências

- confirmar pesos de fonte carregados, especialmente PT Serif 700;
- confirmar hover exato de todos os componentes;
- confirmar estados completos de formulários;
- revisar padrões específicos de dashboards e ferramentas;
- atualizar este arquivo sempre que a implementação oficial divergir do consolidado.
