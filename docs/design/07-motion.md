---
title: "07 - Motion"
version: "2.1"
---

# Motion

## Princípio

Motion deve confirmar estado, orientar foco e melhorar percepção de continuidade. Não deve decorar, distrair ou esconder informação.

## Transição Padrão

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

## Entrada Fade-Up

Padrão consolidado para elementos editoriais relevantes:

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

Aplicar apenas a:

- H1;
- overline;
- título de page header;
- divisor;
- elementos editoriais de destaque.

## Hover, Focus E Active

- hover confirma interatividade sem deslocar layout;
- focus-visible deve ser mais evidente que hover;
- active pode escurecer, comprimir levemente ou reduzir opacidade;
- componentes não devem depender de movimento para comunicar estado.

## Loading

Usar loading quando a ação for assíncrona.

Regras:

- impedir envio duplicado;
- preservar tamanho do botão;
- comunicar progresso com texto ou indicador;
- não deixar layout saltar;
- não esconder erro.

## Disabled

Disabled deve comunicar indisponibilidade com:

- opacidade ou cor;
- cursor adequado quando aplicável;
- bloqueio real de interação;
- explicação quando a razão não for óbvia.

## Reduced Motion

```css
@media (prefers-reduced-motion: no-preference) {
  /* animações */
}
```

Quando o usuário preferir menos movimento:

- remover translate;
- remover animação de entrada;
- reduzir transições;
- manter conteúdo visível;
- não tornar informação dependente de animação.

## Não Usar

- autoplay;
- bounce;
- parallax forte;
- animações contínuas;
- rotação decorativa;
- transições acima de 1 segundo;
- movimento que altere layout;
- animação de texto permanente.
