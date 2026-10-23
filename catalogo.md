# Catálogo técnico dos meus trabalhos

Neste catálogo explico com mais detalhes o que fiz em cada projeto, quais conceitos utilizei e como organizei meu raciocínio durante as práticas.

## Laboratórios de segurança de aplicações

### Rettah Auth Pentest Lab

Neste projeto trabalhei com uma aplicação Flask deliberadamente vulnerável. A ideia foi reunir diferentes falhas de autenticação em um ambiente que pudesse ser iniciado localmente e testado sem colocar sistemas reais em risco.

Estudei ausência de limitação de tentativas, uso de MD5 para senhas, comparação vulnerável a diferença de tempo, fixação de sessão, JWT aceito sem validação de assinatura e recuperação de senha com token previsível.

Minha lógica foi acompanhar cada fluxo completo. No login, por exemplo, observei desde a entrada do usuário até a consulta ao banco, a comparação da senha, a criação do token e o cookie devolvido ao navegador. Isso me ajudou a perceber que segurança não depende de um único controle: uma aplicação pode validar a senha e continuar vulnerável por causa da sessão ou da autorização.

As principais correções que identifiquei foram rate limiting, hash de senha apropriado, comparação segura, rotação de sessão, cookies com atributos de proteção, validação completa do JWT e tokens de recuperação aleatórios, curtos e de uso único.

**Ferramentas e tecnologias:** Python, Flask, SQLite, PyJWT, navegador e scripts locais de validação.

**Como usar:** consulte o [`README` do laboratório](laboratorios/rettah-auth-lab/README.md), instale as dependências e execute somente em `localhost` ou rede isolada.

### Portal do Aluno — SQL Injection

Criei este laboratório para visualizar por que a validação feita somente no navegador não protege o servidor. O formulário recebe matrícula e senha, mas a versão vulnerável concatena esses valores diretamente em uma consulta SQL.

Meu raciocínio foi seguir o caminho do dado: formulário, requisição, variável Python, construção da consulta e execução no SQLite. Quando percebi que a entrada era incorporada como parte do comando, a causa raiz ficou clara. A correção não é bloquear algumas palavras ou caracteres; é separar comandos e dados por meio de consultas parametrizadas.

Além da parametrização, considerei validação no servidor, mensagens de erro genéricas, privilégio mínimo, armazenamento seguro de senhas e testes de regressão.

**Ferramentas e tecnologias:** Python, Flask, SQLite e HTML.

**Como usar:** siga as instruções em [`portal-aluno-sqli`](laboratorios/portal-aluno-sqli/README.md). O código original utiliza uma porta que pode exigir privilégio; para prática local, recomendo uma porta alta, como 5000.

### Portal Acadêmico — SQL Injection com resultado no servidor

Este laboratório é uma evolução do exercício anterior. Nele, o banco é recriado a cada inicialização com dados fictícios, deixando a prática repetível e evitando dependência de informações reais.

Minha análise voltou a acompanhar o fluxo entre o formulário e o SQL, mas com atenção especial ao resultado retornado e renderizado pelo servidor. Isso mostrou como uma consulta alterada pode mudar não só o acesso, mas também os registros devolvidos à aplicação.

**Ferramentas e tecnologias:** Python, Flask, SQLite e templates HTML.

**Como usar:** consulte [`portal-academico-sqli`](laboratorios/portal-academico-sqli/README.md) e acesse o endereço local indicado após iniciar a aplicação.

## Redes, reconhecimento e pentest

### Análise em Metasploitable

Nesta atividade configurei máquinas virtuais em uma rede isolada. Primeiro confirmei o endereçamento para evitar conflito de IP. Depois usei descoberta de hosts para separar roteador, dispositivos auxiliares e máquina vulnerável.

Minha linha de raciocínio foi avançar do geral para o específico: descobrir quem estava na rede, verificar portas, identificar serviços e versões e, somente depois, estudar possíveis vulnerabilidades. Essa sequência reduz conclusões precipitadas e ajuda a registrar de onde cada hipótese surgiu.

Também aprendi que uma porta aberta representa uma superfície de exposição, mas não comprova sozinha uma falha. É necessário correlacionar serviço, versão, configuração, contexto e evidência.

**Ferramentas:** Nmap, Kali Linux, máquinas virtuais e editor de texto para registro dos alvos autorizados.

### Avaliação sem vulnerabilidade confirmada

Um dos meus relatórios registra uma situação em que encontrei hosts e serviços, mas não obtive evidência suficiente para confirmar uma vulnerabilidade.

Esse exercício foi importante porque mostrou que um bom relatório não precisa terminar com uma exploração. Ao encontrar respostas limitadas e possíveis controles de rede, documentei as tentativas, as limitações e as hipóteses sem declarar uma falha que não havia sido comprovada.

Minha conclusão foi separar claramente três estados: serviço identificado, vulnerabilidade possível e vulnerabilidade confirmada. Essa distinção torna o relatório mais confiável.

### Ambiente Windows legado em laboratório

Em uma máquina virtual legada, comecei pela descoberta do host e enumeração dos serviços. A presença de SMB direcionou a pesquisa para vulnerabilidades compatíveis com o sistema e a versão observada. A validação ocorreu somente dentro do laboratório autorizado.

Na versão pública removi hashes, credenciais e dados extraídos. O aprendizado profissional que preservo é o processo: evidência inicial, hipótese, validação controlada, avaliação de impacto e recomendação.

As recomendações incluem atualizar sistemas, remover protocolos obsoletos, segmentar a rede, limitar o acesso ao serviço e monitorar tentativas anormais.

**Ferramentas:** Nmap, Kali Linux, Metasploit em laboratório e ferramentas de análise de hashes para fins didáticos.

### Reconhecimento no scanme.nmap.org

Utilizei o `scanme.nmap.org`, disponibilizado pelo próprio projeto Nmap para testes autorizados, para praticar identificação das portas mais comuns e detecção de versões.

Minha lógica foi interpretar o resultado em vez de apenas copiar a saída. Analisei o estado das portas, o serviço provável e as informações de versão. Depois revisei uma conclusão importante: serviço acessível não é automaticamente vulnerável. Ele precisa ser comparado com configuração, versão corrigida, exposição necessária e validação dentro das regras do alvo.

**Ferramentas:** Nmap e Kali Linux.

### Segurança de e-mail

Estudei o caminho de uma mensagem entre cliente, servidor de envio e servidor de recebimento. Analisei o papel do SMTP, do acesso web, do Postfix e do Dovecot, além da diferença entre envelope, cabeçalho e corpo.

Depois relacionei essa arquitetura aos mecanismos SPF, DKIM e DMARC. Meu raciocínio foi entender primeiro onde a identidade do remetente pode ser manipulada e, em seguida, qual parte cada mecanismo protege. SPF autoriza servidores, DKIM adiciona uma assinatura verificável e DMARC define política e alinhamento.

**Ferramentas:** ambiente de e-mail didático, Thunderbird, Cisco Packet Tracer e análise de cabeçalhos.

## Segurança de aplicações web

### Pentest web em aplicação didática

Analisei autenticação, consultas SQL, sessões, tokens, autorização e recuperação de senha. Comecei observando o comportamento normal da aplicação e depois comparei as requisições e respostas com o que deveria acontecer em um fluxo seguro.

O Burp Suite foi útil para visualizar parâmetros e respostas HTTP. Minha lógica foi questionar cada fronteira de confiança: o que o navegador controla, o que o servidor valida, quais informações voltam na resposta e se uma identidade autenticada também possui autorização para aquela ação.

As recomendações principais foram consultas parametrizadas, redução de informações nas respostas, tokens imprevisíveis e de uso único, cookies seguros, verificação de assinatura JWT e autorização aplicada no servidor.

**Ferramentas:** Burp Suite, DevTools, navegador, Python, Flask e SQLite.

### Evident Crime — cadeia de risco em nuvem

Neste estudo acadêmico analisei como pequenas exposições podem formar uma cadeia maior: código público, documentação de API, armazenamento em nuvem e controle de identidade.

Meu raciocínio foi correlacionar pistas em vez de tratar cada descoberta de forma isolada. Uma informação exposta pode parecer de baixo impacto, mas pode revelar um endpoint; o endpoint pode exigir um token; um token exposto pode permitir acesso adicional. Foi nesse encadeamento que avaliei o risco.

Como o material original contém detalhes operacionais e foi marcado como confidencial, publiquei somente a síntese. As recomendações incluem remoção e rotação de segredos, revisão do histórico, IAM com privilégio mínimo, restrição de buckets, proteção de metadados e monitoramento.

### VulnBank — avaliação de aplicação web

Neste exercício identifiquei e relacionei classes de vulnerabilidade como SQL Injection, XSS, CSRF, SSRF, falhas de autorização, GraphQL exposto, prompt injection e vazamento de tokens.

Minha principal evolução foi deixar de olhar cada falha apenas pela severidade individual e começar a pensar em cadeia de ataque. Uma falha pode permitir entrada, outra elevação de acesso e uma terceira exposição de dados. Por isso, organizei os achados por impacto e possibilidade de combinação.

Mantive fora da versão pública dados de clientes, tokens, evidências e instruções operacionais contra o alvo. Preservei as recomendações: autorização por objeto, output encoding, proteção contra CSRF, restrição de saída para SSRF, proteção de segredos e telemetria.

## Criptografia

### Assinaturas digitais

Neste trabalho estudei como uma assinatura digital fornece autenticidade, integridade e não repúdio. Parti da limitação da criptografia simétrica: se duas pessoas compartilham a mesma chave, não é possível provar qual delas produziu uma mensagem.

Depois analisei criptografia assimétrica, par de chaves, função hash, assinatura com chave privada e verificação com chave pública. A parte mais importante para mim foi entender que o algoritmo sozinho não resolve todo o problema; também é necessário proteger a chave privada e confiar corretamente no certificado e na infraestrutura de chaves públicas.

**Conceitos:** hash, RSA, RSA-PSS, chaves assimétricas, certificados, PKI, autenticidade, integridade e não repúdio.

## Desenvolvimento web

### Site de pizzaria

Desenvolvi um site com páginas de apresentação, cardápio, promoções, delivery, reservas, contato e unidades. Organizei uma folha de estilos compartilhada e mantive navegação consistente entre as páginas.

Minha lógica foi pensar na jornada de quem acessa: conhecer o estabelecimento, visualizar opções e encontrar o canal adequado para pedir, reservar ou entrar em contato.

**Tecnologias:** HTML e CSS. As imagens não foram publicadas porque eu não consegui confirmar a licença de redistribuição.

### Site institucional de curso

Criei uma página para apresentar um curso e conduzir a pessoa interessada a um formulário de inscrição. Trabalhei hierarquia de informações, chamada para ação e campos de cadastro.

Ao revisar o projeto pela perspectiva de segurança, identifiquei que um formulário real precisaria de HTTPS, backend seguro, validação no servidor, consentimento, minimização de dados e política de retenção.

**Tecnologias:** HTML e estrutura de formulário.

### Site temático de artista

Desenvolvi páginas de início, biografia, discografia, notícias, galeria e formulário. Também implementei JavaScript para carrossel, lightbox, máscaras e validações.

Esse projeto me ajudou a separar estrutura, aparência e comportamento. Também reforçou que validação no navegador melhora a experiência, mas não pode ser considerada controle de segurança porque o cliente pode ser alterado.

**Tecnologias:** HTML, CSS e JavaScript. Fotos e vídeos de terceiros ficaram fora da publicação.

## Conscientização e comunicação

### Jogo Vida Digital

Participei da criação de um material que transforma situações de segurança em decisões de jogo, incluindo senhas fracas, redes públicas, golpes, proteção de conexão, atualização de credenciais e compartilhamento de dados.

O objetivo foi explicar segurança sem depender de linguagem técnica. Essa atividade mostrou que conscientização funciona melhor quando a pessoa consegue relacionar o risco a uma decisão cotidiana.

### Resolução de conflitos

Estudei escuta, diálogo, autocontrole e busca de soluções equilibradas. Relacionei essa competência ao trabalho técnico porque incidentes, auditorias e correções dependem da colaboração entre pessoas e áreas diferentes.

Aprendi que comunicar um risco não significa procurar culpados. Uma boa comunicação descreve evidência, impacto, prioridade e próximo passo de forma respeitosa e objetiva.

## O que mantive fora da publicação

Alguns arquivos originais não aparecem diretamente neste repositório porque continham hashes, flags, tokens, dados pessoais, detalhes de alvos, marcação de confidencialidade, material de outros grupos ou mídia sem licença confirmada. Nesses casos, escrevi uma versão sanitizada que preserva meu raciocínio e os aprendizados sem expor outras pessoas ou organizações.

