---
title: "14 - Agent Rules"
version: "2.1"
---

# Agent Rules

Este arquivo é destinado a Codex, Claude, ChatGPT e agentes semelhantes.

## Nunca Inventar

Agentes nunca devem inventar:

- preços;
- descontos;
- datas;
- prazos;
- número de vagas;
- bônus;
- cashback;
- links;
- telefones;
- professores;
- credenciais;
- produtos;
- carreiras;
- depoimentos;
- aprovações;
- estatísticas;
- regras acadêmicas;
- FAQs;
- imagens atribuídas a pessoas reais.

Também não devem recriar, redesenhar, recolorir ou substituir a logo oficial do Ênfase sem fonte oficial.

## Ordem De Busca

Antes de criar informação, verificar:

1. código existente;
2. dados do projeto;
3. Figma;
4. documentação;
5. fontes oficiais;
6. perguntar ao usuário.

Se a informação não puder ser confirmada, declarar pendência. Não preencher lacuna com inferência.

## Escopo Antes De Editar

Antes de editar, identificar:

- tipo da interface;
- objetivo da página;
- público;
- ação principal;
- componentes aplicáveis;
- regras não aplicáveis;
- dados que exigem confirmação.

## Alterações

O agente deve:

- preservar comportamento;
- não alterar dados de negócio sem autorização;
- não alterar componentes compartilhados sem avaliar impacto;
- listar arquivos afetados;
- separar fato, inferência e dúvida;
- marcar como `N/A` regras que não se aplicam.

## Logo E Marca

Ao usar a logo:

- verificar primeiro [`01-brand.md`](01-brand.md);
- usar o ativo oficial [`assets/logo-enfase.avif`](assets/logo-enfase.avif) quando aplicável;
- não inventar versão alternativa;
- não alterar proporção, cor, efeitos ou composição;
- garantir contraste e leitura;
- registrar como pendência quando a interface exigir uma variação oficial não documentada.

## Documentação

Quando a tarefa for apenas documentação:

- não alterar código de projeto;
- manter links relativos corretos;
- preservar conteúdo factual existente;
- mover conteúdo para o arquivo responsável;
- evitar duplicação desnecessária;
- verificar terminologia.

## Auditoria

Ao auditar:

- usar [15-audit.md](15-audit.md);
- não afirmar responsividade sem teste real;
- não afirmar fonte carregada apenas porque `font-family` foi declarado;
- registrar evidência;
- separar validação estática de validação em navegador.

## Linguagem

Use sempre "o Ênfase". Não use artigo feminino para a marca.
