# Rettah Auth Pentest Lab

Desenvolvi esta aplicação Flask deliberadamente vulnerável para estudar autenticação e sessão. Ela deve ser usada **exclusivamente em aula, VM ou rede isolada e autorizada**.

## O que eu quis estudar

- ausência de limitação de tentativas;
- armazenamento MD5 e comparação com vazamento temporal;
- fixação de cookie de sessão;
- JWT aceito sem validação de assinatura;
- reset de senha com token previsível/vazado;
- descoberta de uma flag armazenada no banco como dado de usuário.

Organizei o laboratório como uma sequência de desafios porque queria observar cada falha separadamente e depois entender como elas podem formar uma cadeia. Na primeira execução, acesse a aplicação e informe o nome do aluno. Cinco flags individuais serão geradas. Apague `.student.json` e `lab.db` para reiniciar para outro aluno.

## Minha lógica de análise

Comecei pelo fluxo de login e acompanhei o dado até o banco. Depois observei como o token e o cookie eram criados e quais decisões de autorização o servidor tomava. Por último, analisei a recuperação de senha. Essa sequência mostrou que autenticar uma identidade e autorizar uma ação são problemas diferentes.

Para cada falha, relacionei uma correção: limitação de tentativas, algoritmo moderno para senha, comparação segura, renovação de sessão, verificação de assinatura JWT e token de recuperação aleatório e de uso único.

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

