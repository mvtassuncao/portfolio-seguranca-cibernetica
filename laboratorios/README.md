# Laboratórios de Segurança de Aplicações

Esta área reúne aplicações deliberadamente vulneráveis, criadas para compreender falhas por meio de reprodução controlada e posterior análise de mitigação.

| Laboratório | Foco | Base da criação | Competência demonstrada |
|---|---|---|---|
| [Rettah Auth Lab](rettah-auth-lab/) | Autenticação e sessão | Fluxos inseguros contrastados com requisitos defensivos | Modelagem de ameaças, Flask, JWT, cookies e recuperação de senha |
| [Portal do Aluno](portal-aluno-sqli/) | SQL Injection | Concatenação insegura de entrada em consulta SQL | Identificação de causa raiz e parametrização como correção |
| [Portal Acadêmico](portal-academico-sqli/) | SQL Injection e resultados | Banco descartável e resposta renderizada pelo servidor | Reprodutibilidade, SQLite e análise do fluxo de dados |

> Execute apenas em `localhost`, máquina virtual ou rede isolada. Não publique portas nem direcione os exemplos a sistemas de terceiros.

