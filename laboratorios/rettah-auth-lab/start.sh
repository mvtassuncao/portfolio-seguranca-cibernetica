#!/usr/bin/env sh
set -eu
test -d .venv || python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python app.py

