# Lista de Verificação de Release

Use esta lista antes de publicar uma release do claude-blog.

## Versionamento
- [ ] A versão está coerente em `.claude-plugin/plugin.json`, `pyproject.toml`, `README.md` e `CHANGELOG.md`.
- [ ] O `CHANGELOG.md` tem uma seção datada para a release.
- [ ] Os exemplos de instalação do README apontam para o repositório e a referência pretendidos.
- [ ] Os hashes do instalador no README correspondem aos `install.sh` e `install.ps1` commitados.

## Validação
- [ ] `python3 scripts/lint_prose.py` passa.
- [ ] `python3 -m pytest tests/ -q` passa quando scripts ou testes mudaram.
- [ ] `claude plugin validate .` passa numa máquina com o Claude Code instalado.
- [ ] A CI está verde na branch protegida.

## Teste de fumaça do instalador
- [ ] O instalador Unix funciona num `HOME` temporário.
- [ ] O instalador Windows funciona num perfil temporário.
- [ ] Os payloads aninhados das skills estão presentes após a instalação, incluindo as referências de prompt do FLOW e os templates de relatório do Google.
- [ ] A desinstalação no Unix remove apenas caminhos do manifesto do claude-blog ou da lista permitida do pacote.
- [ ] As credenciais compartilhadas em `~/.config/claude-seo` não são apagadas pela desinstalação.

## Publicação
- [ ] Os metadados do marketplace apontam para o proprietário e o repositório pretendidos.
- [ ] As notas da release destacam correções de segurança ou de auditoria.
- [ ] Crie e envie a tag da release somente depois que todas as checagens passarem.
