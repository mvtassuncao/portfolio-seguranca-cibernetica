# Portal Acadêmico — laboratório de SQL Injection

Criei esta aplicação Flask/SQLite para estudar o efeito de SQL Injection sobre os resultados processados e exibidos pelo servidor.

## Como a criação se baseou

Configurei o banco para ser recriado a cada inicialização com dados fictícios, garantindo um estado conhecido e repetível. O formulário envia matrícula e senha; na versão vulnerável, concatenei propositalmente esses valores na consulta para tornar a falha observável em ambiente controlado.

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

