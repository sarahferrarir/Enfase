# Templates oficiais

Somente os três templates abaixo fazem parte do MVP. Todos usam os componentes nomeados, tokens oficiais, pranchetas de `03-formats.md` e posições bloqueadas. **Decisão pendente:** coordenadas e tamanhos finais após montagem e aprovação no Pencil.

## 1. Carrossel educativo

Objetivo: explicar tema jurídico/educacional em sequência. Uso: conceito, entendimento, procedimento, consequência prática. Formato: 1080 × 1350; recomendado 6 slides; máximo 10 com aprovação.

Estrutura:

1. capa — categoria, título, apoio opcional, logo;
2. contexto — o problema ou enquadramento;
3. explicação principal — fundamento fornecido;
4. consequência prática — efeito sem extrapolação;
5. conclusão ou resumo — síntese aprovada;
6. CTA — ação específica, logo e fonte quando aplicável.

Obrigatórios: `CategoryLabel` quando recebida, `TitleBlock`, `BodyText` nos internos, `Footer`, `SlideNumber`, `Brand/Logo`; fonte quando necessária. Opcionais: subtítulo, quote, processo, divisor, imagem e CTA quando explicitamente `N/A` por contexto.

Hierarquia: categoria < título > corpo > referência/rodapé. Variantes permitidas: clara, escura e com imagem, somente se já montadas no template. Pode mudar conteúdo, foto/crop e variante prevista. Não pode mudar grid, fonte, cores, componentes, margens, logo, numeração ou ordem mínima. Imagem deve ser autorizada, com foco protegido. CTA não pode introduzir promessa.

Exportar seis PNGs sRGB na sequência e nomenclatura oficial; JPEG só para fotografia justificada.

Exemplo:

```text
S1 [CATEGORIA] [TÍTULO] [SUBTÍTULO?]
S2 [TÍTULO: CONTEXTO] [TEXTO]
S3 [TÍTULO: EXPLICAÇÃO] [TEXTO/FONTE]
S4 [TÍTULO: CONSEQUÊNCIA] [TEXTO]
S5 [TÍTULO: EM RESUMO] [SÍNTESE APROVADA]
S6 [CTA] [FONTE?] [LOGO]
```

Prompt de preenchimento: `Preencha a instância do template Carrossel educativo com o input estruturado. Preserve componentes e conteúdo jurídico; associe cada unidade aos slides 1–6; sinalize qualquer excesso, lacuna ou conflito sem redesenhar.`

Checklist: [ ] 6 slides mínimos [ ] uma ideia por slide [ ] sequência lógica [ ] números corretos [ ] fonte presente [ ] CTA confirmado [ ] capa legível no grid [ ] QA completo.

## 2. Post informativo simples

Objetivo: comunicar uma informação principal. Uso: aviso, notícia, atualização ou resumo que não exige sequência. Formato padrão 1080 × 1350; quadrado somente com necessidade e aprovação; um slide.

Estrutura: categoria; título; resumo; imagem opcional; CTA; logo. Obrigatórios: `CategoryLabel`, `TitleBlock`, `BodyText`, `Brand/Logo`; CTA obrigatório salvo `N/A` explícito. Opcionais: `NewsLabel`, `AlertLabel`, `ImageContainer`, `SourceReference`, `ProcessNumber`, divisor.

Hierarquia: categoria < título > resumo > CTA > marca. Variantes: clara, escura, com imagem; apenas variantes existentes. Pode mudar texto, imagem/crop e variante. Não pode mudar anatomia, tokens, margens, fonte ou marca. Fotografia não pode reduzir leitura. CTA precisa de ação/destino real.

Exportar um PNG sRGB com nomenclatura oficial; JPEG conforme regra de fotografia.

```text
[CATEGORIA]
[TÍTULO]
[RESUMO]
[IMAGEM OPCIONAL]
[CTA]
[LOGO]
```

Prompt: `Preencha o template Post informativo simples com categoria, título, resumo, CTA e asset fornecidos. Use a variante existente adequada; não crie elementos; devolva excesso ou campo ausente.`

Checklist: [ ] uma ideia [ ] categoria correta [ ] título factual [ ] resumo cabe sem compressão [ ] fonte/data quando necessárias [ ] CTA confirmado [ ] logo preservada [ ] QA completo.

## 3. Conteúdo com professor

Objetivo: associar conteúdo/convite a professor real e autorizado. Uso: aula, análise, apresentação ou chamada com identificação. Formato padrão 1080 × 1350; um slide; desdobramento em carrossel requer o template educativo.

Estrutura: fotografia; título; identificação; resumo; CTA; logo. Obrigatórios: `ImageContainer`, `TitleBlock`, `ProfessorIdentification`, `Brand/Logo`; resumo e CTA conforme input. Opcionais: categoria, curso, divisor e fonte.

Hierarquia: título e rosto > nome > resumo > CTA > marca. Variantes: retrato à esquerda/direita ou full-bleed somente se existentes. Pode mudar foto, crop, texto e variante. Não pode gerar professor, inventar credencial, retocar identidade, mover marca ou alterar moldura. CTA específico e confirmado.

Exportar um PNG sRGB; JPEG permitido se preservar texto/nitidez e reduzir peso.

```text
[FOTO AUTORIZADA]
[TÍTULO]
[NOME DO PROFESSOR]
[CARGO/TITULAÇÃO] · [CURSO?]
[RESUMO]
[CTA]
[LOGO]
```

Prompt: `Preencha o template Conteúdo com professor com foto autorizada e dados confirmados. Preserve identidade, crop seguro, identificação literal, componentes e tokens. Bloqueie a saída se direito de imagem ou credencial estiver pendente.`

Checklist: [ ] autorização da foto [ ] identidade correta [ ] credencial literal [ ] crop natural [ ] texto não cobre rosto [ ] CTA confirmado [ ] logo preservada [ ] QA completo.
