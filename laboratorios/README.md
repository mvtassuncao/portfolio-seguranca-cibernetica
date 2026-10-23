# Laboratórios de Segurança de Aplicações

Nesta área reuni aplicações deliberadamente vulneráveis que desenvolvi e utilizei para compreender falhas por meio de reprodução controlada. Em cada exercício procurei observar a causa técnica, comprovar o comportamento dentro do laboratório e depois relacionar a vulnerabilidade com sua mitigação.

| Laboratório | Foco | Base da criação | Competência demonstrada |
|---|---|---|---|
| [Rettah Auth Lab](rettah-auth-lab/) | Autenticação e sessão | Fluxos inseguros contrastados com requisitos defensivos | Modelagem de ameaças, Flask, JWT, cookies e recuperação de senha |
| [Portal do Aluno](portal-aluno-sqli/) | SQL Injection | Concatenação insegura de entrada em consulta SQL | Identificação de causa raiz e parametrização como correção |
| [Portal Acadêmico](portal-academico-sqli/) | SQL Injection e resultados | Banco descartável e resposta renderizada pelo servidor | Reprodutibilidade, SQLite e análise do fluxo de dados |

> Eu executei estes projetos somente em ambiente autorizado. Para reproduzir os exercícios, use `localhost`, máquina virtual ou rede isolada. Não publique as portas nem direcione os exemplos a sistemas de terceiros.

