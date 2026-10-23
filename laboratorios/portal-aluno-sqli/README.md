# Portal do Aluno — laboratório de SQL Injection

Criei esta aplicação acadêmica em Flask e SQLite para demonstrar, de forma controlada, por que dados recebidos do navegador nunca devem ser concatenados diretamente em SQL.

## Como a criação se baseou

Parti de um fluxo simples de autenticação por matrícula e senha. Implementei propositalmente uma versão insegura que mistura a entrada do usuário com a instrução SQL, deixando visível a causa raiz da injeção. Usei uma tabela separada para representar um dado que deveria permanecer inacessível.

## Prática e aprendizados

- acompanhar a entrada do formulário até a consulta;
- distinguir validação de interface de controle no servidor;
- observar o efeito de uma consulta alterada pelo usuário;
- propor consultas parametrizadas, privilégio mínimo e erros genéricos;
- executar testes somente em ambiente descartável e autorizado.

## Execução local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

O código original usa a porta 443. Em alguns sistemas ela exige privilégios elevados; para estudo local, altere para uma porta alta, como 5000. Não exponha a aplicação à internet.

