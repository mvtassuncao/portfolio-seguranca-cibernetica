# Portal Acadêmico — laboratório de SQL Injection

Aplicação Flask/SQLite criada para estudar o efeito de SQL Injection sobre os resultados processados e exibidos pelo servidor.

## Como a criação se baseou

O banco é recriado a cada inicialização com dados fictícios, garantindo um estado conhecido e repetível. O formulário envia matrícula e senha; a versão vulnerável concatena esses valores na consulta para tornar a falha observável em um ambiente controlado.

## Prática e aprendizados

- compreender a fronteira entre dados e comandos;
- analisar como a consulta influencia a resposta do servidor;
- trabalhar com ambientes reproduzíveis;
- substituir concatenação por parâmetros do driver SQLite;
- aplicar validação no servidor, minimização de dados e testes de regressão.

## Execução local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:8080`. Não exponha o laboratório à internet.

