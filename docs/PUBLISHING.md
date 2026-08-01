# Fluxo de Publicação

Este guia é para mantenedores que publicam releases a partir do repositório
público
[`AgriciDaniel/claude-blog`](https://github.com/AgriciDaniel/claude-blog).
Quem contribui deve abrir um pull request em vez de enviar direto para a `main`.

## Fluxo padrão de release

1. Prepare a release numa branch de feature.
2. Confirme que a versão e a entrada datada do changelog concordam.
3. Rode o conjunto completo de validação local:

   ```bash
   python3 -m pytest tests/ -q
   python3 scripts/lint_prose.py --root .
   python3 scripts/consistency_check.py --root .
   python3 scripts/validate_public_release.py --root .
   claude plugin validate .
   git diff --check
   ```

4. Abra um pull request contra a `main` e espere todas as checagens de CI passarem.
5. Revise o diff final quanto a arquivos gerados, travas de dependência, hashes
   do instalador, referências canônicas ao repositório e coerência da versão.
6. Faça o merge do commit revisado sem ignorar checagens que falharam.
7. Crie uma tag anotada e assinada a partir do commit da `main` já mesclado.
8. Publique a release do GitHub a partir dessa tag existente.

## Versão e changelog

Mantenha a versão coerente em todas as superfícies canônicas:

- `.claude-plugin/plugin.json`
- `pyproject.toml`
- `CITATION.cff`, incluindo `date-released`
- `skills/blog/SKILL.md`
- Quaisquer valores `metadata.version` de sub-skills

Mova as mudanças concluídas de `## [Unreleased]` para uma seção datada
`## [X.Y.Z] - AAAA-MM-DD`. As notas da release devem descrever comportamento
visível ao usuário, compatibilidade, mudanças de dependência, correções de
segurança e limitações conhecidas. Links históricos de issue e pull request
podem permanecer quando ajudarem a rastrear uma correção.

## Tag e release do GitHub

Rode estes comandos somente depois que o pull request da release for mesclado e
a `main` estiver verde:

```bash
git switch main
git pull --ff-only origin main
git tag -s vX.Y.Z -m "claude-blog vX.Y.Z"
git verify-tag vX.Y.Z
git push origin refs/tags/vX.Y.Z

gh release create vX.Y.Z \
  --repo AgriciDaniel/claude-blog \
  --verify-tag \
  --fail-on-no-commits \
  --generate-notes \
  --title "claude-blog vX.Y.Z"
```

O `--verify-tag` impede que a CLI do GitHub crie silenciosamente uma tag
diferente. Nunca mova nem substitua uma tag de release já publicada. Se uma
release precisar de correção, publique uma nova versão de correção.

## Revisão de release pública

Antes de criar a tag, confirme:

- Comandos do instalador, URLs brutas, metadados canônicos do repositório e
  instruções do marketplace apontam para o projeto público.
- Os hashes do instalador correspondem aos arquivos commitados.
- Não há credenciais, caminhos locais, áreas de trabalho de auditoria,
  informação de cliente não publicada nem notas operacionais restritas ao
  mantenedor sob controle de versão.
- Os requisitos de dependência concordam com suas travas fixadas por hash.
- O registro de atualizações do Google contém apenas fontes primárias;
  observações não verificadas não podem afetar a pontuação.
- As notas da release descrevem as notas de citação por IA como heurísticas
  internas de prontidão, não como probabilidades calibradas ou garantia de
  inclusão.

## Artefatos da release

A tag de código e a release do GitHub são os artefatos canônicos. Mantenha fora
da release a saída local de auditoria, ambientes temporários, capturas geradas e
arquivos `BRAND.md`, `VOICE.md` ou `DISCOURSE.md` específicos de projeto, a menos
que um fluxo documentado exija explicitamente.

Se a publicação falhar depois que a tag foi enviada, mas antes de a release do
GitHub ser criada, investigue a falha antes de tentar de novo. Não recrie a tag
apontando para um commit diferente com a mesma versão.
