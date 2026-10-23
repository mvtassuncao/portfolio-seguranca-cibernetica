# Rettah Auth Pentest Lab

Aplicação Flask deliberadamente vulnerável para uso **exclusivo em aula, VM ou rede isolada e autorizada**.

## Objetivos

- ausência de limitação de tentativas;
- armazenamento MD5 e comparação com vazamento temporal;
- fixação de cookie de sessão;
- JWT aceito sem validação de assinatura;
- reset de senha com token previsível/vazado;
- descoberta de uma flag armazenada no banco como dado de usuário.

Na primeira execução, acesse a aplicação e informe o nome do aluno. Cinco flags individuais serão geradas no formato `flagN_nome_quantidadeDeLetrasNumeroAleatorio`. Apague `.student.json` e `lab.db` para reiniciar para outro aluno.

## Windows

Execute `start.bat`. Depois, abra `http://127.0.0.1:5000`.

## Linux

```bash
chmod +x start.sh
./start.sh
```

## Acesso pela VM Kali em modo bridge

1. Execute o laboratório na máquina do aluno.
2. Descubra o IPv4 dessa máquina (`ipconfig` no Windows ou `ip addr` no Linux).
3. Libere a porta TCP 5000 apenas no perfil de rede privada/laboratorial do firewall.
4. Na Kali, acesse `http://IP-DA-MAQUINA:5000`.

O Flask escuta em `0.0.0.0:5000`. Não encaminhe essa porta no roteador e não exponha o laboratório à internet.

## Ferramentas demonstrativas

Com o ambiente virtual ativo:

```bash
python tools/brute_force.py --url http://127.0.0.1:5000
python tools/session_fixation.py --url http://127.0.0.1:5000
python tools/timing_probe.py --url http://127.0.0.1:5000
python tools/reset_token.py --url http://127.0.0.1:5000
python tools/jwt_exploit.py --url http://127.0.0.1:5000 --token TOKEN_DO_LOGIN
```

As ferramentas têm alvo padrão local e devem ser usadas somente nesta aplicação.

## Flags

- Flag 1: código-fonte HTML da página inicial.
- Flag 2: autenticação válida.
- Flag 3: registro do usuário `backup` no banco SQLite.
- Flag 4: painel administrativo via JWT vulnerável.
- Flag 5: conclusão do reset de senha.

