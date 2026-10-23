# Catálogo técnico do portfólio

## Laboratórios de segurança de aplicações

### Rettah Auth Pentest Lab

Aplicação Flask deliberadamente vulnerável criada para estudar falhas de autenticação de forma reproduzível. A construção se baseia na ideia de comparar uma implementação insegura com controles defensivos: limitação de tentativas, armazenamento moderno de senhas, rotação de sessão, validação de assinatura JWT e tokens de recuperação imprevisíveis.

Na prática, o laboratório permite observar por que segredos fixos, MD5, cookies controlados pelo cliente, JWT sem verificação e respostas que expõem tokens quebram as garantias de confidencialidade e autenticidade. O principal aprendizado é transformar a exploração em requisito de correção verificável. Uso exclusivamente local e autorizado.

### Portal do Aluno — SQL Injection

Aplicação Flask/SQLite feita para demonstrar que validação no navegador não é controle de segurança. A consulta SQL é construída de forma propositalmente insegura, permitindo estudar a diferença entre entrada de usuário e instrução executável.

A base conceitual é a separação entre dados e comandos. A remediação correspondente é usar consultas parametrizadas, validação no servidor, mensagens de erro genéricas, privilégio mínimo e testes automatizados contra entradas maliciosas.

### Portal Acadêmico — SQL Injection com resultado no servidor

Evolução do laboratório anterior, com banco recriado a cada inicialização para garantir repetibilidade. O exercício ajuda a visualizar como a concatenação de strings afeta o conjunto de resultados devolvido pelo servidor e como um ambiente descartável facilita testes seguros.

O aprendizado central é que filtros superficiais não substituem parametrização, modelagem de ameaça e revisão de código.

## Estudos de caso de pentest e análise

### Metasploitable e análise de vulnerabilidades

Exercício em rede virtual isolada envolvendo descoberta de hosts, identificação de serviços e análise de exposição. A prática foi baseada em inventário progressivo: primeiro saber quais hosts existem, depois quais portas respondem e, por fim, quais versões e riscos precisam ser validados.

O estudo reforçou segmentação, autorização, registro de evidências e a diferença entre uma porta aberta e uma vulnerabilidade comprovada.

### Avaliação de serviço sem vulnerabilidade confirmada

Caso importante de resultado negativo: o reconhecimento encontrou serviços, mas as evidências não sustentaram exploração. O trabalho mostra maturidade ao evitar transformar hipótese em achado e ao documentar limitações, possíveis controles de rede e próximos passos de validação.

### Ambiente Windows legado em laboratório

Avaliação controlada de uma máquina virtual legada, passando por descoberta, enumeração SMB, validação de falha conhecida e discussão de impacto. A versão pública remove hashes e dados extraídos. As recomendações incluem atualização, desativação de protocolos obsoletos, segmentação, restrição de acesso e monitoramento.

### Segurança de e-mail

Estudo do fluxo entre cliente e servidores de correio, com SMTP, acesso web, Postfix e Dovecot, seguido de mecanismos de confiança como SPF, DKIM e DMARC. A prática conectou arquitetura, autenticação de domínio e análise de cabeçalhos à prevenção de spoofing e fraude.

### Nmap e reconhecimento autorizado

Atividade sobre descoberta de hosts, portas e versões utilizando um alvo público criado para testes. O aprendizado inclui leitura crítica do resultado: porta aberta não significa, por si só, vulnerabilidade. A evidência precisa ser correlacionada com versão, configuração, contexto e validação autorizada.

### Pentest de aplicação web em laboratório

Avaliação de autenticação, consultas SQL, gerenciamento de sessão, exposição de informações e recuperação de senha em aplicação didática. O método combinou observação no navegador, interceptação de requisições e revisão de respostas.

A versão pública enfatiza causas e correções: consultas parametrizadas, mensagens mínimas, tokens aleatórios e de uso único, cookies seguros, validação de JWT e controles de autorização no servidor.

### Evident Crime — cadeia de risco em nuvem

Estudo acadêmico de como exposição de código ou token, documentação de API e configurações frágeis de armazenamento podem compor uma cadeia de ataque. Por ter sido marcado como confidencial e conter detalhes operacionais de alvo, o relatório original não é publicado.

O valor técnico preservado está no raciocínio: reduzir exposição pública, remover segredos do histórico, rotacionar credenciais, aplicar IAM de privilégio mínimo, restringir buckets, proteger metadados e monitorar uso anômalo.

### VulnBank — avaliação web

Estudo de múltiplas classes de falha — autenticação, autorização, injeção, XSS, CSRF, SSRF, GraphQL e exposição de tokens — e de como vulnerabilidades combinadas ampliam impacto. A versão pública omite dados de clientes e instruções operacionais contra o alvo.

O aprendizado principal foi priorizar cadeias de ataque pelo impacto de negócio e recomendar defesa em profundidade: validação contextual, output encoding, tokens anti-CSRF, autorização por objeto, restrição de egress, proteção de segredos e telemetria.

## Criptografia e confiança digital

### Assinaturas digitais

Trabalho técnico sobre autenticidade, integridade e não repúdio. A construção parte da limitação da criptografia simétrica para provar autoria e avança para pares de chaves, funções hash, assinatura com chave privada e verificação com chave pública.

Também relaciona algoritmos e padrões a aplicações reais, como documentos eletrônicos, certificados e infraestrutura de chaves públicas. A competência demonstrada é explicar não apenas o algoritmo, mas o modelo de confiança e a proteção da chave privada.

## Desenvolvimento web

### Site de pizzaria

Site multipágina em HTML e CSS, com home, cardápio, promoções, delivery, reservas, contato e unidades. Foi criado para praticar arquitetura de informação, navegação consistente, organização visual e formulários. A publicação prioriza o código; mídias sem licença comprovada ficam fora do portfólio.

### Site institucional de curso

Página acadêmica para divulgação de curso e formulário de inscrição. A atividade trabalhou hierarquia de conteúdo, chamada para ação, organização de informações e captura de dados no front-end. Em uma aplicação real, o formulário exigiria backend seguro, consentimento e proteção dos dados enviados.

### Site temático de artista

Projeto multipágina para praticar layout, biografia, discografia, notícias, galeria e formulário. O código demonstra estruturação de páginas e reutilização de estilos. Fotos, músicas e vídeos de terceiros não são redistribuídos, pois a licença não foi confirmada.

## Comunicação, cidadania digital e trabalho em equipe

### Jogo Vida Digital

Material lúdico de conscientização que traduz riscos digitais em decisões de jogo: senhas fracas, redes abertas, golpes, proteção de conexão, atualização de credenciais e compartilhamento responsável. Demonstra capacidade de comunicar segurança para público não técnico.

### Resolução de conflitos

Apresentação sobre escuta, diálogo, autocontrole e busca de soluções equilibradas. A competência é relevante à segurança porque incidentes, auditorias e correções exigem colaboração entre áreas, comunicação de risco sem culpabilização e negociação de prioridades.

