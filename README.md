# Meu Portfólio Técnico em Segurança Cibernética

Olá! Eu sou **Marcos Vinicio Tiburcio Assunção** e este repositório reúne os principais trabalhos que desenvolvi durante minha formação técnica em **Segurança Cibernética**, entre **2024 e 2026**.

Criei este portfólio para apresentar de forma organizada o que aprendi e pratiquei durante o curso. Aqui estão meus laboratórios de segurança, análises de vulnerabilidades, relatórios de pentest, atividades de redes e criptografia, além de projetos em HTML, CSS, JavaScript, Python, Flask e SQLite.

Meu objetivo não é apenas mostrar arquivos prontos. Em cada seção eu procuro explicar:

- o que eu estava estudando;
- por que desenvolvi aquela atividade;
- quais ferramentas e conceitos utilizei;
- como organizei meu raciocínio durante a análise;
- o que encontrei e como cheguei à conclusão;
- quais correções ou melhorias eu recomendaria;
- o que aprendi com a prática.

> Todos os testes ofensivos foram realizados em laboratórios didáticos, máquinas vulneráveis, redes isoladas ou alvos destinados a testes. Removi da versão pública dados pessoais, credenciais, hashes, tokens, flags, bancos de dados e evidências que pudessem afetar terceiros. Mais detalhes estão em [SECURITY.md](SECURITY.md).

## O que este portfólio demonstra

| Área | O que eu pratiquei | Conhecimentos demonstrados |
|---|---|---|
| Segurança de aplicações | Criação e análise de aplicações Flask vulneráveis | SQL Injection, autenticação, JWT, sessões, reset de senha e mitigação |
| Pentest | Reconhecimento, enumeração, validação e documentação | Escopo, evidências, impacto, risco, recomendação e reteste |
| Redes | Descoberta de hosts, portas e serviços | Nmap, redes virtuais, segmentação e interpretação de resultados |
| Criptografia | Estudo de assinaturas digitais | Hashes, chaves assimétricas, autenticidade, integridade e não repúdio |
| Desenvolvimento web | Sites acadêmicos multipágina | HTML5, CSS3, JavaScript, formulários e organização de código |
| Comunicação técnica | Relatórios e apresentações | Escrita técnica, síntese, explicação de risco e trabalho em equipe |

## Como organizei o repositório

- [`laboratorios/`](laboratorios/) — aplicações que criei ou utilizei para compreender vulnerabilidades em ambiente controlado.
- [`estudos-de-caso/`](estudos-de-caso/) — análises públicas e sanitizadas dos exercícios de pentest.
- [`relatorios/`](relatorios/) — documentos acadêmicos que passaram pela revisão de segurança para publicação.
- [`projetos-web/`](projetos-web/) — sites e aplicações desenvolvidos durante o curso.
- [`catalogo.md`](catalogo.md) — explicação detalhada de cada trabalho, incluindo minha linha de raciocínio.
- [`PUBLICACAO.md`](PUBLICACAO.md) — o que decidi publicar e o que mantive fora por segurança ou privacidade.

## Como eu conduzo uma análise

Ao longo do curso, desenvolvi uma forma de organizar meu raciocínio para não começar diretamente pela exploração:

1. **Entender o objetivo e o escopo:** primeiro identifico qual ambiente pode ser testado, quais limites devem ser respeitados e qual resultado a atividade espera.
2. **Preparar um ambiente seguro:** sempre que possível, uso máquinas virtuais, rede isolada e dados fictícios.
3. **Fazer reconhecimento:** procuro entender os hosts, portas, aplicações e serviços disponíveis.
4. **Enumerar antes de concluir:** coleto versões e comportamentos para transformar uma suspeita em uma hipótese técnica.
5. **Validar com controle:** testo somente o necessário para comprovar ou descartar a hipótese, evitando ações fora do escopo.
6. **Registrar evidências:** documento comandos, respostas, capturas e observações relevantes.
7. **Analisar impacto:** relaciono a falha técnica com confidencialidade, integridade, disponibilidade e possíveis efeitos para o negócio.
8. **Recomendar correções:** procuro tratar a causa raiz, não somente o sintoma.
9. **Reconhecer limitações:** quando não há evidência suficiente, registro que a vulnerabilidade não foi confirmada.

Essa lógica foi importante para eu compreender que encontrar uma porta aberta, uma versão de software ou uma mensagem de erro não significa automaticamente que existe uma vulnerabilidade explorável.

## Ferramentas e tecnologias que utilizei

- **Nmap:** descoberta de hosts, identificação de portas, serviços e versões.
- **Burp Suite:** observação e alteração controlada de requisições HTTP em laboratórios web.
- **Kali Linux:** ambiente de apoio para ferramentas de segurança e testes autorizados.
- **Metasploit Framework:** validação de vulnerabilidades conhecidas em máquinas deliberadamente vulneráveis.
- **Python e Flask:** construção de aplicações e laboratórios de segurança.
- **SQLite:** criação de bancos locais e estudo de consultas seguras e inseguras.
- **HTML, CSS e JavaScript:** desenvolvimento de interfaces, sites, formulários e interações no navegador.
- **Máquinas virtuais:** isolamento de redes e sistemas para execução segura das práticas.
- **DevTools e `curl`:** inspeção de páginas, requisições, respostas e comportamento de endpoints.

## Como visualizar os projetos

Os projetos web podem ser abertos localmente pelo arquivo principal indicado em cada pasta. Os laboratórios Python possuem um `README.md` próprio com dependências, endereço local e cuidados de execução.

Para conhecer o raciocínio técnico por trás de cada atividade, recomendo começar pelo meu [catálogo técnico](catalogo.md).

## Uso responsável

Este material foi publicado para demonstrar minha formação e meu desenvolvimento profissional. Não autorizo o uso dos laboratórios para atacar sistemas de terceiros. Qualquer teste de segurança deve possuir autorização, escopo e responsabilidade sobre os dados envolvidos.

