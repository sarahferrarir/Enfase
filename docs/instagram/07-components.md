# Componentes

## Contrato comum

Nomes usam `Instagram/Nome` (logo preserva `Brand/Logo`); variantes usam `/Variant`; instâncias usam `cmp.nome.variante`. Dimensões e espaçamentos numéricos ficam definidos e bloqueados no template após as decisões de grid. **Decisão pendente:** medidas sociais exatas. Todos usam a escala de espaços, cores e tipografia oficiais. Estado padrão: `default`; `optional`, `empty`, `long-content` ou `with-image` apenas quando listado. Agentes alteram somente conteúdo e propriedades declaradas; nunca geometria, fonte, token, raio ou efeito.

## Biblioteca

### `Brand/Logo`

- Finalidade/estrutura: identificar autoria com o ativo oficial único.
- Conteúdo: imagem sem texto anexado; proporção original, área de proteção pendente.
- Cores/variantes/estados: arquivo original; `default` apenas.
- Uso: uma instância visível na peça conforme template. Não usar como marca-d'água, padrão, título, recortar, recolorir ou aplicar efeitos.
- Editável: escala proporcional dentro do tamanho bloqueado. Imutável: arquivo, proporção, cor e posição.

### `Instagram/CategoryLabel`

- Finalidade/estrutura: categoria curta em pill ou overline; texto único.
- Conteúdo: categoria confirmada; não frase promocional.
- Tipografia/cor: Montserrat 700, caixa alta, tracking `0.08em`; roxo, rosa ou dourado somente em combinação contrastante aprovada.
- Variantes/estados: `overline`, `pill`; `default`, `optional`. Não usar mais de uma categoria.
- Editável: texto e variante prevista. Imutável: padding, raio e estilo.

### `Instagram/TitleBlock`

- Finalidade/estrutura: ideia principal; título e destaque opcional.
- Conteúdo: título fiel, sem fato novo; limite de linhas de `05-typography.md`.
- Tipografia/cor: PT Serif 700; ink em claro ou branco em escuro.
- Variantes: `cover`, `internal`; estado `long-content` reprova se exceder caixa.
- Não usar para corpo; não reduzir fonte. Editável: texto/destaque autorizado.

### `Instagram/Subtitle`

- Finalidade/estrutura: contextualizar título em um bloco.
- Conteúdo: apoio fornecido, até três linhas recomendadas.
- Tipografia/cor: Montserrat; foreground ou muted com contraste.
- Variantes: `light`, `dark`; `optional`. Não duplicar o título.

### `Instagram/BodyText`

- Finalidade/estrutura: conteúdo principal em parágrafos/lista curta.
- Conteúdo: texto aprovado; sem interpretação nova.
- Tipografia/cor: Montserrat regular, line-height 1,50–1,55; ink/branco.
- Variantes: `paragraph`, `bullets`; `long-content` exige divisão/devolução.
- Não centralizar, justificar, comprimir ou usar PT Serif.

### `Instagram/CTA`

- Finalidade/estrutura: ação específica; label e ícone oficial opcional.
- Conteúdo: ação real e destino confirmado.
- Tipografia/cor: Montserrat 700; rosa principal prioritário; raio 8.
- Variantes: `primary`, `text`; `optional`. Em imagem estática não simular hover.
- Não usar “Clique aqui”, inventar link ou empilhar CTAs.

### `Instagram/Footer`

- Finalidade/estrutura: faixa recorrente com logo, número e/ou referência.
- Conteúdo: componentes filhos, sem slogan inventado.
- Cor: superfície oficial contrastante; borda padrão opcional.
- Variantes: `standard`, `final`; estado `default`.
- Posição e altura bloqueadas; não virar área decorativa.

### `Instagram/SlideNumber`

- Finalidade/estrutura: indicar sequência como `NN/NN`.
- Conteúdo: números reais, dois dígitos.
- Tipografia/cor: Montserrat 700; foreground ou branco.
- Variantes: `light`, `dark`; obrigatório em carrossel, opcional/ausente em post único.
- Não numerar errado, mudar posição ou competir com logo.

### `Instagram/ProfessorIdentification`

- Finalidade/estrutura: nome, cargo/titulação e curso opcionais em linhas separadas.
- Conteúdo: somente dados confirmados.
- Tipografia/cor: Montserrat 700 no nome, regular no apoio; alto contraste.
- Variantes: `compact`, `full`; `missing-data` bloqueia exportação quando identificação for essencial.
- Não inventar credencial nem cobrir o rosto.

### `Instagram/ImageContainer`

- Finalidade/estrutura: máscara com imagem e ponto focal.
- Conteúdo: foto autorizada, institucional, editorial ou IA identificada.
- Forma: raio 0, 14 ou 20 conforme template; sombra apenas se elevado.
- Variantes: `portrait`, `editorial`, `full-bleed`; `missing`, `approved`, `rights-pending`.
- Editável: imagem, crop e ponto focal. Imutável: moldura e efeitos.

### `Instagram/QuoteBlock`

- Finalidade/estrutura: citação fiel, aspas visuais discretas e autoria/fonte.
- Tipografia/cor: PT Serif no trecho; Montserrat na fonte; dourado apenas em detalhe.
- Variantes: `short`, `legal`; `source-missing` bloqueia publicação.
- Não parafrasear entre aspas nem inventar autoria.

### `Instagram/AlertLabel`

- Finalidade/estrutura: aviso curto com label textual; ícone opcional.
- Conteúdo: alerta real, não urgência artificial.
- Cor: tokens oficiais; significado não depende só de cor.
- Variantes: `attention`, `deadline`; estado `optional`.
- Não usar como decoração ou afirmar prazo não confirmado.

### `Instagram/NewsLabel`

- Finalidade/estrutura: marcar conteúdo noticioso; label e data opcional.
- Conteúdo: categoria/data confirmadas.
- Tipografia: Montserrat 700; cores oficiais.
- Variantes: `news`, `update`; `date-missing` quando data for necessária.
- Não converter opinião em notícia.

### `Instagram/ProcessNumber`

- Finalidade/estrutura: rótulo “Processo” e identificador integral.
- Conteúdo: número fornecido, preservando pontuação e dígitos.
- Tipografia: Montserrat; usar dígitos legíveis.
- Variante: `standard`; `verification-pending` bloqueia publicação.
- Não truncar, reformatar ou completar número.

### `Instagram/SourceReference`

- Finalidade/estrutura: “Fonte:” e referência curta.
- Conteúdo: fonte recebida e verificável; URL pode ficar na legenda quando longa.
- Tipografia/cor: Montserrat, papel de legenda; muted apenas se contraste AA.
- Variantes: `short`, `multi`; `missing` bloqueia alegação factual que exija fonte.
- Não fabricar ou ocultar referência necessária.

### `Instagram/Divider`

- Finalidade/estrutura: separar hierarquia; linha ou cápsula curta.
- Cor: gold com moderação, purple ou line; espessura conforme borda padrão.
- Variantes: `line`, `gold-accent`; `optional`.
- Não repetir entre todos os blocos nem usar sem função.

### `Instagram/DecorativeShape`

- Finalidade/estrutura: apoiar composição sem carregar significado.
- Conteúdo: forma simples sem texto.
- Cor/forma: tokens oficiais; raios oficiais; opacidade somente confirmada.
- Variantes: `block`, `circle`, `accent`; `optional`.
- Não competir com conteúdo, simular logo, criar padrão novo, neon ou clichê jurídico.

## Criação e mudança

Um componente novo exige uso recorrente, responsabilidade própria, impossibilidade de composição, acessibilidade, nome semântico e aprovação humana. Mudanças estruturais geram nova versão de template; não são correções de publicação.
