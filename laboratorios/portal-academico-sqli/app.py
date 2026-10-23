from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "lab.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    # Recria o banco sempre que a aplicação é iniciada.
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = get_db()

    conn.executescript("""
        CREATE TABLE alunos (
            id INTEGER PRIMARY KEY,
            matricula TEXT UNIQUE NOT NULL,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        );

        CREATE TABLE secrets (
            id INTEGER PRIMARY KEY,
            descricao TEXT NOT NULL,
            flag TEXT NOT NULL
        );

        INSERT INTO alunos (matricula, nome, senha) VALUES
            ('100001', 'Ana Souza', 'ana123'),
            ('100002', 'Bruno Lima', 'bruno123'),
            ('100003', 'Carlos Silva', 'carlos123');

        INSERT INTO secrets (descricao, flag) VALUES
            (
                'Segredo do laboratório',
                'FLAG{SQLI_SERVER_SIDE_RESULT_2026}'
            );
    """)

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def index():

    resultado = []
    erro = None

    if request.method == "POST":

        matricula = request.form.get("matricula", "")
        senha = request.form.get("senha", "")

        # ==========================================================
        # VULNERABILIDADE INTENCIONAL DO LABORATÓRIO
        #
        # NÃO faça isso em uma aplicação real.
        #
        # A entrada do usuário é concatenada diretamente na SQL.
        # ==========================================================

        query = f"""
            SELECT matricula, nome, senha
            FROM alunos
            WHERE matricula = '{matricula}'
            AND senha = '{senha}'
        """

        conn = get_db()

        try:
            rows = conn.execute(query).fetchall()

            # Tudo que aparecer na página veio diretamente
            # do resultado da consulta executada pelo servidor.
            resultado = [
                dict(row)
                for row in rows
            ]

        except sqlite3.Error:
            # Não mostramos detalhes do SQLite.
            erro = "Erro na consulta."

        finally:
            conn.close()

    return render_template(
        "index.html",
        resultado=resultado,
        erro=erro
    )


if __name__ == "__main__":
    init_db()

    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )