---
title: "03 - Tokens"
version: "2.1"
---

# Tokens

## Papel

Tokens são a base visual reutilizável do Design System. Este arquivo documenta valores conhecidos e preservados da versão 2.0. Valores específicos confirmados por implementação ficam em [Implementação Atual](17-current-implementation.md).

## Cores

```yaml
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
```

## Tokens CSS Base

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

## Uso Das Cores

### Rosa Principal: `#FF2759`

Usar em CTA principal, ações importantes, ícones interativos, estados ativos, elementos de alta prioridade, preços em destaque e sinalização de marca.

Não usar como fundo predominante, cor de grandes seções, texto corrido ou decoração repetida.

### Rosa Escuro: `#D6224C`

Usar em hover, pressed, estados densos do CTA e detalhes controlados.

### Roxo Institucional: `#200140`

Usar em fundos escuros, ícones institucionais, bordas, detalhes, títulos secundários, superfícies de dropdown e navegação.

### Roxo Escuro: `#170030`

Usar em header, dropdown, hero, blocos de alto contraste, rodapé e navegação ativa em fundos escuros.

### Texto Principal: `#160023`

Usar em títulos, textos principais, labels, preços e informações críticas em superfícies claras.

### Texto Secundário: `#675F78`

Usar em descrições, supporting copy, metadados, respostas de FAQ e textos auxiliares.

### Dourado: `#D6B56D`

Usar com moderação em divisores, badges premium, contornos de destaque, detalhes jurídicos e pequenas sinalizações de autoridade.

Não usar em parágrafos, grandes fundos, CTAs principais ou texto pequeno com contraste baixo.

## Proporção De Cor

Em interfaces claras:

- 65-80% superfícies claras;
- 10-20% roxo ou escuro;
- 5-10% rosa;
- menos de 5% dourado.

Rosa deve significar ação ou destaque. Dourado deve significar autoridade, refinamento ou recomendação.

## Espaçamento

Escala baseada em 4px:

- `4px`;
- `8px`;
- `16px`;
- `24px`;
- `32px`;
- `48px`;
- `64px`;
- `clamp(56px, 7vw, 92px)` para seções.

Evitar valores arbitrários, salvo quando já existirem em componente oficial ou houver motivo técnico documentado.

## Radius

- `0`: superfícies sem arredondamento;
- `4px`: controles pequenos;
- `8px`: botões e elementos interativos;
- `14px`: cards padrão;
- `20px`: cards editoriais maiores;
- `9999px`: pills, badges e divisores.

## Bordas E Sombras

Borda padrão:

```css
border: 1px solid rgba(32, 1, 64, 0.14);
```

Sombra padrão:

```css
box-shadow: 0 18px 50px rgba(22, 0, 35, 0.14);
```

Usar sombra em dropdowns, menus, modais, cards elevados, componentes flutuantes e planos destacados.

Evitar glassmorphism, blur como linguagem principal, sombras duras, bordas grossas sem função e arredondamento em pill para todos os elementos.

## Breakpoints

- mobile: até `720px`;
- tablet: até `1024px`;
- desktop: a partir de `1025px`.

Breakpoints podem ser refinados por componente quando houver necessidade real, mas devem ser documentados.

## Contraste

Atender WCAG AA:

- 4.5:1 para texto normal;
- 3:1 para texto grande;
- 3:1 para componentes gráficos essenciais.

## Arquivos Relacionados

- [Tipografia](04-typography.md)
- [Layout](05-layout.md)
- [Implementação Atual](17-current-implementation.md)
