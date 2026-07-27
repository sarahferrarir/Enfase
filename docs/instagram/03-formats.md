# Formatos

## Pranchetas oficiais

| Uso | Pixels | Proporção | Regra |
| --- | ---: | ---: | --- |
| Post vertical e carrossel | 1080 × 1350 | 4:5 | Padrão do feed |
| Post quadrado | 1080 × 1080 | 1:1 | Somente quando necessário e aprovado |
| Story | 1080 × 1920 | 9:16 | Não possui template no MVP |
| Capa de reel | 1080 × 1920 | 9:16 | Considerar corte no grid; não possui template no MVP |

Criar na resolução final, em pixels, sem redimensionamento posterior. Não misturar proporções em um carrossel.

## Área segura, grid e cortes

Todo conteúdo crítico deve permanecer dentro da área segura e a capa deve continuar compreensível no recorte do grid. Não posicionar rostos, logo, títulos, CTA, identificação ou números junto às bordas. Imagens podem sangrar até a borda se o foco permanecer protegido.

**Decisão pendente:** margens numéricas da área segura de cada formato, recorte exato usado pelo grid do perfil e zonas cobertas pela interface de Story/Reel. Até aprovação, nenhuma peça pode ser considerada pronta somente por inspeção da prancheta; deve haver teste visual no canal ou mockup validado.

Regras de corte:

- não cortar texto ou logo;
- não cortar olhos, boca ou articulações de forma acidental;
- definir ponto focal da foto;
- testar capa vertical na visualização reduzida e no recorte do grid;
- não acrescentar segunda versão improvisada para compensar corte.

## Carrosséis

Recomendação inicial: 6 slides para o carrossel educativo definido. Limite máximo técnico solicitado para o sistema: 10 slides. Entre 7 e 10 slides, a extensão exige justificativa editorial e aprovação humana. Não usar slides vazios para atingir quantidade.

## Exportação

- perfil de cor: sRGB;
- dimensões: exatamente as da tabela;
- imagem estática: PNG por padrão; JPEG somente para fotografia quando o ganho de peso for necessário e não houver degradação visível;
- não exportar GIF, PDF ou arquivo editável como publicação;
- sem transparência, salvo necessidade operacional aprovada;
- exportar cada slide individualmente e revisar a sequência.

**Decisão pendente:** compressão/qualidade JPEG, limite de peso, profundidade de cor, método de sharpening e padrão de metadados.

Nomenclatura: `AAAA-MM-DD_slug-template_formato_sNN_vNN.ext`.

Exemplos: `2026-07-27_prisao-preventiva-educativo_4x5_s01_v01.png`; post único usa `s01`. Use minúsculas, ASCII, hífens no slug, sem espaços ou acentos. Arquivo aprovado troca o diretório, não o nome; nova correção incrementa `vNN`.
