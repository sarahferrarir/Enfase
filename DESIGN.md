---
version: "2.0"
status: "active"
name: "Ênfase Design System"
website: "https://cursoenfase.com.br/"
purpose:
  - "Orientar humanos e agentes na criação de interfaces do Ênfase."
  - "Orientar auditorias, correções e refatorações de páginas existentes."
  - "Padronizar identidade visual, tokens, componentes, conteúdo, acessibilidade e responsividade."
  - "Separar decisões de design de regras específicas de negócio."
  - "Reduzir contexto repetido em prompts para Codex, Claude, ChatGPT e outros agentes."
source_priority:
  - "Código e tokens oficiais do site."
  - "Componentes e estilos oficiais do Figma."
  - "Este DESIGN.md."
  - "Padrões visuais recorrentes do ecossistema do Ênfase."
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
  mobileMax: "720px"
  tabletMax: "1024px"
  desktopMin: "1025px"
---

# Ênfase Design System

## 1. Introdução

Este documento é a fonte de verdade visual e estrutural para qualquer interface do Ênfase.

Ele deve ser usado por designers, desenvolvedores, redatores e agentes de IA ao criar, revisar, auditar ou refatorar:

- landing pages;
- páginas institucionais;
- páginas de curso;
- blogs;
- páginas de artigo;
- dashboards;
- ferramentas;
- planners;
- trackers;
- portais;
- áreas internas;
- aplicações administrativas;
- sistemas web;
- páginas de documentação.

O objetivo não é reproduzir uma Home específica. O objetivo é garantir que qualquer interface pareça pertencer ao mesmo ecossistema: clara, jurídica, editorial, responsiva, acessível e consistente.

Quando houver conflito entre fontes, aplicar esta prioridade:

1. dados oficiais e regras de negócio atuais;
2. código e tokens oficiais do site;
3. componentes e estilos oficiais do Figma;
4. este documento;
5. inferência do agente, apenas quando não houver fonte melhor.

Este arquivo não autoriza agentes a inventar dados, preços, resultados, condições comerciais, regras acadêmicas, nomes de produtos ou afirmações institucionais.

Regra de linguagem: usar sempre "o Ênfase". Não usar artigo feminino para a marca.

---

## 2. Marca

### 2.1 Quem é o Ênfase

O Ênfase é uma marca de educação jurídica com linguagem institucional, editorial e contemporânea. A interface deve comunicar autoridade acadêmica e direção prática sem parecer rígida, datada ou excessivamente comercial.

O Ênfase deve parecer:

- jurídico;
- experiente;
- premium;
- organizado;
- institucional;
- atual;
- objetivo;
- confiável;
- editorial.

O Ênfase não deve parecer:

- startup SaaS genérica;
- plataforma tecnológica sem identidade jurídica;
- cursinho visualmente popular ou agressivo;
- site infantil;
- escritório jurídico frio ou excessivamente conservador;
- template pronto de landing page;
- campanha desconectada da identidade principal;
- produto neon, futurista ou experimental.

### 2.2 Personalidade visual

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

O equilíbrio desejado é:

- sério, sem ser frio;
- sofisticado, sem ser ostensivo;
- tradicional, sem parecer ultrapassado;
- comercial, sem parecer agressivo;
- objetivo, sem parecer seco;
- jurídico, sem ser burocrático.

### 2.3 Princípios de marca

Toda interface deve comunicar, nesta ordem:

1. autoridade;
2. clareza;
3. direção;
4. confiança;
5. sofisticação;
6. modernidade discreta.

Quando duas soluções forem visualmente válidas, preferir a que seja:

- mais simples;
- mais editorial;
- mais legível;
- mais sóbria;
- mais alinhada aos componentes existentes;
- menos decorativa;
- mais fácil de manter.

---

## 3. Design Principles

### 3.1 Função antes da decoração

Elementos visuais devem existir para estruturar, orientar, hierarquizar ou reforçar confiança. Ornamentos sem função devem ser removidos.

Evitar:

- excesso de badges;
- ícones decorativos repetidos;
- gradientes sem propósito;
- sombras fortes;
- padrões visuais competindo com o conteúdo.

### 3.2 Hierarquia forte

Cada tela deve deixar claro:

- onde o usuário está;
- qual é a informação principal;
- quais ações são possíveis;
- qual ação é prioritária;
- o que é secundário.

Usar contraste, tamanho, espaço negativo e posição antes de adicionar decoração.

### 3.3 Tipografia editorial

A combinação entre PT Serif e Montserrat é parte central da identidade. A serifada cria autoridade e ritmo editorial. A sans-serif sustenta leitura, navegação e operação.

### 3.4 Simplicidade operacional

Ferramentas, dashboards e sistemas internos devem ser mais densos e funcionais que páginas comerciais, mas ainda devem preservar tokens, tipografia, cores, acessibilidade e linguagem visual.

### 3.5 Consistência sobre novidade

Não criar uma identidade paralela para cada campanha, ferramenta ou produto. Novas páginas devem reutilizar tokens, componentes e padrões já definidos.

### 3.6 Leitura como prioridade

O Ênfase trabalha com conteúdo jurídico e educacional. Interfaces devem favorecer leitura, comparação, consulta e tomada de decisão.

Regras:

- parágrafos curtos;
- largura controlada de texto;
- títulos informativos;
- listas quando ajudam;
- tabelas quando comparação for necessária;
- CTAs específicos.

### 3.7 Componentes grandes, claros e acessíveis

Controles devem ter área confortável, estados visíveis, foco evidente e semântica correta. A sofisticação da marca não pode reduzir usabilidade.

---

## 4. Design Tokens

### 4.1 Tokens CSS oficiais

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

### 4.2 Cores

#### Rosa principal: `#FF2759`

Usar em:

- CTA principal;
- ações importantes;
- ícones interativos;
- estados ativos;
- elementos de alta prioridade;
- preços em destaque;
- linha superior da página;
- sinalização de marca.

Não usar como:

- fundo predominante;
- cor de grandes seções;
- texto corrido;
- decoração repetida em todos os componentes.

#### Rosa escuro: `#D6224C`

Usar em:

- hover;
- pressed;
- estados densos do CTA;
- detalhes controlados.

#### Roxo institucional: `#200140`

Usar em:

- fundos escuros;
- ícones institucionais;
- bordas e detalhes;
- títulos secundários;
- superfícies de dropdown;
- navegação.

#### Roxo escuro: `#170030`

Usar em:

- header;
- dropdown;
- hero;
- blocos de alto contraste;
- rodapé;
- navegação ativa em fundos escuros.

#### Texto principal: `#160023`

Usar em:

- títulos em superfícies claras;
- textos principais;
- labels;
- preços;
- informações críticas.

#### Texto secundário: `#675F78`

Usar em:

- descrições;
- supporting copy;
- metadados;
- respostas de FAQ;
- textos auxiliares.

#### Dourado: `#D6B56D`

Usar com moderação em:

- divisores;
- badges premium;
- contornos de destaque;
- detalhes jurídicos;
- pequenas sinalizações de autoridade.

Não usar em:

- parágrafos;
- grandes fundos;
- CTAs principais;
- texto pequeno com contraste baixo.

#### Superfícies

- `#FFFFFF`: superfície base;
- `#F5F2F8`: superfície clara alternativa;
- `#EEE8F4`: superfície de apoio;
- `#20014024`: linha ou borda sutil.

### 4.3 Proporção de cor

Em interfaces claras, usar como referência:

- 65-80% superfícies claras;
- 10-20% roxo ou escuro;
- 5-10% rosa;
- menos de 5% dourado.

A regra principal é preservar força semântica. Rosa deve significar ação ou destaque. Dourado deve significar autoridade, refinamento ou recomendação.

### 4.4 Contraste

- texto principal em fundo claro: `#160023`;
- texto secundário em fundo claro: `#675F78`;
- texto em fundo escuro: branco;
- bordas em fundo claro: `#20014024`;
- foco em fundo claro: `#3A0A6E`;
- foco em fundo escuro: branco ou rosa com contraste adequado.

Atender WCAG AA:

- 4.5:1 para texto normal;
- 3:1 para texto grande;
- 3:1 para componentes gráficos essenciais.

### 4.5 Espaçamento

Usar escala baseada em 4px:

- `4px`;
- `8px`;
- `16px`;
- `24px`;
- `32px`;
- `48px`;
- `64px`;
- `clamp(56px, 7vw, 92px)` para seções.

Evitar valores arbitrários como `13px`, `27px` ou `43px`, exceto quando já existirem em componente oficial ou quando houver motivo técnico documentado.

### 4.6 Bordas, radius e sombras

Radius:

- `0`: superfícies sem arredondamento;
- `4px`: controles pequenos;
- `8px`: botões e elementos interativos;
- `14px`: cards padrão;
- `20px`: cards editoriais maiores;
- `9999px`: pills, badges e divisores.

Borda padrão:

```css
border: 1px solid rgba(32, 1, 64, 0.14);
```

Sombra padrão:

```css
box-shadow: 0 18px 50px rgba(22, 0, 35, 0.14);
```

Usar sombra em:

- dropdowns;
- menus;
- modais;
- cards elevados;
- componentes flutuantes;
- planos destacados.

Evitar:

- glassmorphism;
- blur como linguagem principal;
- sombras duras;
- bordas grossas sem função;
- arredondamento em pill para todos os elementos.

### 4.7 Breakpoints

Tokens consolidados:

- mobile: até `720px`;
- tablet: até `1024px`;
- desktop: a partir de `1025px`.

Breakpoints podem ser refinados por componente quando houver necessidade real, mas devem ser documentados.

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

### 5.2 PT Serif

Usar em:

- H1;
- H2 de seção;
- títulos editoriais;
- títulos de cards institucionais;
- títulos de planos ou produtos;
- blocos que precisam transmitir autoridade.

Não usar em:

- botões;
- navegação;
- campos;
- labels;
- texto longo;
- mensagens de sistema;
- tabelas operacionais;
- dashboards densos.

O CSS solicita PT Serif com peso 700. Confirmar que esse peso está carregado. Não depender de bold sintético em novas implementações.

### 5.3 Montserrat

Usar em:

- corpo;
- botões;
- navegação;
- labels;
- FAQs;
- preços;
- formulários;
- metadados;
- cards funcionais;
- menus;
- descrições;
- tabelas;
- dashboards;
- ferramentas.

### 5.4 Escala recomendada

H1 editorial ou hero:

```css
font-family: var(--font-headline);
font-size: clamp(42px, 6vw, 60px);
font-weight: 700;
line-height: 0.98;
letter-spacing: 0;
```

Page title:

```css
font-family: var(--font-headline);
font-size: clamp(38px, 5vw, 58px);
font-weight: 700;
line-height: 1.02;
letter-spacing: 0;
```

H2 de seção:

```css
font-family: var(--font-headline);
font-size: clamp(34px, 4vw, 54px);
font-weight: 700;
line-height: 1.05;
letter-spacing: 0;
color: #170030;
```

Título editorial de card:

```css
font-family: var(--font-headline);
font-size: clamp(28px, 3vw, 42px);
font-weight: 700;
line-height: 1.08;
letter-spacing: 0;
```

Título funcional de card:

```css
font-family: var(--font-brand);
font-size: 22px;
font-weight: 700;
line-height: 1.25;
letter-spacing: 0;
```

Body grande:

```css
font-family: var(--font-brand);
font-size: clamp(18px, 1.6vw, 21px);
font-weight: 400;
line-height: 1.55;
```

Body padrão:

```css
font-family: var(--font-brand);
font-size: 16px;
font-weight: 400;
line-height: 1.55;
```

Body pequeno:

```css
font-family: var(--font-brand);
font-size: 14px;
font-weight: 400;
line-height: 1.5;
```

Overline:

```css
font-family: var(--font-brand);
font-size: 13px;
font-weight: 700;
line-height: 1.2;
letter-spacing: 0.08em;
text-transform: uppercase;
```

### 5.5 Regras tipográficas

- não usar tracking negativo em títulos serifados;
- manter line-height fechado apenas em títulos grandes;
- evitar parágrafos longos ocupando o container inteiro;
- limitar headings centrais a aproximadamente `820px`;
- usar `strong` para ênfase moderada;
- reservar caixa alta a overlines, badges e labels;
- não usar mais de três pesos diferentes na mesma seção;
- não usar bold excessivo;
- não centralizar parágrafos longos;
- não inserir quebras `<br>` rígidas sem necessidade;
- se houver quebra editorial, ela deve ser responsiva;
- texto de botão deve caber sem esmagar padding.

---

## 6. Layout System

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

- largura máxima de `1200px`;
- gutter mínimo de `20px` por lado;
- alinhamento central;
- seções full-bleed podem ter fundo de largura total;
- conteúdo interno deve alinhar ao container;
- não criar containers independentes com larguras arbitrárias.

### 6.2 Seções

Padrão:

```css
.section {
  padding: clamp(56px, 7vw, 92px) 0;
}
```

O espaço negativo faz parte da identidade. Não reduzir seções apenas para mostrar mais conteúdo acima da dobra.

### 6.3 Cabeçalho de seção

```css
.section-heading {
  text-align: center;
  max-width: 820px;
  margin: 0 auto 32px;
}
```

Anatomia recomendada:

1. overline opcional;
2. H2;
3. divisor dourado opcional;
4. supporting copy.

Divisor dourado:

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

### 6.4 Grid

Usar grids previsíveis:

- 1 coluna em mobile;
- 2 colunas em tablet quando houver espaço;
- 3 ou 4 colunas em desktop para cards;
- colunas assimétricas apenas quando a hierarquia justificar.

Exemplos:

```css
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

@media (max-width: 1024px) {
  .grid-3 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .grid-3 {
    grid-template-columns: 1fr;
  }
}
```

### 6.5 Fundos

Hero ou bloco escuro institucional:

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
- atmosfera editorial;
- contraste alto;
- ausência de neon.

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

A textura deve permanecer sutil.

Alternar entre:

- branco texturizado;
- soft lilás;
- roxo escuro;
- bloco branco elevado.

Não alternar cores sem função.

### 6.6 Estrutura global

Tokens consolidados:

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

---

## 7. Component Library

Cada componente deve documentar objetivo, anatomia, uso, variantes, estados e acessibilidade. Componentes compartilhados devem ser alterados com cuidado, verificando todas as telas impactadas.

### 7.1 Button

Objetivo: executar ação, iniciar fluxo, enviar formulário ou navegar para destino prioritário.

Anatomia:

- label específico;
- ícone opcional;
- estado visual;
- foco visível;
- loading quando assíncrono.

Primário:

```css
background: #ff2759;
color: #fff;
min-height: 48px;
padding: 0 24px;
border-radius: 8px;
font-family: var(--font-brand);
font-weight: 700;
```

Hover:

```css
background: #d6224c;
```

Variantes:

- primary;
- secondary;
- outline on dark;
- outline on light;
- ghost;
- icon-only;
- destructive, apenas quando necessário e com critério.

Estados obrigatórios:

- default;
- hover;
- focus-visible;
- active;
- disabled;
- loading, quando assíncrono.

Regras:

- disabled não pode depender apenas de cor;
- botão com ícone sem texto precisa de `aria-label`;
- usar `<button>` para ação e `<a>` para navegação;
- evitar CTAs genéricos.

Textos preferidos:

- Explorar carreiras;
- Começar pelo ENAM;
- Conhecer o NDCJ;
- Conhecer o NDP;
- Garantir minha vaga;
- Falar com a equipe;
- Ver resposta;
- Abrir relatório;
- Salvar plano.

Evitar:

- Clique aqui;
- Saiba mais;
- Ver mais;
- Continuar, quando existir termo mais específico;
- Acessar, quando o destino puder ser nomeado.

### 7.2 Card

Objetivo: agrupar conteúdo relacionado em uma unidade escaneável.

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
- carreira;
- métrica;
- plano;
- artigo;
- ferramenta.

Regras:

- fundo branco ou soft;
- borda sutil;
- sombra suave apenas quando houver elevação real;
- padding generoso;
- título claro;
- descrição específica;
- card inteiro clicável quando representar navegação única;
- hover sutil;
- foco no link ou controle principal.

Evitar:

- vários CTAs competindo;
- badges em excesso;
- imagem repetida em múltiplos cards;
- conteúdo sem hierarquia;
- card dentro de card.

### 7.3 Input e Textarea

Objetivo: coletar dados com clareza e baixo atrito.

Anatomia:

- label visível;
- campo;
- placeholder opcional;
- texto de ajuda opcional;
- mensagem de erro ou sucesso;
- estado disabled ou readonly quando aplicável.

Regras:

- placeholder não substitui label;
- usar `aria-describedby` para ajuda e erro;
- erro não depende apenas de vermelho;
- altura mínima de toque de `44px`;
- foco visível;
- mensagens específicas;
- prevenção de envio duplicado.

Estados:

- default;
- hover;
- focus;
- filled;
- error;
- success;
- disabled;
- readonly;
- loading, quando aplicável.

### 7.4 Select e Combobox

Objetivo: permitir escolha entre opções controladas.

Usar select nativo quando a lista for simples. Usar combobox apenas quando houver busca, listas longas ou necessidade operacional real.

Regras:

- label visível;
- opção atual clara;
- navegação por teclado;
- Escape fecha menu customizado;
- estados de erro e disabled;
- menu não pode ser cortado por containers;
- opções devem ter labels compreensíveis.

### 7.5 Accordion

Objetivo: revelar conteúdo secundário sem alongar excessivamente a página.

Anatomia:

- pergunta ou título;
- botão ocupando o cabeçalho inteiro;
- ícone de expansão;
- painel;
- resposta.

Semântica:

```html
<button
  aria-expanded="false"
  aria-controls="panel-id"
>
```

Regras:

- todo o cabeçalho clicável;
- não depender apenas do ícone;
- resposta em Montserrat;
- cor muted para texto auxiliar;
- animação suave;
- reduced motion respeitado;
- comportamento de item único ou múltiplos itens deve ser consistente.

FAQ deve responder dúvidas reais e específicas. Não copiar perguntas irrelevantes entre produtos.

### 7.6 Badge

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
- não transformar badge em decoração repetitiva;
- dourado deve ser reservado a autoridade, premium ou recomendação.

### 7.7 Modal e Dialog

Objetivo: solicitar decisão ou exibir fluxo temporário sem trocar de página.

Regras:

- usar `role="dialog"` ou elemento semântico equivalente;
- associar título com `aria-labelledby`;
- prender foco dentro do modal;
- fechar com Escape quando seguro;
- retornar foco ao acionador;
- incluir botão de fechar acessível;
- não usar modal para conteúdo longo que deveria ser página.

### 7.8 Hero e Page Header

Objetivo: introduzir contexto, proposta principal e ação prioritária quando a página exigir entrada editorial.

Hero é componente, não obrigação. Ferramentas, dashboards e áreas internas podem usar cabeçalho funcional compacto.

Anatomia típica:

- overline opcional;
- H1;
- divisor opcional;
- supporting copy;
- ações;
- imagem ou fundo institucional opcional.

Layout consolidado para hero editorial:

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

Usar quando:

- a página precisa de posicionamento editorial;
- existe proposta comercial ou institucional;
- a primeira dobra precisa orientar decisão.

Evitar quando:

- a interface é uma ferramenta;
- o usuário já está em fluxo operacional;
- a tela precisa priorizar dados, filtros ou tarefas.

### 7.9 Table

Objetivo: comparar dados estruturados.

Regras:

- usar `<table>` para dados tabulares reais;
- cabeçalhos claros;
- alinhamento consistente;
- ordenação e filtros quando necessário;
- estados vazios;
- overflow horizontal controlado em mobile;
- não usar tabela para layout.

### 7.10 Breadcrumb

Objetivo: mostrar localização e permitir retorno hierárquico.

Regras:

- usar em páginas profundas;
- labels curtos;
- último item representa página atual;
- incluir `aria-current="page"` no item atual;
- não substituir navegação principal.

### 7.11 Progress

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

### 7.12 Tabs

Objetivo: alternar visões relacionadas no mesmo contexto.

Regras:

- usar quando os painéis forem paralelos;
- navegação por teclado com setas quando implementado como tabs ARIA;
- indicar tab ativa;
- não usar tabs para esconder conteúdo essencial de SEO em páginas públicas sem critério.

### 7.13 Timeline

Objetivo: representar sequência temporal, etapas de curso, cronograma ou processo.

Regras:

- cada etapa precisa de título;
- datas devem ser verificadas;
- status visual deve ter texto;
- mobile deve manter leitura linear.

### 7.14 Empty State

Objetivo: orientar o usuário quando não houver dados, resultados ou conteúdo.

Anatomia:

- título curto;
- explicação objetiva;
- ação recomendada quando existir;
- ícone discreto opcional.

Evitar tom informal excessivo. Empty state deve ajudar, não decorar.

### 7.15 Tooltip

Objetivo: explicar controle, abreviação ou metadado auxiliar.

Regras:

- não conter informação essencial;
- funcionar com teclado e hover;
- manter texto curto;
- não usar para mensagens de erro;
- não esconder CTAs dentro de tooltip.

### 7.16 Header e navegação

Objetivo: orientar deslocamento global e expor ações de alto valor.

Anatomia em páginas comerciais ou institucionais:

- topbar rosa de `5px`;
- fundo roxo escuro;
- logo;
- navegação principal;
- portal;
- CTA principal.

Regras:

- altura desktop consolidada: `80px`;
- logo alinhado ao container;
- links em Montserrat;
- ação principal em rosa;
- dropdown em roxo escuro;
- estado ativo destacado;
- foco visível;
- navegação por teclado;
- mobile com menu colapsado;
- dropdown deve fechar com Escape;
- não depender apenas de hover.

Ferramentas e áreas internas podem usar navegação compacta, sidebar, app shell ou topbar funcional.

### 7.17 Footer

Objetivo: encerrar páginas públicas com contexto institucional, links úteis e informações legais.

Footer público deve conter:

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

Ferramentas e áreas internas podem usar footer mínimo ou omitir footer, desde que a navegação operacional continue clara.

### 7.18 Icons

Preferir Lucide para ícones funcionais.

```html
<svg
  class="lucide"
  aria-hidden="true"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
>
```

Regras:

- usar `currentColor`;
- ícones decorativos recebem `aria-hidden="true"`;
- botão apenas com ícone recebe `aria-label`;
- manter traço consistente;
- não misturar múltiplas bibliotecas no mesmo componente;
- não usar emoji como ícone da UI.

SVGs próprios podem representar:

- tribunais;
- balança;
- carreiras;
- documentos;
- plano de estudos;
- diagnóstico;
- execução guiada;
- resposta rápida.

Manter estilo linear, institucional e discreto.

### 7.19 Pricing

Objetivo: apresentar investimento, condições e comparação de planos.

Pricing é componente comercial, não fundação do Design System.

Anatomia:

1. overline;
2. título;
3. opções;
4. badge de destaque;
5. prazo;
6. preço;
7. condição;
8. desconto, se oficial;
9. CTA.

Regras:

- preço e condições devem ser oficiais e atuais;
- não copiar preço de outra página;
- plano recomendado pode usar borda dourada;
- badge dourado em pill;
- preço em rosa;
- explicar parcelamento e valor à vista;
- mostrar prazo de acesso;
- manter comparação justa;
- CTA principal no plano recomendado.

Nunca inventar:

- desconto;
- cashback;
- bônus;
- prazo;
- parcelamento;
- número de vagas;
- data de encerramento.

### 7.20 Career Card

Objetivo: apresentar uma carreira ou trilha com navegação clara.

Anatomia:

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

Regras:

- card inteiro clicável;
- usar `<article>`;
- imagem decorativa com `alt=""`;
- título claro;
- descrição específica;
- ícone circular sobreposto quando o padrão visual pedir;
- sombra suave;
- fundo branco;
- borda discreta;
- focus no link inteiro;
- hover sutil;
- não repetir imagens em cards diferentes.

Responsividade consolidada:

```html
sizes="
  (max-width: 720px) 78vw,
  (max-width: 1024px) 33vw,
  20vw
"
```

### 7.21 Carousel

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

---

## 8. Motion

### 8.1 Transição padrão

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

### 8.2 Entrada fade-up

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

### 8.3 Hover, focus e active

- hover deve confirmar interatividade sem deslocar layout;
- focus-visible deve ser mais evidente que hover;
- active pode escurecer, comprimir levemente ou reduzir opacidade;
- componentes não devem depender de movimento para comunicar estado.

### 8.4 Loading

Usar loading quando a ação for assíncrona.

Regras:

- impedir envio duplicado;
- preservar tamanho do botão;
- comunicar progresso com texto ou indicador;
- não deixar layout saltar;
- não esconder erro.

### 8.5 Disabled

Disabled deve comunicar indisponibilidade com:

- opacidade ou cor;
- cursor adequado quando aplicável;
- bloqueio real de interação;
- explicação quando a razão não for óbvia.

### 8.6 Reduced motion

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
- não tornar informação dependente de animação.

Não usar:

- autoplay;
- bounce;
- parallax forte;
- animações contínuas;
- rotação decorativa;
- transições acima de 1 segundo;
- movimento que altere layout;
- animação de texto permanente.

---

## 9. Content

### 9.1 Tom

O texto deve ser:

- claro;
- direto;
- jurídico;
- confiante;
- editorial;
- específico;
- sem exagero comercial.

Evitar:

- informalidade excessiva;
- promessas absolutas;
- urgência artificial;
- jargão sem explicação;
- frases genéricas de marketing;
- afirmações sem fonte.

### 9.2 Headings

Regras:

- um H1 por página;
- H2 por seção;
- H3 em cards ou subseções;
- não usar heading apenas por aparência;
- título deve explicar o conteúdo, não apenas vender.

### 9.3 Subtítulos e supporting copy

Supporting copy deve:

- contextualizar;
- reduzir ambiguidade;
- explicar público, método ou benefício;
- manter largura confortável;
- evitar parágrafo longo centralizado.

### 9.4 CTAs

CTA deve ser específico e orientado à ação real.

Bom:

- Conhecer o curso;
- Montar plano de estudos;
- Baixar relatório;
- Falar com a equipe;
- Ver cronograma;
- Abrir dashboard.

Ruim:

- Clique aqui;
- Saiba mais;
- Ver mais;
- Continuar sem contexto.

### 9.5 Links

- texto descritivo;
- evitar "clique aqui";
- evitar nomes diferentes para o mesmo destino;
- verificar links externos;
- indicar destino externo quando necessário.

### 9.6 SEO e conteúdo público

- responder intenção de busca;
- usar nomes oficiais;
- manter parágrafos curtos;
- usar FAQ estruturado quando compatível;
- imagens com dimensões, alt correto e formato otimizado;
- evitar duplicar conteúdo irrelevante entre produtos.

---

## 10. Accessibility

### 10.1 Semântica

- um H1 por página;
- hierarquia correta;
- `<nav>` para navegação;
- `<main>` para conteúdo;
- `<section>` com heading;
- `<article>` para cards independentes;
- `<button>` para ações;
- `<a>` para navegação;
- não usar `<div>` clicável.

### 10.2 Teclado

Suportar:

- Tab;
- Shift+Tab;
- Enter;
- Espaço;
- Escape;
- setas quando o padrão do componente exigir.

### 10.3 Focus visible

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

### 10.4 ARIA

Usar ARIA para complementar semântica, não para corrigir markup inadequado.

Regras:

- `aria-label` em botões apenas com ícone;
- `aria-expanded` em disclosure, menu e accordion;
- `aria-controls` quando houver painel controlado;
- `aria-current="page"` em item atual;
- `aria-describedby` para ajuda e erro em campos;
- não usar roles desnecessárias quando HTML nativo resolve.

### 10.5 Contraste

Atender WCAG AA:

- texto normal: 4.5:1;
- texto grande: 3:1;
- componentes gráficos essenciais: 3:1.

### 10.6 Touch target

Área mínima aproximada: `44px` por `44px`.

### 10.7 Skip link

Manter "Pular para o conteúdo" como primeiro link focável em páginas com navegação global.

### 10.8 Imagens

Imagem decorativa:

```html
<div aria-hidden="true">
  <img alt="">
</div>
```

Imagem informativa deve ter alt descritivo e objetivo.

### 10.9 Movimento

Respeitar `prefers-reduced-motion`. Nenhuma informação pode depender exclusivamente de animação.

---

## 11. Responsividade

### 11.1 Princípio

Mobile não é desktop reduzido. A interface deve reorganizar prioridade, densidade e fluxo.

Revisar:

- header;
- navegação;
- hero ou page header;
- cards;
- grids;
- tabelas;
- formulários;
- CTAs;
- dashboards;
- modais.

### 11.2 Desktop

Desktop pode usar:

- grids de 3 ou 4 colunas;
- navegação horizontal;
- tabelas completas;
- painéis lado a lado;
- espaço negativo amplo;
- imagens editoriais maiores.

### 11.3 Tablet

Tablet deve:

- reduzir colunas;
- preservar padding;
- evitar textos espremidos;
- manter controles confortáveis;
- considerar orientação retrato e paisagem.

### 11.4 Mobile

Mobile deve:

- priorizar leitura linear;
- empilhar CTAs quando necessário;
- usar botões full-width quando fizer sentido;
- evitar altura fixa em hero;
- esconder ou reordenar imagens que competem com a tarefa;
- permitir overflow horizontal controlado em tabelas;
- remover quebras manuais de desktop.

### 11.5 Cards e grids

- uma coluna para cards grandes;
- duas colunas apenas com largura suficiente;
- carrossel apenas quando o componente existente exigir;
- preservar padding interno;
- não reduzir tipografia a ponto de perder leitura.

### 11.6 Tabelas

Em mobile:

- usar scroll horizontal controlado;
- ou transformar linhas em cards quando a comparação não exigir colunas simultâneas;
- manter cabeçalhos ou labels visíveis;
- não cortar conteúdo.

### 11.7 Quebras manuais

Quebras como `.desktop-break` devem ser removidas ou ocultadas em mobile. Não depender de `<br>` para layout responsivo.

---

## 12. Tipos de Página

Templates são exemplos de composição. Eles não definem o Design System. Cada template deve reutilizar tokens, layout, componentes, conteúdo e acessibilidade já descritos.

### 12.1 Landing Page

Usar para campanha, produto ou oferta específica.

Pode conter:

- hero ou page header;
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

Não criar identidade visual independente.

### 12.2 Página Institucional

Usar para apresentar marca, história, método, equipe ou posicionamento.

Pode conter:

- page hero;
- história;
- proposta;
- método;
- números verificáveis;
- equipe;
- CTA;
- footer.

### 12.3 Página de Curso

Usar para produto educacional específico.

Pode conter:

- page hero;
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

### 12.4 Blog

Usar para listagem editorial.

Deve priorizar:

- categorias;
- busca;
- cards de artigo;
- metadados;
- paginação;
- leitura limpa;
- SEO.

### 12.5 Página de Artigo

Usar para conteúdo editorial longo.

Deve conter:

- H1 claro;
- autor ou fonte quando aplicável;
- data;
- corpo com largura confortável;
- headings coerentes;
- links relacionados;
- imagens otimizadas;
- compartilhamento quando fizer sentido.

### 12.6 Dashboard

Usar para acompanhamento, métricas, desempenho ou operação.

Deve priorizar:

- tarefas principais;
- métricas;
- filtros;
- tabelas;
- estados vazios;
- carregamento;
- densidade controlada;
- clareza operacional.

Não precisa de hero comercial.

### 12.7 Ferramenta, Planner ou Tracker

Usar para execução de tarefa.

Deve conter:

- cabeçalho funcional;
- estado atual;
- controles principais;
- feedback;
- salvamento ou exportação quando aplicável;
- acessibilidade de formulário;
- responsividade orientada ao uso.

### 12.8 Portal ou Área Interna

Usar para ambiente autenticado.

Pode usar:

- app shell;
- sidebar;
- topbar compacta;
- breadcrumbs;
- tabs;
- filtros;
- tabelas;
- cards de status.

### 12.9 Página de Login

Deve conter:

- marca;
- formulário simples;
- labels visíveis;
- erro claro;
- recuperação de acesso;
- termos ou privacidade quando aplicável;
- segurança sem excesso de texto.

### 12.10 Página de Erro

Deve conter:

- mensagem clara;
- explicação breve;
- ação de retorno;
- contato ou ajuda quando aplicável;
- tom sóbrio.

### 12.11 Página de Documentação

Deve priorizar:

- navegação lateral ou índice;
- headings estáveis;
- exemplos;
- blocos de código;
- busca quando necessário;
- versão ou contexto;
- leitura longa confortável.

---

## 13. Application and Tool Pages

Ferramentas internas, planners, trackers, dashboards e aplicações web não precisam utilizar a estrutura completa de uma landing page.

Devem preservar:

- tokens;
- tipografia;
- componentes;
- cores;
- acessibilidade;
- responsividade;
- linguagem visual.

Podem omitir:

- hero comercial;
- pricing;
- prova social;
- CTA de venda;
- footer institucional completo;
- navegação comercial.

A função da ferramenta sempre prevalece sobre a estrutura comercial.

Regras complementares:

- usar densidade maior apenas quando a tarefa exigir;
- preferir Montserrat em superfícies operacionais;
- reservar PT Serif para títulos de página ou momentos editoriais;
- manter ações principais em rosa;
- usar roxo escuro para navegação ou áreas de identidade;
- exibir estados vazios, loading, erro e sucesso;
- proteger layout contra transbordamento de tabelas, labels e botões;
- não transformar ferramenta em landing page.

---

## 14. Business Rules

Regras de negócio devem ficar separadas das regras visuais. Elas impedem que uma página visualmente correta fique comercial, acadêmica ou juridicamente errada.

### 14.1 Produtos e carreiras

Não alterar sem confirmação:

- nomes;
- combinações;
- destinos;
- escopo;
- etapa;
- público;
- promessas;
- condições.

Carreiras oficiais já usadas:

1. Magistratura Federal;
2. Magistratura Estadual;
3. Magistratura Federal e Estadual;
4. Procuradorias;
5. Magistratura Federal e MPF;
6. Magistratura Estadual e MPE;
7. Magistratura do Trabalho e MPT;
8. Defensorias.

### 14.2 ENAM

O ENAM se relaciona às magistraturas. Não assumir aplicação automática a Procuradorias, Defensorias ou outros produtos.

Regras, datas, cashback e condições precisam de fonte oficial atual.

### 14.3 Núcleo Duro

Existem ao menos:

- NDCJ: Núcleo Duro Carreiras Jurídicas;
- NDP: Núcleo Duro Procuradorias.

Núcleo Duro não é sinônimo de curso Regular.

### 14.4 Conteúdo e acesso

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

### 14.5 Preço e condições

Sempre verificar:

- produto;
- vigência;
- parcelamento;
- Pix;
- desconto;
- acesso;
- bônus;
- checkout.

Não inventar:

- preço;
- prazo;
- desconto;
- parcelamento;
- bônus;
- número de vagas;
- data de encerramento.

### 14.6 Resultados e depoimentos

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

### 14.7 WhatsApp e contato

"Falar com a equipe" deve usar link oficial. Não criar números divergentes.

### 14.8 Portais

Distinguir:

- Portal de Entrada;
- Portal da Pós.

Não substituir um pelo outro.

---

## 15. Auditoria

Esta seção orienta agentes ao auditar páginas, componentes, ferramentas ou fluxos.

### 15.1 Escala de conformidade

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

### 15.2 Severidade

Cada problema encontrado deve receber severidade:

- Crítico: impede uso, viola regra legal/comercial relevante, quebra fluxo principal ou cria risco grave de acessibilidade;
- Alto: prejudica conversão, compreensão, navegação, responsividade ou acessibilidade importante;
- Médio: desalinhamento perceptível com o Design System ou problema que afeta parte dos usuários;
- Baixo: refinamento visual, inconsistência pequena ou melhoria de manutenção.

### 15.3 Categorias de auditoria

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

### 15.4 Formato recomendado

Usar tabela:

| Requisito | Status | Severidade | Evidência | Recomendação |
| --- | --- | --- | --- | --- |
| Usa tokens oficiais | Atendido | N/A | Cores derivam de tokens | Manter |
| Pricing presente em ferramenta interna | N/A | N/A | Tela não é comercial | Nenhuma |
| Botão sem focus visível | Não atendido | Alto | Navegação por teclado sem indicação | Adicionar `focus-visible` |

### 15.5 Resumo final obrigatório

Ao final, gerar resumo com:

- Visual;
- Código;
- Acessibilidade;
- Responsividade;
- Design System;
- Score Geral.

Score sugerido:

- 90-100: excelente aderência;
- 75-89: bom, com ajustes;
- 60-74: parcial, requer correções;
- abaixo de 60: desalinhado ou arriscado.

O score deve considerar apenas requisitos aplicáveis. Itens `N/A` não reduzem pontuação.

### 15.6 Checklist base para agentes

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

---

## 16. Implementação

### 16.1 Tokens

Reutilizar tokens globais. Não hardcodar a mesma cor, espaço, sombra ou radius em vários componentes.

### 16.2 Componentes

Criar variantes controladas.

Bom:

- `Button`;
- `ButtonPrimary`;
- `ButtonOutline`;
- `SectionHeading`;
- `Card`;
- `CareerCard`;
- `PricingCard`;
- `Accordion`;
- `PageHeader`;
- `Tabs`;
- `Table`.

Ruim:

- `HomePinkButton`;
- `DefensoriaPinkButton`;
- `NdcjPinkButton`;
- `OtherPinkButton`.

### 16.3 Dados

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

### 16.4 Alterações em componentes compartilhados

Antes de alterar:

- verificar todas as páginas impactadas;
- revisar responsividade;
- revisar estados;
- revisar acessibilidade;
- não corrigir uma página quebrando outras.

### 16.5 Figma e ativos

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

### 16.6 Fotografia e imagens

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

Estilo:

- cinematográfico;
- tons quentes;
- sombras profundas;
- contraste controlado;
- fundo desfocado;
- roupa formal;
- expressão séria;
- composição com espaço para texto.

Evitar:

- stock photo genérica;
- coworking;
- pessoa sorrindo para notebook;
- aperto de mãos;
- pose corporativa artificial;
- martelo de juiz como clichê dominante;
- anatomia incorreta em imagens geradas;
- texto embutido na imagem;
- repetição da mesma foto.

Performance:

- definir dimensões;
- evitar CLS;
- lazy load abaixo da dobra;
- usar `sizes`;
- otimizar formato;
- priorizar imagem crítica;
- usar `object-fit: cover`;
- ajustar `object-position`.

### 16.7 Redes sociais

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

## 17. O Que Fazer

- usar PT Serif em títulos editoriais;
- usar Montserrat na interface;
- respeitar container de `1200px`;
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
- preservar os dois portais quando aplicáveis;
- marcar regras não aplicáveis como `N/A` em auditorias.

---

## 18. O Que Não Fazer

- não usar glassmorphism;
- não usar azul SaaS como identidade;
- não usar neon;
- não usar sombras duras;
- não arredondar tudo;
- não usar sans-serif em todos os títulos editoriais;
- não usar serif em botões;
- não usar fotos genéricas;
- não repetir imagens;
- não misturar bibliotecas de ícones;
- não inventar preço;
- não inventar prazo;
- não inventar resultado;
- não prometer aprovação;
- não criar identidade paralela;
- não reduzir padding apenas para encaixar conteúdo;
- não usar autoplay;
- não remover Portal de Entrada ao adicionar Portal da Pós;
- não alterar produto, carreira ou regra sem confirmação;
- não tratar ausência de hero, pricing ou footer comercial como erro em ferramentas.

---

## 19. Estado Deste Documento

Valores oficialmente confirmados pelo site:

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

Valores consolidados que podem ser refinados com inspeção adicional:

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
