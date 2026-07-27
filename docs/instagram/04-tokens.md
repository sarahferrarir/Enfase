# Tokens

## Cores oficiais

| Token | HEX | Função |
| --- | --- | --- |
| `color.background` | `#FFFFFF` | Fundo claro principal |
| `color.foreground` | `#160023` | Texto principal em claro |
| `color.primary` | `#FF2759` | CTA e destaque prioritário |
| `color.primary-hover` | `#D6224C` | Estado denso; não criar hover em imagem estática |
| `color.primary-deep` | `#370F18` | Apoio vermelho profundo |
| `color.primary-foreground` | `#FFFFFF` | Texto sobre rosa quando contraste aprovado |
| `color.purple` | `#200140` | Roxo institucional, fundo, ícone e detalhe |
| `color.purple-high` | `#3A0A6E` | Roxo de apoio e foco claro |
| `color.purple-dark` | `#170030` | Fundo institucional escuro |
| `color.ink` | `#160023` | Títulos e informação crítica |
| `color.muted` | `#675F78` | Texto secundário |
| `color.gold` | `#D6B56D` | Autoridade e divisor, com moderação |
| `color.line` | `#20014024` | Linha translúcida (alpha embutido) |
| `color.surface` | `#FFFFFF` | Superfície |
| `color.surface-soft` | `#F5F2F8` | Fundo claro alternativo |
| `color.surface-soft-2` | `#EEE8F4` | Fundo claro de apoio |
| `color.hero-start` | `#0D001B` | Gradiente escuro |
| `color.hero-stop-1` | `#12001F` | Gradiente escuro |
| `color.hero-stop-2` | `#15011C` | Gradiente escuro |
| `color.hero-stop-3` | `#100018` | Gradiente escuro |
| `color.hero-end` | `#09000F` | Gradiente escuro |
| `color.focus-light` | `#FFFFFF` | Foco em fundo escuro |
| `color.focus-dark` | `#3A0A6E` | Foco em fundo claro |

O brilho quente confirmado é `rgba(77, 36, 16, 0.42)` e só pode integrar o fundo escuro institucional. Proporção orientadora em composição clara: 65–80% claro, 10–20% roxo/escuro, 5–10% rosa e menos de 5% dourado.

## Combinações

Permitidas condicionadas à medição: `ink` sobre branco/soft; branco sobre roxo escuro; rosa como bloco de CTA com foreground aprovado; dourado apenas em detalhe sobre fundo que alcance contraste necessário. Proibidas: muted ou dourado quando falharem contraste; rosa como fundo predominante ou texto corrido; dourado em parágrafo, CTA principal ou fundo amplo; neon; cores fora da tabela.

Contraste mínimo WCAG AA: 4,5:1 para texto normal, 3:1 para texto grande e 3:1 para elemento gráfico essencial. “Texto grande” deve ser verificado pela equivalência tipográfica, não presumido pela prancheta.

## Estrutura

- espaçamento oficial: `4, 8, 16, 24, 32, 48, 64px`;
- raios: `0, 4, 8, 14, 20, 9999px`;
- borda: `1px solid rgba(32, 1, 64, 0.14)`;
- sombra: `0 18px 50px rgba(22, 0, 35, 0.14)`.

Raios: 4 em elementos pequenos, 8 em CTA, 14 em cards, 20 em blocos editoriais e 9999 somente em pills/badges/divisores. Sombra somente quando há elevação; evitar sombras duras, blur dominante e glassmorphism. Opacidades: somente as incorporadas em `line`, brilho quente, borda e sombra estão confirmadas; **Decisão pendente:** demais níveis.

**Decisão pendente:** tokens específicos de margem e grid social, dimensões dos componentes e escala de ícones.

Novo token só pode ser criado após recorrência comprovada, nome semântico, teste de contraste, aprovação humana e atualização deste arquivo e dos templates. Agentes não criam tokens durante uma publicação.
