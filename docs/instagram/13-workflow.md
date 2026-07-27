# Fluxo de produção

## Etapas

1. **Receber:** criar ID, preservar conteúdo original e registrar responsável.
2. **Preparar:** estruturar o input de `09-content.md` sem mudar significado.
3. **Validar:** conferir campos, fontes, processo, datas, CTA, status jurídico e direitos.
4. **Selecionar:** escolher um dos três templates pelo objetivo; exceções exigem aprovação.
5. **Preparar assets:** confirmar origem/licença, nomear, recortar sem alteração indevida e registrar IA.
6. **Abrir no Pencil:** duplicar a versão oficial do template; nunca trabalhar no master.
7. **Preencher:** mapear campos aos componentes; não redesenhar; registrar conflitos.
8. **Revisar visualmente:** executar checklist por slide, visualização reduzida, grid/cortes e sequência.
9. **Revisar conteúdo e jurídico:** comparar palavra, número, data, fonte, tese e ressalva com a entrada aprovada.
10. **Corrigir:** separar correção de conteúdo de correção de layout; incrementar versão; repetir QA afetado.
11. **Exportar:** dimensões finais, sRGB, formato e nomes oficiais; gerar manifesto.
12. **Aprovar:** obter aceite visual, editorial, jurídico e de direitos aplicáveis.
13. **Publicar/arquivar:** mover cópia aprovada, manter fontes e registrar data; não sobrescrever histórico.
14. **Aprender:** guardar exemplos aprovados; atualizar master/documentação somente por mudança governada.

Nenhuma etapa posterior elimina bloqueio anterior. Uma correção após aprovação cria nova versão e nova aprovação.

## Estrutura operacional sugerida

```text
instagram-content/
├── assets/       # originais, licenças e registros de IA
├── templates/    # masters versionados e bloqueados
├── drafts/       # instâncias em produção e manifestos
├── approved/     # exports e aprovações finais
└── examples/     # peças aprovadas, catalogadas por template/variante
```

Dentro de cada trabalho, manter `input`, `source`, `assets`, `review` e `exports` identificáveis. **Decisão pendente:** convenção de subpastas, manifesto técnico e política de retenção.

## Governança

Exemplos aprovados demonstram uso; não viram template automaticamente. Alteração de master exige motivo recorrente, impacto avaliado, nova versão, QA, aprovação humana e atualização sincronizada de componentes, prompts e checklists. Atualização documental não deve apagar decisões anteriores sem registro.

## Responsabilidades

Humanos: fornecer conteúdo e fontes; decidir estratégia; validar resumo; revisar juridicamente; liberar direitos; aprovar decisões pendentes, templates, exceções e publicação.

IA: validar input; selecionar entre opções autorizadas; preencher; preservar conteúdo e marca; detectar overflow, contraste e inconsistência; produzir relatórios; exportar somente após aprovações. IA não concede direitos, interpreta silêncio como aprovação, altera master, cria fatos ou faz julgamento jurídico final.
