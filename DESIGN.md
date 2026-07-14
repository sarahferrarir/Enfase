---
version: "1.0"
status: "active"
name: "Ênfase — Autoridade Jurídica Contemporânea"
website: "https://cursoenfase.com.br/"
purpose:
  - "Orientar agentes na criação de novas páginas."
  - "Orientar agentes na correção de páginas existentes."
  - "Reduzir contexto repetido em prompts."
  - "Padronizar respostas e implementações de agentes."
  - "Documentar identidade visual, componentes, interações e regras de negócio."
source_priority:
  - "Código e tokens oficiais do site."
  - "Componentes e estilos oficiais do Figma."
  - "Este DESIGN.md."
  - "Padrões visuais recorrentes do site."
  - "Inferências do agente, somente quando não houver fonte melhor."
colors:
  background: "#FFFFFF"
  foreground: "#160023"
  primary: "#FF2759"
  primary-hover: "#D6224C"
  primary-deep: "#370F18"
  primary-foreground: "#FFFFFF"
  purple: "#200140"
  purple-high: "#3A0A6E"
  purple-dark: "#170030"
  ink: "#160023"
  muted: "#675F78"
  gold: "#D6B56D"
  line: "#20014024"
  surface: "#FFFFFF"
  surface-soft: "#F5F2F8"
  surface-soft-2: "#EEE8F4"
  hero-start: "#0D001B"
  hero-stop-1: "#12001F"
  hero-stop-2: "#15011C"
  hero-stop-3: "#100018"
  hero-end: "#09000F"
  hero-warm-glow: "rgba(77, 36, 16, 0.42)"
  focus-light: "#FFFFFF"
  focus-dark: "#3A0A6E"
typography:
  brand:
    fontFamily: "Montserrat, Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
  headline:
    fontFamily: "PT Serif, Georgia, 'Times New Roman', serif"
  hero-title:
    fontFamily: "PT Serif, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(42px, 6vw, 60px)"
    fontWeight: "700"
    lineHeight: "0.98"
    letterSpacing: "0"
  section-title:
    fontFamily: "PT Serif, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(34px, 4vw, 54px)"
    fontWeight: "700"
    lineHeight: "1.05"
    letterSpacing: "0"
  page-title:
    fontFamily: "PT Serif, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(38px, 5vw, 58px)"
    fontWeight: "700"
    lineHeight: "1.02"
    letterSpacing: "0"
  editorial-card-title:
    fontFamily: "PT Serif, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(28px, 3vw, 42px)"
    fontWeight: "700"
    lineHeight: "1.08"
  ui-card-title:
    fontFamily: "Montserrat, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: "700"
    lineHeight: "1.25"
  body-lg:
    fontFamily: "Montserrat, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(18px, 1.6vw, 21px)"
    fontWeight: "400"
    lineHeight: "1.55"
  body-md:
    fontFamily: "Montserrat, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: "400"
    lineHeight: "1.55"
  body-sm:
    fontFamily: "Montserrat, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: "400"
    lineHeight: "1.5"
  label:
    fontFamily: "Montserrat, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: "700"
    lineHeight: "1.2"
  overline:
    fontFamily: "Montserrat, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: "700"
    lineHeight: "1.2"
    letterSpacing: "0.08em"
    textTransform: "uppercase"
rounded:
  none: "0"
  sm: "4px"
  md: "8px"
  lg: "14px"
  xl: "20px"
  pill: "9999px"
spacing:
  base: "4px"
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  2xl: "48px"
  3xl: "64px"
  section-y: "clamp(56px, 7vw, 92px)"
  container-gutter: "20px"
  hero-y: "72px"
layout:
  container: "min(100% - 40px, 1200px)"
  maxWidth: "1200px"
  topbarHeight: "5px"
  headerHeight: "80px"
  heroMinHeight: "600px"
  anchorScrollMarginTop: "104px"
elevation:
  soft: "0 18px 50px rgba(22, 0, 35, 0.14)"
  goldGlow: "0 0 24px rgba(214, 181, 109, 0.28)"
motion:
  defaultDuration: "150ms"
  defaultTiming: "cubic-bezier(0.4, 0, 0.2, 1)"
  entranceDuration: "700ms"
  entranceTiming: "cubic-bezier(0.22, 1, 0.36, 1)"
  entranceOffsetY: "14px"
breakpoints:
  careerCarouselMobileMax: "720px"
  careerCarouselTabletMax: "1024px"
---

# DESIGN.md — Curso Ênfase

## 1. Função deste documento

Este arquivo é a fonte de verdade visual e estrutural para agentes que criam, editam, revisam ou refatoram páginas do site do Curso Ênfase.

Ele deve permitir que um agente:

- construa uma página nova sem inventar uma identidade paralela;
- corrija páginas existentes que não seguem o padrão;
- reutilize componentes já estabelecidos;
- preserve comportamento responsivo e acessibilidade;
- respeite regras de negócio;
- mantenha consistência entre site, Figma e materiais institucionais;
- reduza a necessidade de repetir contexto em prompts.

Quando houver conflito, aplicar esta ordem de prioridade:

1. dados e regras de negócio oficiais e atuais;
2. código e tokens oficiais do site;
3. componentes e estilos oficiais do Figma;
4. este documento;
5. inferências visuais do agente.

O agente não deve tratar este arquivo como uma licença para inventar dados, preços, resultados, condições comerciais ou regras acadêmicas.

---

## 2. Princípio central da marca

Toda página deve comunicar, nesta ordem:

1. autoridade;
2. clareza;
3. direção;
4. confiança;
5. sofisticação;
6. modernidade discreta.

O Ênfase deve parecer:

- jurídica;
- experiente;
- premium;
- organizada;
- institucional;
- atual;
- objetiva;
- segura.

O Ênfase não deve parecer:

- startup SaaS;
- plataforma tecnológica genérica;
- cursinho visualmente popular ou agressivo;
- site infantil;
- escritório jurídico excessivamente conservador;
- template pronto de landing page;
- campanha desconectada da identidade principal;
- produto neon, futurista ou experimental.

A interface combina tradição jurídica e experiência editorial com uma construção digital limpa, responsiva e orientada à conversão.

---

## 3. Personalidade visual

### 3.1 Conceitos visuais principais

A identidade deve remeter a:

- bibliotecas;
- livros jurídicos;
- madeira;
- couro;
- tribunais;
- instituições públicas;
- profissionais do Direito;
- iluminação quente;
- autoridade acadêmica;
- preparação de alto nível.

### 3.2 Equilíbrio da marca

A marca é:

- séria, sem ser fria;
- sofisticada, sem ser ostensiva;
- tradicional, sem parecer ultrapassada;
- comercial, sem parecer agressiva;
- objetiva, sem parecer seca;
- jurídica, sem ser burocrática.

### 3.3 Regra de decisão

Quando houver duas soluções visualmente válidas, preferir a que seja:

- mais simples;
- mais editorial;
- mais legível;
- mais sóbria;
- mais alinhada aos componentes existentes;
- menos decorativa;
- mais fácil de manter.

---

## 4. Cores

### 4.1 Tokens oficiais

```css
:root {
  --background: #fff;
  --foreground: #160023;

  --enfase-red-1: #ff2759;
  --enfase-red-2: #d6224c;
  --enfase-red-deep: #370f18;

  --enfase-purple: #200140;
  --enfase-purple-hi: #3a0a6e;
  --enfase-purple-dark: #170030;

  --enfase-ink: #160023;
  --enfase-muted: #675f78;
  --enfase-gold: #d6b56d;
  --enfase-line: #20014024;

  --enfase-surface: #fff;
  --enfase-soft: #f5f2f8;
  --enfase-soft-2: #eee8f4;
}
```

### 4.2 Função de cada cor

#### Rosa principal — `#FF2759`

Usar em:

- CTA principal;
- ações importantes;
- ícones interativos;
- estados ativos;
- elementos de alta prioridade;
- preços em destaque;
- linha superior da página;
- identidade da marca.

Não usar como:

- fundo predominante de página;
- cor de grandes seções;
- texto corrido;
- decoração repetida em todos os componentes.

#### Rosa escuro — `#D6224C`

Usar principalmente em:

- hover;
- pressed;
- estados mais densos do CTA;
- gradientes ou detalhes controlados.

#### Roxo institucional — `#200140`

Usar em:

- fundos escuros;
- ícones institucionais;
- bordas e detalhes;
- títulos secundários;
- superfícies de dropdown;
- elementos de navegação.

#### Roxo escuro — `#170030`

Usar em:

- header;
- dropdown;
- hero;
- blocos de alto contraste;
- rodapé;
- navegação ativa em fundos escuros.

#### Texto principal — `#160023`

Usar em:

- títulos e textos em superfícies claras;
- labels;
- preços;
- informações principais.

#### Texto secundário — `#675F78`

Usar em:

- descrições;
- supporting copy;
- metadados;
- FAQ;
- textos auxiliares.

#### Dourado — `#D6B56D`

Usar em:

- divisores;
- badges premium;
- contornos de plano recomendado;
- detalhes jurídicos;
- pequenas sinalizações de autoridade.

Não usar em:

- parágrafos;
- grandes fundos;
- CTAs principais;
- texto pequeno com contraste baixo.

#### Superfícies

- branco: `#FFFFFF`;
- superfície clara: `#F5F2F8`;
- superfície alternativa: `#EEE8F4`;
- linha/borda: `rgba(32, 1, 64, 0.14)`.

### 4.3 Proporção recomendada

Em páginas claras:

- 65–80% superfícies claras;
- 10–20% roxo/escuro;
- 5–10% rosa;
- menos de 5% dourado.

Essa proporção é orientativa. A regra mais importante é não diluir a força do rosa e do dourado pelo uso excessivo.

### 4.4 Contraste

- texto principal em fundo claro: `#160023`;
- texto secundário em fundo claro: `#675F78`;
- texto em fundo escuro: branco;
- bordas em fundo claro: `#20014024`;
- focus em fundo claro: roxo;
- focus em fundo escuro: branco ou rosa, desde que o contraste seja adequado.

---

## 5. Tipografia

### 5.1 Famílias oficiais

```css
--font-brand:
  var(--font-montserrat),
  "Inter",
  ui-sans-serif,
  system-ui,
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  sans-serif;

--font-headline:
  var(--font-pt-serif),
  Georgia,
  "Times New Roman",
  serif;
```

### 5.2 Montserrat

Usar em:

- corpo;
- botões;
- navegação;
- labels;
- FAQ;
- preços;
- formulários;
- metadados;
- cards funcionais;
- menus;
- descrições.

### 5.3 PT Serif

Usar em:

- H1;
- H2 de seção;
- títulos editoriais;
- títulos de cards institucionais;
- títulos de pricing;
- blocos que precisam transmitir autoridade.

Não usar PT Serif em:

- botões;
- navegação;
- campos de formulário;
- labels;
- textos longos;
- mensagens de sistema.

### 5.4 Escalas confirmadas

#### H1 do hero

```css
font-family: var(--font-headline);
font-size: clamp(42px, 6vw, 60px);
font-weight: 700;
line-height: 0.98;
letter-spacing: 0;
```

#### H2 de seção

```css
font-family: var(--font-headline);
font-size: clamp(34px, 4vw, 54px);
font-weight: 700;
line-height: 1.05;
letter-spacing: 0;
color: #170030;
```

### 5.5 Regras tipográficas

- não usar tracking negativo em títulos serifados;
- manter line-height mais fechado apenas em títulos grandes;
- evitar parágrafos longos ocupando o container inteiro;
- limitar headings centrais a aproximadamente 820px;
- usar `strong` para ênfase moderada;
- reservar caixa alta a overlines, badges e labels;
- não usar mais de três pesos diferentes na mesma seção;
- não usar bold excessivo em todos os textos;
- não centralizar parágrafos longos;
- não inserir quebras `<br>` rígidas sem necessidade;
- se houver quebra editorial, ela deve ser responsiva.

### 5.6 Observação técnica

O CSS solicita PT Serif com peso 700. Confirmar que esse peso está carregado. Não depender de bold sintético em novas implementações.

---

## 6. Layout

### 6.1 Container

```css
--container: min(100% - 40px, 1200px);
```

Equivalente a:

```css
width: min(100% - 40px, 1200px);
margin-inline: auto;
```

Regras:

- largura máxima de 1200px;
- gutter mínimo de 20px por lado;
- alinhamento central;
- seções full-bleed podem ter fundo de largura total, mas o conteúdo interno deve alinhar ao container;
- não criar containers independentes com larguras arbitrárias.

### 6.2 Estrutura global

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

Valor resultante aproximado: `104px`.

### 6.3 Espaçamento de seção

```css
.section {
  padding: clamp(56px, 7vw, 92px) 0;
}
```

O espaço negativo faz parte da identidade. Não reduzir seções apenas para mostrar mais conteúdo acima da dobra.

### 6.4 Ritmo

Usar escala baseada em 4px:

- 4px;
- 8px;
- 16px;
- 24px;
- 32px;
- 48px;
- 64px;
- `clamp(56px, 7vw, 92px)`.

Evitar valores arbitrários como 13px, 27px ou 43px, exceto quando comprovados no componente existente.

### 6.5 Cabeçalho de seção

```css
.section-heading {
  text-align: center;
  max-width: 820px;
  margin: 0 auto 32px;
}
```

Estrutura:

1. overline opcional;
2. H2;
3. divisor dourado;
4. supporting copy.

### 6.6 Divisor dourado

```css
.section-heading h2::after {
  content: "";
  width: 60px;
  height: 2px;
  margin: 18px auto 0;
  display: block;
  border-radius: 999px;
  background: #d6b56d;
  box-shadow: 0 0 24px rgba(214, 181, 109, 0.28);
}
```

Usar em títulos principais de seção, não em headings internos de cards.

---

## 7. Fundos

### 7.1 Hero escuro

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

Características:

- roxo quase preto;
- brilho quente central;
- profundidade;
- atmosfera de biblioteca;
- contraste alto;
- ausência de neon.

### 7.2 Seção clara institucional

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

A textura deve permanecer sutil.

### 7.3 Alternância de seções

Preferir alternância entre:

- branco texturizado;
- soft lilás;
- roxo escuro;
- bloco branco elevado.

Não alternar cores sem função narrativa.

---

## 8. Bordas, raios e sombras

### 8.1 Raios

- 4px: controles pequenos;
- 8px: botões e elementos interativos;
- 14px: cards padrão;
- 20px: cards editoriais maiores;
- 9999px: pills, badges e divisores.

### 8.2 Sombra padrão

```css
box-shadow: 0 18px 50px rgba(22, 0, 35, 0.14);
```

Usar em:

- dropdowns;
- pricing destacado;
- cards elevados;
- menus;
- componentes flutuantes.

### 8.3 Bordas

```css
border: 1px solid rgba(32, 1, 64, 0.14);
```

Não usar borda preta ou cinza pesada.

### 8.4 Proibições

- não usar glassmorphism;
- não usar blur como linguagem principal;
- não usar sombras duras;
- não usar bordas grossas sem função;
- não arredondar todos os elementos como pills.

---

## 9. Motion

### 9.1 Transição padrão

```css
transition-duration: 150ms;
transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
```

Aplicar em:

- cores;
- bordas;
- background;
- opacidade;
- transform leve;
- ícones.

### 9.2 Entrada fade-up

```css
animation:
  700ms
  cubic-bezier(0.22, 1, 0.36, 1)
  both
  fade-up;
```

Estado inicial:

```css
opacity: 0;
transform: translateY(14px);
```

Aplicar apenas a elementos de entrada relevantes:

- H1;
- overline;
- título de page hero;
- divisor;
- elementos editoriais de destaque.

### 9.3 Reduced motion

```css
@media (prefers-reduced-motion: no-preference) {
  /* animações */
}
```

Quando o usuário preferir menos movimento:

- remover translate;
- remover animação de entrada;
- reduzir transições;
- manter o conteúdo visível;
- não tornar nenhuma informação dependente de animação.

### 9.4 Não usar

- autoplay;
- bounce;
- parallax forte;
- animações contínuas;
- rotação decorativa;
- transições acima de 1 segundo;
- movimento que altere layout;
- animação de texto permanente.

---

## 10. Header e navegação

### 10.1 Anatomia

O header desktop contém:

- topbar rosa de 5px;
- fundo roxo escuro;
- logo;
- grupos de carreira;
- botão Portal;
- CTA “Falar com a equipe”.

### 10.2 Regras

- altura desktop: 80px;
- logo alinhado ao container;
- links em Montserrat;
- ação principal em rosa;
- Portal como ação secundária outline;
- dropdown em roxo escuro;
- estado ativo destacado;
- foco visível;
- navegação por teclado;
- mobile deve usar menu colapsado.

### 10.3 Dropdown

- fundo `#170030`;
- texto branco/cinza claro;
- sombra suave;
- raio moderado;
- itens com área clicável ampla;
- abrir por teclado;
- fechar com Escape;
- não depender apenas de hover;
- funcionar em touch.

### 10.4 Portais

Distinguir:

- Portal de Entrada;
- Portal da Pós.

Não substituir um pelo outro.

---

## 11. Hero principal

### 11.1 Estrutura semântica

```html
<section class="hero" aria-labelledby="hero-title">
  <div class="hero__inner">
    <div class="hero__copy">
      <h1 id="hero-title">...</h1>
      <div class="hero__divider" aria-hidden="true"></div>
      <p>...</p>

      <div
        class="hero__actions"
        aria-label="Ações principais"
      >
        ...
      </div>
    </div>
  </div>
</section>
```

### 11.2 Layout confirmado

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

### 11.3 Conteúdo

O hero deve conter:

1. título;
2. divisor;
3. texto de apoio;
4. CTA principal;
5. CTA secundário opcional;
6. imagem jurídica;
7. contraste suficiente.

### 11.4 Regras de copy

O título deve responder rapidamente:

- qual carreira;
- qual curso;
- qual fase;
- qual resultado de organização/direção.

O texto deve explicar:

- para quem;
- qual método;
- qual benefício;
- qual diferencial.

Não usar mais de dois CTAs principais.

### 11.5 Page hero

Páginas internas podem usar uma versão menor:

- título PT Serif;
- overline;
- supporting copy;
- CTA;
- imagem ou fundo escuro;
- altura inferior ao hero da home.

Não replicar o hero da home integralmente em todas as páginas.

---

## 12. Botões

### 12.1 Primário

```css
background: #ff2759;
color: #fff;
min-height: 48px;
padding: 0 24px;
border-radius: 8px;
font-family: Montserrat, sans-serif;
font-weight: 700;
```

Hover:

```css
background: #d6224c;
```

### 12.2 Outline em fundo escuro

- transparente;
- texto branco;
- borda clara;
- hover com branco de baixa opacidade;
- não competir visualmente com CTA principal.

### 12.3 Outline em fundo claro

- transparente;
- texto rosa;
- borda rosa;
- hover com rosa suave ou preenchimento rosa.

### 12.4 Texto

Preferir:

- Explorar carreiras;
- Começar pelo ENAM;
- Conhecer o NDCJ;
- Conhecer o NDP;
- Garantir minha vaga;
- Falar com a equipe;
- Ver resposta.

Evitar:

- Clique aqui;
- Saiba mais;
- Ver mais;
- Continuar;
- Acessar, quando um termo mais específico existir.

### 12.5 Estados obrigatórios

Todo botão deve ter:

- default;
- hover;
- focus-visible;
- active;
- disabled;
- loading, quando assíncrono.

Disabled não pode depender apenas de cor.

---

## 13. Ícones

### 13.1 Ícones funcionais

Preferir Lucide.

```html
<svg
  class="lucide"
  aria-hidden="true"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
>
```

### 13.2 Regras

- usar `currentColor`;
- ícones decorativos recebem `aria-hidden="true"`;
- botão apenas com ícone recebe `aria-label`;
- manter traço consistente;
- não misturar múltiplas bibliotecas no mesmo componente;
- não usar emoji como ícone da UI.

### 13.3 Ícones institucionais

SVGs próprios podem representar:

- tribunais;
- balança;
- carreiras;
- documentos;
- plano de estudos;
- diagnóstico;
- execução guiada;
- resposta rápida.

Manter estilo linear e institucional.

---

## 14. Cards de carreira

### 14.1 Anatomia

```html
<article class="career-card">
  <a class="career-card__link" href="...">
    <div
      class="career-card__media"
      aria-hidden="true"
    >
      <img alt="" ...>
    </div>

    <div class="career-card__body">
      <span class="career-card__icon">
        ...
      </span>

      <h3 class="career-card__title">
        ...
      </h3>

      <p class="career-card__description">
        ...
      </p>
    </div>
  </a>
</article>
```

### 14.2 Regras

- card inteiro clicável;
- usar `<article>`;
- imagem decorativa com `alt=""`;
- título claro;
- descrição específica;
- ícone circular sobreposto;
- sombra suave;
- fundo branco;
- borda discreta;
- focus no link inteiro;
- hover sutil;
- não repetir imagens em cards diferentes.

### 14.3 Responsividade confirmada

```html
sizes="
  (max-width: 720px) 78vw,
  (max-width: 1024px) 33vw,
  20vw
"
```

Comportamento:

- mobile: carrossel horizontal;
- tablet: largura aproximada de 33vw;
- desktop: largura aproximada de 20vw.

### 14.4 Carreiras oficiais

1. Magistratura Federal;
2. Magistratura Estadual;
3. Magistratura Federal e Estadual;
4. Procuradorias;
5. Magistratura Federal e MPF;
6. Magistratura Estadual e MPE;
7. Magistratura do Trabalho e MPT;
8. Defensorias.

Não alterar os nomes sem confirmação.

---

## 15. Carrossel

### 15.1 Estrutura

```html
<div class="career-carousel">
  <div class="mobile-carousel__viewport">
    <div class="career-grid">
      ...
    </div>
  </div>

  <div class="mobile-carousel__nav">
    <button aria-label="Anterior">...</button>
    <button aria-label="Próximo">...</button>
  </div>
</div>
```

### 15.2 Regras

- viewport com overflow controlado;
- navegação anterior/próximo;
- estado `disabled`;
- labels acessíveis;
- não depender apenas de swipe;
- não usar autoplay;
- preservar conteúdo no DOM;
- não esconder controles em desktop sem motivo;
- suportar teclado.

---

## 16. Cards institucionais

Usados para:

- NDCJ;
- NDP;
- diferenciais;
- explicações;
- apresentação de produtos;
- etapas.

Características:

- fundo branco;
- borda sutil;
- sombra suave;
- título editorial em PT Serif quando adequado;
- descrição em Montserrat;
- CTA rosa;
- padding generoso;
- composição simples;
- pouco ornamento.

Não inserir vários badges, ícones e CTAs no mesmo card sem função clara.

---

## 17. Pricing

### 17.1 Estrutura

1. overline;
2. título;
3. opções;
4. badge de destaque;
5. prazo;
6. preço;
7. condição;
8. desconto;
9. CTA.

### 17.2 Regras

- preço e condições devem ser oficiais e atuais;
- não copiar preço de outra página;
- plano recomendado pode usar borda dourada;
- badge dourado em pill;
- preço em rosa;
- explicar parcelamento e valor à vista;
- mostrar prazo de acesso;
- manter comparação justa;
- CTA principal no plano recomendado.

### 17.3 Proibição

Não inventar:

- desconto;
- cashback;
- bônus;
- prazo;
- parcelamento;
- número de vagas;
- data de encerramento.

---

## 18. FAQ / Accordion

### 18.1 Anatomia

- pergunta;
- ícone `+`;
- estado aberto com `×` ou rotação;
- resposta;
- borda;
- área clicável inteira.

### 18.2 Semântica

Usar:

```html
<button
  aria-expanded="false"
  aria-controls="faq-panel-id"
>
```

### 18.3 Regras

- todo o cabeçalho clicável;
- não clicar apenas no ícone;
- navegação por teclado;
- resposta em Montserrat;
- cor muted;
- animação suave;
- reduced motion;
- manter comportamento existente de múltiplos ou único item aberto.

### 18.4 Conteúdo

FAQ deve responder dúvidas reais:

- carreiras;
- ENAM;
- Núcleo Duro;
- aulas;
- acesso;
- simulados;
- suporte;
- preço;
- prazo;
- garantia, se oficial.

Não copiar FAQs irrelevantes entre produtos.

---

## 19. Professores

### 19.1 Fotografia

- imagem oficial;
- boa resolução;
- recorte consistente;
- fundo sóbrio;
- tratamento profissional;
- sem filtros exagerados;
- aparência real;
- boa iluminação.

### 19.2 Conteúdo

- nome;
- cargo ou especialidade;
- credenciais verificáveis;
- vínculo com o curso;
- sem afirmações infladas.

### 19.3 Figma

A página “Professores” do Figma é referência oficial de:

- fotos;
- nomenclatura;
- organização;
- recortes;
- proporções.

---

## 20. Templates de redes sociais

O Figma possui referências de:

- edital + demanda;
- prova/questão;
- resposta;
- diagnóstico;
- plano de estudo;
- execução guiada;
- resposta rápida.

Esses materiais ajudam a manter consistência de:

- paleta;
- tipografia;
- hierarquia;
- ícones;
- CTA;
- linguagem de dados.

Não copiar layouts de Instagram diretamente para a web. Adaptar a lógica, não a proporção.

---

## 21. Fotografia e imagens

### 21.1 Direção de arte

Preferir:

- profissionais do Direito;
- magistrados;
- procuradores;
- defensores;
- promotores;
- tribunais;
- livros;
- biblioteca;
- madeira;
- documentos;
- balança;
- ambientes institucionais.

### 21.2 Estilo

- cinematográfico;
- tons quentes;
- sombras profundas;
- contraste controlado;
- fundo desfocado;
- roupa formal;
- expressão séria;
- composição com espaço para texto.

### 21.3 Evitar

- stock photo genérica;
- coworking;
- pessoa sorrindo para notebook;
- aperto de mãos;
- pose corporativa artificial;
- martelo de juiz como clichê dominante;
- anatomia incorreta em imagens geradas;
- texto embutido na imagem;
- repetição da mesma foto.

### 21.4 Imagens decorativas

Quando a imagem não acrescentar informação semântica:

```html
<div aria-hidden="true">
  <img alt="">
</div>
```

Quando comunicar informação real, usar alt descritivo.

### 21.5 Performance

- definir dimensões;
- evitar CLS;
- lazy load abaixo da dobra;
- usar `sizes`;
- otimizar formato;
- priorizar hero;
- `object-fit: cover`;
- ajustar `object-position`.

---

## 22. Footer

O footer deve conter:

- logo;
- descrição institucional;
- carreiras;
- links institucionais;
- links úteis;
- informações legais;
- copyright.

Links úteis esperados:

- Quem Somos;
- Fale Conosco;
- Blog;
- Portal de Entrada;
- Portal da Pós.

Não remover um portal ao adicionar o outro.

---

## 23. Formulários

### 23.1 Regras

- labels visíveis;
- placeholder não substitui label;
- mensagens específicas;
- estados de erro e sucesso;
- foco visível;
- altura confortável;
- ajuda associada por `aria-describedby`;
- loading;
- prevenção de envio duplicado;
- privacidade e consentimento quando aplicável.

### 23.2 Campos

- fundo branco ou soft;
- borda discreta;
- raio moderado;
- texto ink;
- erro não depende apenas de vermelho;
- área mínima de toque de 44px.

---

## 24. Acessibilidade

### 24.1 Semântica

- um H1 por página;
- hierarquia correta;
- `<nav>` para navegação;
- `<main>` para conteúdo;
- `<section>` com heading;
- `<article>` para cards;
- `<button>` para ações;
- `<a>` para navegação;
- não usar `<div>` clicável.

### 24.2 Teclado

Suportar:

- Tab;
- Shift+Tab;
- Enter;
- Espaço;
- Escape;
- setas quando aplicável.

### 24.3 Focus visible

Sugestão em fundo claro:

```css
outline: 3px solid #3a0a6e;
outline-offset: 3px;
```

Em fundo escuro:

```css
outline: 3px solid #ffffff;
outline-offset: 3px;
```

### 24.4 Contraste

Atender WCAG AA:

- 4.5:1 para texto normal;
- 3:1 para texto grande;
- 3:1 para componentes gráficos essenciais.

### 24.5 Movimento

Respeitar `prefers-reduced-motion`.

### 24.6 Touch

Área mínima aproximada: 44x44px.

### 24.7 Skip link

Manter “Pular para o conteúdo” como primeiro link focável.

---

## 25. Responsividade

### 25.1 Princípio

Mobile não é o desktop reduzido. Reorganizar:

- header;
- hero;
- cards;
- pricing;
- grids;
- CTAs;
- tabelas.

### 25.2 Hero mobile

- título continua legível;
- ações podem empilhar;
- botões podem ocupar largura total;
- imagem não compete com texto;
- altura não deve ser fixa;
- manter padding vertical.

### 25.3 Cards

- uma coluna para cards grandes;
- carrossel quando o componente existente usa carrossel;
- duas colunas apenas com largura suficiente;
- preservar padding.

### 25.4 Header

- menu colapsado;
- Portal acessível;
- contato acessível;
- disclosure em vez de hover puro.

### 25.5 Pricing

- planos empilhados;
- plano recomendado preservado;
- ordem de conteúdo mantida.

### 25.6 Quebras manuais

Quebras como `.desktop-break` devem ser removidas ou ocultadas em mobile.

---

## 26. Regras de negócio

### 26.1 Objetivo

Regras de negócio devem impedir que o agente produza páginas visualmente corretas, porém comercialmente ou juridicamente erradas.

### 26.2 Produtos e carreiras

Não alterar:

- nomes;
- combinações;
- destinos;
- escopo;
- etapa;
- público.

Sem confirmação.

### 26.3 ENAM

O ENAM se relaciona às magistraturas. Não assumir aplicação automática a Procuradorias, Defensorias ou outros produtos.

Regras, datas, cashback e condições precisam de fonte oficial atual.

### 26.4 Núcleo Duro

Existem ao menos:

- NDCJ — Núcleo Duro Carreiras Jurídicas;
- NDP — Núcleo Duro Procuradorias.

Núcleo Duro não é sinônimo de curso Regular.

### 26.5 Conteúdo e acesso

Não generalizar entre produtos:

- aulas ao vivo;
- aulas gravadas;
- PDF;
- simulados;
- correção;
- cronograma;
- mentoria;
- acesso integral;
- acesso progressivo;
- prazo.

### 26.6 Preço

Sempre verificar:

- produto;
- vigência;
- parcelamento;
- Pix;
- desconto;
- acesso;
- bônus;
- checkout.

### 26.7 Resultados

Permitido:

- tradição;
- método;
- resultados oficiais;
- aprovações verificadas;
- depoimentos autorizados.

Proibido:

- aprovação garantida;
- método infalível;
- números inventados;
- causalidade absoluta;
- afirmações não comprovadas.

### 26.8 WhatsApp

“Falar com a equipe” deve usar link oficial. Não criar números divergentes.

### 26.9 FAQ

FAQ deve refletir o produto específico.

### 26.10 Ordem narrativa

A sequência recomendada é:

1. proposta;
2. público;
3. método;
4. conteúdo;
5. diferenciais;
6. prova social;
7. FAQ;
8. investimento;
9. CTA final.

Não é obrigatório usar todas as seções.

---

## 27. Templates de página

### 27.1 Home

1. header;
2. hero;
3. carreiras;
4. ENAM;
5. Núcleo Duro;
6. autoridade/resultados;
7. FAQ;
8. footer.

### 27.2 Página de carreira

1. header;
2. page hero;
3. para quem é;
4. proposta;
5. método;
6. conteúdo;
7. professores;
8. materiais;
9. diferenciais;
10. resultados;
11. FAQ;
12. investimento;
13. CTA;
14. footer.

### 27.3 Fase avançada

1. concurso/fase/banca;
2. contexto;
3. escopo;
4. cronograma;
5. acompanhamento;
6. professores;
7. entregáveis;
8. FAQ;
9. preço;
10. CTA.

### 27.4 Institucional

1. hero;
2. história;
3. proposta;
4. números;
5. método;
6. equipe;
7. CTA;
8. footer.

### 27.5 Professores

1. hero curto;
2. grupos/filtros;
3. cards;
4. credenciais;
5. CTA.

### 27.6 Landing page de campanha

1. headline;
2. contexto factual;
3. oferta;
4. dados principais;
5. fonte/documento;
6. próximos passos;
7. CTA;
8. condições;
9. FAQ.

Campanha não pode criar uma identidade visual independente.

---

## 28. SEO e conteúdo

### 28.1 Headings

- um H1;
- H2 por seção;
- H3 em cards;
- não usar heading apenas por aparência.

### 28.2 Links

- texto descritivo;
- evitar “clique aqui”;
- evitar nomes diferentes para o mesmo destino;
- verificar links externos.

### 28.3 Conteúdo

- usar nomes oficiais;
- responder intenção de busca;
- evitar texto genérico;
- manter parágrafos curtos;
- usar listas somente quando ajudam;
- FAQ pode usar dados estruturados, se compatível.

### 28.4 Imagens

- dimensões;
- alt correto;
- lazy loading;
- prioridade;
- formato otimizado;
- sem CLS.

---

## 29. Implementação

### 29.1 Tokens

Reutilizar tokens globais. Não hardcodar a mesma cor e o mesmo espaço em vários componentes.

### 29.2 Componentes

Criar variantes controladas.

Bom:

- `Button`;
- `ButtonPrimary`;
- `ButtonOutline`;
- `SectionHeading`;
- `CareerCard`;
- `PricingCard`;
- `Accordion`;
- `PageHero`.

Ruim:

- `HomePinkButton`;
- `DefensoriaPinkButton`;
- `NdcjPinkButton`;
- `OtherPinkButton`.

### 29.3 Dados

Centralizar:

- links;
- cursos;
- FAQs;
- preços;
- informações institucionais;
- professores;
- CTAs.

### 29.4 Alterações em componentes compartilhados

Antes de alterar:

- verificar todas as páginas impactadas;
- revisar responsividade;
- revisar estados;
- revisar acessibilidade;
- não corrigir uma página quebrando outras.

---

## 30. Figma e ativos

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

---

## 31. O que fazer

- usar PT Serif em títulos;
- usar Montserrat na interface;
- respeitar container de 1200px;
- manter espaço negativo;
- usar rosa para ação;
- usar dourado com moderação;
- usar imagens jurídicas coerentes;
- manter animações sutis;
- reutilizar componentes;
- escrever CTAs específicos;
- preservar foco;
- validar conteúdo comercial;
- testar mobile;
- testar teclado;
- preservar os dois portais.

---

## 32. O que não fazer

- não usar glassmorphism;
- não usar azul SaaS;
- não usar neon;
- não usar sombras duras;
- não arredondar tudo;
- não usar sans em todos os títulos;
- não usar serif em botões;
- não usar fotos genéricas;
- não repetir imagens;
- não misturar bibliotecas de ícones;
- não inventar preço;
- não inventar prazo;
- não inventar resultado;
- não prometer aprovação;
- não criar identidade paralela;
- não reduzir padding para “encaixar” conteúdo;
- não usar autoplay;
- não remover Portal de Entrada ao adicionar Portal da Pós;
- não alterar produto, carreira ou regra sem confirmação.

---

## 33. Checklist obrigatório para agentes

Antes de concluir uma página:

### Conteúdo

- [ ] O H1 descreve claramente a página?
- [ ] O produto e a carreira estão corretos?
- [ ] Os preços foram confirmados?
- [ ] As condições foram confirmadas?
- [ ] Os links foram confirmados?
- [ ] Não existem promessas indevidas?
- [ ] O CTA é específico?

### Visual

- [ ] As cores usam tokens oficiais?
- [ ] PT Serif e Montserrat estão nos papéis corretos?
- [ ] O conteúdo usa o container oficial?
- [ ] O espaçamento segue o sistema?
- [ ] As imagens seguem a direção de arte?
- [ ] O dourado não está excessivo?
- [ ] O rosa está reservado a ações e destaque?

### Componentes

- [ ] Foram reutilizados componentes existentes?
- [ ] Hover existe?
- [ ] Focus-visible existe?
- [ ] Disabled existe?
- [ ] Loading existe quando necessário?
- [ ] O card inteiro é clicável quando deve ser?
- [ ] O accordion usa semântica correta?
- [ ] O carrossel tem controles acessíveis?

### Responsividade

- [ ] Desktop revisado?
- [ ] Tablet revisado?
- [ ] Mobile revisado?
- [ ] Botões não quebram?
- [ ] Headings não transbordam?
- [ ] Imagens mantêm foco?
- [ ] Pricing empilha corretamente?
- [ ] Menu mobile funciona?

### Acessibilidade

- [ ] Um único H1?
- [ ] Hierarquia de headings correta?
- [ ] Navegação por teclado?
- [ ] Focus visível?
- [ ] Contraste AA?
- [ ] Reduced motion?
- [ ] Alt texts corretos?
- [ ] Touch targets adequados?

### Regressão

- [ ] Componentes compartilhados foram verificados?
- [ ] Nenhum link oficial foi removido?
- [ ] Portal de Entrada e Portal da Pós foram preservados?
- [ ] Não houve alteração acidental em outra página?

---

## 34. Estado deste documento

Valores oficialmente confirmados pelo site:

- cores;
- fontes;
- container;
- topbar;
- header;
- hero;
- sombra;
- H1;
- H2;
- espaçamento de seção;
- fundo claro;
- fundo base do hero;
- divisor dourado;
- animação fade-up;
- transição padrão;
- estrutura semântica do hero;
- estrutura dos cards de carreira;
- breakpoints do carrossel de carreira.

Valores que devem ser tratados como padrões consolidados, mas ainda podem ser refinados com inspeção adicional:

- escala completa de body;
- escala de card titles;
- altura exata de todos os botões;
- padding de todos os cards;
- hover exato de todos os componentes;
- grids de páginas internas;
- breakpoints globais;
- estados de formulário;
- estrutura de todas as páginas.

Quando o código oficial fornecer um valor mais preciso, atualizar este arquivo.
