# Ênfase

Repositório utilizado para armazenar projetos, estudos, protótipos e entregas desenvolvidos durante o estágio no Ênfase.

## Objetivo

Centralizar os projetos desenvolvidos durante o estágio, mantendo histórico de versões, documentação, testes e implementações realizadas ao longo das atividades.

## Estrutura

| Pasta ou arquivo | Finalidade |
| --- | --- |
| [ConversorInformativoSTF/](ConversorInformativoSTF/README.md) | Conversor determinístico de informativos do STF em DOCX para JSON, com testes e validações em Python. |
| [ConversorInformativoSTJ/](ConversorInformativoSTJ/README.md) | Conversor de informativos do STJ em HTML para JSON, com BeautifulSoup, Ollama e validação por Pydantic. |
| [ProcessoEmSegredo/](ProcessoEmSegredo/README.md) | Parser em TypeScript de PDFs de pautas de julgamento do STJ, com exportação para JSON. |
| [MapeamentoBancoQuestoes/](MapeamentoBancoQuestoes/README.md) | Análise do banco de questões: scripts, dados intermediários, inventário, fontes oficiais e rastreabilidade. |
| [MapeamentoInsta/](MapeamentoInsta/README.md) | Pesquisa editorial do Instagram, com inventários, catálogo de templates, matriz, lacunas e relatório final. |
| [Pencil/](Pencil/) | Arquivo editável de templates do Pencil e assets associados. |
| [docs/design/](docs/design/README.md) | Documentação detalhada do design system e seus assets. |
| [docs/instagram/](docs/instagram/README.md) | Diretrizes visuais, formatos, componentes e fluxo de produção para Instagram. |
| [DESIGN.md](DESIGN.md) | Ponto de entrada do design system do Ênfase. |

### Banco de Questões

Os recursos de análise estão reunidos em `MapeamentoBancoQuestoes/`:

- `scripts/`: extração, inspeção e análise de dados;
- `scripts/legacy/`: gerador histórico `build_deliverables.py`;
- `data/analysis/`: dados intermediários preservados;
- arquivos JSON e Markdown na pasta principal: entregáveis da pesquisa.

O gerador legado não reproduz integralmente os entregáveis finais atuais. Consulte o [README do projeto](MapeamentoBancoQuestoes/README.md) antes de executar scripts que gravam arquivos.

### Pencil

O template está em [Pencil/instagram-content-templates-enfase-instagram.pen](Pencil/instagram-content-templates-enfase-instagram.pen). Os arquivos `clipboard`, `clipboard-1` e a pasta `images/` estão em `Pencil/assets/`.

O template também utiliza assets de `docs/instagram/assets/` por caminhos relativos. Preserve essas referências ao mover arquivos.

## Como utilizar

Cada projeto possui requisitos e comandos próprios. Consulte os READMEs indicados na tabela antes de instalar dependências ou executar conversores; não há um comando único de instalação ou execução para todo o repositório.

O script de inspeção Node do Banco de Questões depende de `@oai/artifact-tool`, atualmente resolvido por um link `node_modules` na raiz para um runtime externo. Esse vínculo é específico do ambiente local; consulte a documentação do projeto para essa limitação.

## Observações

- Este repositório é de uso interno do Ênfase.
- Exemplos, dados intermediários e entregáveis versionados fazem parte do acervo dos projetos; não devem ser tratados automaticamente como arquivos descartáveis.
- As implementações podem conter versões experimentais, protótipos e registros de evolução das soluções.
