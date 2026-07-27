# Tipografia

## Famílias oficiais

- **PT Serif**, fallback `Georgia, "Times New Roman", serif`: títulos editoriais e momentos de autoridade.
- **Montserrat**, fallback `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`: corpo, labels, CTA, metadados e identificação.

PT Serif 700 é o peso solicitado pela identidade, mas **Decisão pendente:** confirmar os arquivos e licenças dos pesos efetivamente disponíveis no ambiente de produção. Não afirmar carregamento pela simples seleção do nome. Fontes alternativas são apenas fallbacks técnicos; não são variantes criativas.

## Hierarquia para Instagram

| Papel | Família | Peso | Tamanho | Line-height | Tracking |
| --- | --- | ---: | --- | --- | --- |
| Título de capa | PT Serif | 700 | Decisão pendente | 0,98–1,05 | 0 |
| Título interno | PT Serif | 700 | Decisão pendente | 1,02–1,08 | 0 |
| Subtítulo | Montserrat | Decisão pendente | Decisão pendente | 1,25 | 0 |
| Corpo | Montserrat | regular | Decisão pendente | 1,50–1,55 | 0 |
| Legenda/metadado | Montserrat | regular | Decisão pendente | 1,50 | 0 |
| Label | Montserrat | 700 | Decisão pendente | 1,20 | `0.08em` |
| CTA | Montserrat | 700 | Decisão pendente | 1,20–1,25 | 0 |
| Professor | Montserrat | 700/regular | Decisão pendente | 1,25 | 0 |
| Número do slide | Montserrat | 700 | Decisão pendente | 1,20 | 0 |

As relações, famílias e line-heights vêm da escala oficial; os tamanhos em pixels para pranchetas sociais não estão definidos e devem ser validados por teste em tela reduzida. Não transportar automaticamente tamanhos de web para Instagram.

## Composição

- máximo recomendado: capa com 3 linhas; título interno com 2 linhas; subtítulo com 3 linhas; corpo com parágrafos curtos;
- **Decisão pendente:** limites de caracteres por papel após teste com Montserrat e PT Serif reais;
- quebrar por unidade de sentido; não deixar artigo, preposição ou número isolado quando houver alternativa;
- não inserir quebra para formar desenho que prejudique leitura;
- destaque com `strong`/peso 700, rosa controlado ou bloco de citação; usar um método por trecho;
- caixa alta somente em label, badge ou overline curto;
- itálico apenas em citação, título de obra ou convenção jurídica confirmada;
- no máximo três pesos na peça; não usar bold em parágrafos inteiros;
- alinhamento à esquerda é padrão; central somente em capa, citação curta ou CTA quando o template definir;
- não centralizar corpo longo; não justificar texto; não usar tracking negativo em serifada.

A validação reduzida é obrigatória: visualizar a peça no tamanho aproximado de exibição em telefone e reprovar texto que exija zoom, perca contraste, colida ou forme viúvas/orfãs problemáticas.

Práticas proibidas: esticar fonte, usar fonte externa, contorno/sombra dura no texto, mais de duas famílias, corpo em PT Serif, botão/CTA em PT Serif, excesso de caixa alta ou reduzir tamanho para fazer conteúdo excessivo caber.
