# Sincronização com o repositório original

Este fork carrega tradução para português e correções próprias. No momento em
que este documento foi escrito, são 38 commits tocando 83 arquivos, concentrados
em `docs/`, `agents/`, `skills/blog/templates/` e `scripts/`.

Por isso `git merge upstream/main` não serve como rotina. O problema não é o
conflito, que ao menos avisa. É o caso silencioso: quando o upstream reescreve
um arquivo inteiro que traduzimos, o git aceita a versão em inglês sem marcar
nada, e a tradução desaparece sem deixar rastro no relatório de merge.

O procedimento abaixo classifica antes de aplicar.

---

## Verificação

```bash
python3 scripts/check_upstream.py
```

Isso busca o remoto `upstream` (criando-o se não existir), compara com o último
ponto revisado e classifica cada arquivo alterado:

| Categoria | Significado | O que fazer |
|-----------|-------------|-------------|
| `seguro` | nunca tocamos este arquivo | pode entrar como está |
| `revisar` | nós mexemos e o upstream também | trabalho manual, veja abaixo |
| `novo` | não existe neste fork | pode entrar; talvez precise de tradução |
| `removido` | o upstream apagou | decidir caso a caso |

Duas marcações aparecem na coluna de notas. `CRITICO` sinaliza os arquivos onde
uma regressão passa despercebida com mais facilidade: `scripts/analyze_blog.py`,
`agents/blog-reviewer.md` e os dois instaladores. `traduzir` sinaliza arquivo em
inglês chegando a uma área que mantemos em português.

Para consumo por outra ferramenta:

```bash
python3 scripts/check_upstream.py --format json
```

---

## Aplicação

### Passo 1: trazer o que é seguro

```bash
python3 scripts/check_upstream.py --apply-safe
git diff
```

Isso escreve na árvore de trabalho apenas os arquivos `seguro` e `novo`. Nenhum
arquivo que alteramos é tocado, e há teste de regressão fixando essa
propriedade em `tests/test_check_upstream.py`.

Revise o diff mesmo assim. "Seguro" quer dizer que não reverte trabalho nosso,
não que a mudança seja desejável.

### Passo 2: tratar os arquivos em `revisar`

Um a um, e nunca trocando o arquivo inteiro:

```bash
git diff <base>..upstream/main -- docs/COMMANDS.md
```

Leia o que o upstream mudou, entenda a intenção, e aplique essa intenção sobre a
versão daqui. Se o upstream acrescentou uma linha numa tabela, acrescente a
linha traduzida. Se corrigiu um erro de lógica em `analyze_blog.py`, aplique a
correção preservando os perfis de idioma.

Um arquivo merece atenção especial: `CHANGELOG.md`. As entradas da v2.0.0 em
diante estão em português neste fork, e o upstream continua em inglês. Traduza
as entradas novas em vez de colar o bloco em inglês no meio.

### Passo 3: traduzir o que chegou em inglês

Arquivos marcados com `traduzir` na coluna de notas entraram em áreas que
mantemos em português. Cubra também os gatilhos de acionamento em pt no
frontmatter, caso tenha entrado uma sub-skill nova.

### Passo 4: validar

```bash
python3 -m pytest tests/ -q
python3 scripts/lint_prose.py
claude plugin validate .
```

### Passo 5: registrar o ponto revisado

```bash
python3 scripts/check_upstream.py --mark-reviewed
```

Isso grava o SHA do upstream em `.upstream-sync.json`, na raiz. O arquivo é
versionado de propósito: sem ele, a próxima verificação recomeça do ponto de
divergência e mostra tudo de novo.

---

## Rotina semanal

Existe uma rotina agendada que roda a verificação toda semana, aplica o que é
seguro e abre um pull request quando encontra novidade. Os arquivos em
`revisar` nunca entram nesse PR; ficam listados no corpo dele para tratamento
manual, seguindo o passo 2 acima.

Se a verificação não encontrar nada, a rotina não abre PR nem envia aviso.

---

## Quando o ledger aponta para um commit que sumiu

Se o upstream fizer rebase ou force-push, o SHA gravado pode deixar de existir.
O script detecta isso, avisa no stderr e cai para o ponto de divergência. O
efeito é mostrar mudanças demais, não de menos, o que é o lado seguro do erro.
