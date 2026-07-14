---
title: "05 - Layout"
version: "2.1"
---

# Layout

## Container

```css
--container: min(100% - 40px, 1200px);
```

Equivalente:

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

## Seções

Padrão:

```css
.section {
  padding: clamp(56px, 7vw, 92px) 0;
}
```

O espaço negativo faz parte da identidade. Não reduzir seções apenas para mostrar mais conteúdo acima da dobra.

## Cabeçalho De Seção

Anatomia recomendada:

1. overline opcional;
2. H2;
3. divisor dourado opcional;
4. supporting copy.

Regra visual:

- alinhamento central quando a seção for editorial;
- alinhamento à esquerda quando a seção for operacional, densa ou parte de dashboard;
- largura de leitura controlada;
- divisor dourado apenas em títulos principais de seção, não em headings internos de cards.

## Grid

Usar grids previsíveis:

- 1 coluna em mobile;
- 2 colunas em tablet quando houver espaço;
- 3 ou 4 colunas em desktop para cards;
- colunas assimétricas apenas quando a hierarquia justificar.

Exemplo reutilizável:

```css
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}
```

## Fundos

Blocos escuros institucionais podem usar roxo quase preto, brilho quente central, profundidade e contraste alto. Não usar neon.

Seção clara institucional pode usar textura sutil quando disponível:

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

Alternar entre:

- branco texturizado;
- soft lilás;
- roxo escuro;
- bloco branco elevado.

Não alternar cores sem função.

## Fluxo Vertical

- páginas editoriais devem ter respiro amplo;
- páginas operacionais podem ser mais densas;
- cada seção deve ter início, conteúdo principal e encerramento claro;
- não comprimir padding apenas para encaixar mais conteúdo.

## Âncoras

Quando houver header fixo ou sticky, preservar margem de rolagem suficiente para que o conteúdo ancorado não fique oculto.

Valor atual aproximado documentado em [Implementação Atual](17-current-implementation.md): `104px`.

## Arquivos Relacionados

- [Tokens](03-tokens.md)
- [Responsividade](10-responsive.md)
- [Tipos de Página](11-page-types.md)
