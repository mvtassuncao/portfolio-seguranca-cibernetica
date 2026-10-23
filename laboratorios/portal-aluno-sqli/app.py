from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DB = "lab.db"


def init_db():
    conn = sqlite3.connect(DB)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flag TEXT NOT NULL
        )
    """)

    # Usuário normal do laboratório
    conn.execute(
        "INSERT OR IGNORE INTO alunos (matricula, senha) VALUES (?, ?)",
        ("123456", "senha123")
    )

    # Flag do desafio
    conn.execute("DELETE FROM secrets")
    conn.execute(
        "INSERT INTO secrets (flag) VALUES (?)",
        ("FLAG{sql_injection_frontend_validation_is_not_security}",)
    )

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = None
    flag = None

    if request.method == "POST":
        matricula = request.form.get("matricula", "")
        senha = request.form.get("senha", "")

        # INTENCIONALMENTE VULNERÁVEL:
        # Não use concatenação de strings para SQL em aplicações reais.
        query = f"""
            SELECT id, matricula, senha
            FROM alunos
            WHERE matricula = '{matricula}'
            AND senha = '{senha}'
        """

        conn = sqlite3.connect(DB)

        try:
            resultado = conn.execute(query).fetchone()

            if resultado:
                mensagem = "Login realizado com sucesso."

            # Para o desafio, verificamos se a consulta conseguiu
            # acessar a tabela secrets.
            secret_query = f"""
                SELECT flag
                FROM secrets
                WHERE '{matricula}' = '{matricula}'
            """

            try:
                secret = conn.execute(secret_query).fetchone()

                if secret:
                    flag = secret[0]

            except sqlite3.Error:
                pass

            if not resultado and not flag:
                mensagem = "Matrícula ou senha inválida."

        except sqlite3.Error:
            mensagem = "Erro na consulta SQL."

        finally:
            conn.close()

    return render_template(
        "index.html",
        mensagem=mensagem,
        flag=flag
    )


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=443, debug=False)