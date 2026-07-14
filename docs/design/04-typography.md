---
title: "04 - Tipografia"
version: "2.1"
---

# Tipografia

## Famílias Oficiais

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

## PT Serif

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

Observação: a implementação atual solicita PT Serif com peso 700. Não afirmar que a fonte está carregada sem verificar. Ver [Implementação Atual](17-current-implementation.md).

## Montserrat

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

## Escala

### H1 Editorial Ou Hero

```css
font-family: var(--font-headline);
font-size: clamp(42px, 6vw, 60px);
font-weight: 700;
line-height: 0.98;
letter-spacing: 0;
```

### Page Title

```css
font-family: var(--font-headline);
font-size: clamp(38px, 5vw, 58px);
font-weight: 700;
line-height: 1.02;
letter-spacing: 0;
```

### H2 De Seção

```css
font-family: var(--font-headline);
font-size: clamp(34px, 4vw, 54px);
font-weight: 700;
line-height: 1.05;
letter-spacing: 0;
color: #170030;
```

### Título Editorial De Card

```css
font-family: var(--font-headline);
font-size: clamp(28px, 3vw, 42px);
font-weight: 700;
line-height: 1.08;
letter-spacing: 0;
```

### Título Funcional De Card

```css
font-family: var(--font-brand);
font-size: 22px;
font-weight: 700;
line-height: 1.25;
letter-spacing: 0;
```

### Body

```css
.body-lg {
  font-family: var(--font-brand);
  font-size: clamp(18px, 1.6vw, 21px);
  line-height: 1.55;
}

.body-md {
  font-family: var(--font-brand);
  font-size: 16px;
  line-height: 1.55;
}

.body-sm {
  font-family: var(--font-brand);
  font-size: 14px;
  line-height: 1.5;
}
```

### Overline

```css
font-family: var(--font-brand);
font-size: 13px;
font-weight: 700;
line-height: 1.2;
letter-spacing: 0.08em;
text-transform: uppercase;
```

## Regras

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

## Arquivos Relacionados

- [Tokens](03-tokens.md)
- [Conteúdo](08-content.md)
- [Responsividade](10-responsive.md)
