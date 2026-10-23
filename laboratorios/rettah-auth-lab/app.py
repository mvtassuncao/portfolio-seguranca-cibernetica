from __future__ import annotations

import hashlib
import json
import os
import random
import re
import sqlite3
import time
from datetime import datetime, timedelta, timezone
from functools import wraps
from pathlib import Path

import jwt
from flask import Flask, jsonify, make_response, redirect, render_template_string, request

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "lab.db"
PROFILE_PATH = BASE_DIR / ".student.json"
JWT_SECRET = "secret"

app = Flask(__name__)
app.secret_key = "hardcoded_super_secret_key_123"


SETUP_PAGE = """<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'><title>Rettah Auth Lab</title>
<style>body{font-family:system-ui;background:#10151d;color:#e8edf5;max-width:620px;margin:60px auto;padding:24px}main{background:#18212d;padding:30px;border-radius:14px}input,button{box-sizing:border-box;width:100%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #516070}button{background:#32b67a;color:#08120e;font-weight:700;cursor:pointer}</style></head>
<body><main><h1>Rettah Auth Lab</h1><p>Informe seu nome antes de iniciar a prova.</p>
<form method='post' action='/setup'><input name='student' maxlength='60' required autocomplete='off' placeholder='Nome do aluno'><button>Iniciar laboratório</button></form></main></body></html>"""

LOGIN_PAGE = """<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'><title>Portal Rettah</title>
<style>body{font-family:system-ui;background:#10151d;color:#e8edf5;max-width:760px;margin:50px auto;padding:24px}main{background:#18212d;padding:30px;border-radius:14px}input,button{box-sizing:border-box;width:100%;padding:12px;margin:7px 0;border-radius:8px;border:1px solid #516070}button{background:#32b67a;font-weight:700;cursor:pointer}code{overflow-wrap:anywhere;color:#84e2b5}.muted{color:#93a0b1}</style></head>
<body><main><h1>Portal Rettah</h1><p class='muted'>Laboratório de autenticação — aluno: {{ student }}</p>
<form id='login'><input id='user' placeholder='Usuário' required><input id='pwd' type='password' placeholder='Senha' required><button>Entrar</button></form><p id='result'></p>
<script>/* {{ flag1 }} */
document.querySelector('#login').onsubmit=async(e)=>{e.preventDefault();let r=await fetch('/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({user:user.value,pwd:pwd.value})});let d=await r.json();if(d.token){localStorage.token=d.token;result.innerHTML='Token: <code>'+d.token+'</code>'}else result.textContent=d.error||'Falha';};</script></main></body></html>"""


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    return value or "aluno"


def load_profile():
    if not PROFILE_PATH.exists():
        return None
    return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))


def make_flags(student: str):
    clean = slugify(student)
    letters = len(re.sub(r"[^A-Za-zÀ-ÿ]", "", student))
    rng = random.SystemRandom()
    return {f"flag{i}": f"flag{i}_{clean}_{letters}{rng.randint(1000, 9999)}" for i in range(1, 6)}


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(profile):
    conn = connect()
    conn.execute("DROP TABLE IF EXISTS users")
    conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, reset_token TEXT, token_expiry TEXT, note TEXT)")
    users = [
        ("admin", hashlib.md5(b"admin123").hexdigest(), None, None, "Conta administrativa"),
        ("pedro", hashlib.md5(b"123456").hexdigest(), None, None, "Usuário padrão"),
        ("maria", hashlib.md5(b"password").hexdigest(), None, None, "Usuária padrão"),
        # A flag 3 está deliberadamente no campo de senha para o exercício de banco.
        ("backup", profile["flags"]["flag3"], None, None, "Conta de contingência"),
    ]
    conn.executemany("INSERT INTO users(username,password,reset_token,token_expiry,note) VALUES(?,?,?,?,?)", users)
    conn.commit()
    conn.close()


def profile_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not load_profile():
            return redirect("/setup")
        return fn(*args, **kwargs)
    return wrapped


@app.get("/")
@profile_required
def index():
    profile = load_profile()
    return render_template_string(LOGIN_PAGE, student=profile["student"], flag1=profile["flags"]["flag1"])


@app.route("/setup", methods=["GET", "POST"])
def setup():
    if request.method == "GET":
        if load_profile():
            return redirect("/")
        return SETUP_PAGE
    student = request.form.get("student", "").strip()
    if not student:
        return SETUP_PAGE, 400
    profile = {"student": student, "flags": make_flags(student)}
    PROFILE_PATH.write_text(json.dumps(profile, ensure_ascii=False, indent=2), encoding="utf-8")
    init_db(profile)
    return redirect("/")


@app.post("/login")
@profile_required
def login():
    data = request.get_json(silent=True) or {}
    username, password = data.get("user", ""), data.get("pwd", "")
    conn = connect()
    row = conn.execute("SELECT password FROM users WHERE username=?", (username,)).fetchone()
    conn.close()
    supplied = hashlib.md5(password.encode()).hexdigest()
    stored = row["password"] if row else "0" * 32
    # Comparação propositalmente vulnerável: demora conforme o prefixo correto.
    correct = True
    for left, right in zip(supplied, stored):
        if left != right:
            correct = False
            break
        time.sleep(0.004)
    correct = correct and supplied == stored
    if not correct:
        return jsonify(error="Credenciais inválidas"), 401
    token = jwt.encode({"user": username, "role": "user", "exp": int(time.time()) + 3600}, JWT_SECRET, algorithm="HS256")
    response = make_response(jsonify(token=token, flag=load_profile()["flags"]["flag2"]))
    # ID escolhido pelo cliente e preservado após o login: fixação de sessão didática.
    response.set_cookie("lab_session", request.cookies.get("lab_session", "guest-session"), httponly=False)
    return response


@app.get("/admin")
@profile_required
def admin():
    token = request.headers.get("Authorization", "").removeprefix("Bearer ")
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
    except Exception:
        return jsonify(error="Token inválido"), 401
    if payload.get("user") != "admin" and payload.get("role") != "admin":
        return jsonify(error="Acesso negado"), 403
    return jsonify(message="Painel administrativo", flag=load_profile()["flags"]["flag4"], token_data=payload)


@app.post("/reset_password")
@profile_required
def reset_password():
    username = (request.get_json(silent=True) or {}).get("username", "")
    timestamp = int(time.time())
    token = hashlib.md5(f"{username}{timestamp}".encode()).hexdigest()
    expiry = (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat()
    conn = connect()
    changed = conn.execute("UPDATE users SET reset_token=?, token_expiry=? WHERE username=?", (token, expiry, username)).rowcount
    conn.commit(); conn.close()
    if not changed:
        return jsonify(message="Se o usuário existir, o reset será processado")
    # Vazamento proposital para tornar o exercício reproduzível.
    return jsonify(message="Token de reset gerado", token=token, generated_at=timestamp)


@app.post("/confirm_reset")
@profile_required
def confirm_reset():
    data = request.get_json(silent=True) or {}
    token, new_password = data.get("token", ""), data.get("new_password", "")
    conn = connect()
    row = conn.execute("SELECT username,token_expiry FROM users WHERE reset_token=?", (token,)).fetchone()
    if not row or datetime.fromisoformat(row["token_expiry"]) <= datetime.now(timezone.utc):
        conn.close(); return jsonify(error="Token inválido ou expirado"), 401
    conn.execute("UPDATE users SET password=?,reset_token=NULL,token_expiry=NULL WHERE username=?", (hashlib.md5(new_password.encode()).hexdigest(), row["username"]))
    conn.commit(); conn.close()
    return jsonify(message="Senha alterada", user=row["username"], flag=load_profile()["flags"]["flag5"])


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    print("Rettah Auth Lab: http://0.0.0.0:5000")
    print("Use apenas em laboratório isolado e autorizado.")
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
