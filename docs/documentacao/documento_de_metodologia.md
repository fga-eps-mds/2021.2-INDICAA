# Plano de Metodologia e Processos

## Histórico de Versão

| Data | Versão | Descrição | Autor(es/as) |
| :--: | :----: | :-------: | :-------: |
| 26/02/2022 | 0.1 | Criação do Documento | Gabriel Mariano, Gabriel Moretti, Mateus Franco |
| 27/02/2022 | 0.1.1 | Adição das Referências e Planning Poker | João Paulo |
| 27/02/2022 | 0.1.2 | Alteração dos conceitos e atribuições das personas do Scrum| João Paulo |

## 1. Introdução
[//]: <> (Moretti)
Esse documento é responsável por elicitar e descrever todas as metodologias e processos que serão utilizadas ao longo da execução do projeto.

## 2. Metodologias
[//]: <> (Mariano)
A combinação das metodologias aqui presentes tem como objetivo construir um processo de desenvolvimento de software consistente e ágil. Estando atentos ao manifesto Ágil - "Indivíduos e interações mais que processos e ferramentas" [Manifesto Ágil](https://www.manifestoagil.com.br) - o nosso plano não busca seguir metodologias à risca, e sim se valer de adaptações que melhor de adequam a equipe.

### 2.1 Scrum
[//]: <> (Moretti)
> "É um  framework no qual as pessoas podem lidar com problemas complexos e, ao mesmo tempo, fornecer produtos de maneira mais criativa e produtiva."[ScrumGuides, 2019](https://scrumguides.org/scrum-guide.html)

#### 2.1.1 Product Backlog
[//]: <> (Mateus)
Artefato que contém as funcionalidade desejadas, sendo este passível de modificação a qualquer etapa do processo.

#### 2.1.2 Pápeis 
[//]: <> (Mateus)
- __Scrum Master:__ Responsável por remover impedimentos relacionados ao desenvolvimento; Minimizar riscos do projeto; Garantir a disseminação de contéudo entre os membros da equipe; Monitorar e aperfeiçoar a produtividade da equipe utilizando métricas bem definidas; Garantir que a metodologia seja aplicada.
- __Product Owner:__ Responsável por trazer a visão de produto às decisões do time; Analisar e priorizar os pontos mais valiosos, do ponto de vista dos stakeholders; E Definir critérios de aceitação considerando visão do cliente.
 - __DevOps:__ Responsável por manter o projeto nas diretrizes da cultura devops e tomar decisoes que garatem que o ambiente desevolvimento esteja também sob essas diretrizes.
 - __Arquiteto:__ Responsável por modelar a arquitetura do sistema e garantir que ela está sendo seguida no desenvolvimento; E monitorar qualidade do código.
 - __Desenvolvedor:__ Responsável por programar as histórias de usuário; Seguir técnicas de programação; E realizar testes no código produzido.

#### 2.1.3 Sprints
[//]: <> (Mariano)
- __Sprint:__ No Scrum "sprint" é como chamamos uma iteração no processo de desenvolvimento. Geralmente tem duração de uma semana ou no máximo um mês, podendo ser adaptável as necessidades da equipe.
- __Sprint Backlog:__ Artefato gerado sempre no início de uma nova iteração. Contém as tarefas que serão realizadas durante esta nova iteração.
- __Sprint Planning:__ Reunião onde é feito o planejamento estrátegico e a definição dos objetivos de uma nova sprint, ou seja, de uma nova iteração, nela é criado o artefato sprint backlog citado à cima.
- __Sprint Review:__ Realizada no final de cada sprint para mostrar o que foi alcançado e avaliar a relação entre o que está sendo desenvolvido e os objetivos da sprint.
- __Sprint Retrospective:__ Ocorre ao final de cada sprint, assim como a sprint review. Tem objetivo de cumprir manter o pilar de inspeção do scrum, nela são avaliados os pontos positivos e negativos da sprint que se finalizou. As informações coletadas norteiam a equipe para um melhoramento de seu processo de desenvolvimento.

#### 2.1.4 Time-Box
[//]: <> (Moretti)
> "É um conceito que diz que a quantidade de tempo (horas ou dias, o que depende das unidades sendo utilizadas para um determinado projeto) é imutável, ou seja, a quantidade de horas não poderá aumentar caso algum problema ou novo requisito seja identificado." [PortalEducação, 2019](https://www.portaleducacao.com.br/conteudo/artigos/informatica/timebox-projeto-scrum/40658)

__Sprints:__
  Duração de 7 dias : Início no domingo e término no sábado da outra semana.Poderão ser menores devido as releases : Mais curtas ou longas, conforme decisão do Scrum Master.
- __Daily Meeting:__ As dailies da equipe serão realizadas diariamente por meio do telegram, prioritariamente no período da manhã. Todos os membros têm como obrigação informar a respeito do andamento das suas atividades.
- __Sprint Review:__ Ocorrerão aos sábados, iniciando às 14h.
- __Sprint Restropective:__ Ocorrerá aos sábados, iniciando às 15:30h.
- __Sprint Planning:__ Será realizado nas reuniões de sábado.

### 2.2 Kanban
[//]: <> (Mateus)
"Em administração da produção, kanban é um cartão de sinalização que controla os fluxos de produção ou transportes em uma indústria."[Wikipédia, 2019](https://pt.wikipedia.org/wiki/Kanban#Scrum_e_Kanban)

Para nós, o kanban será um cartão de sinalização que possuirá os seguintes quadros:
- __Project Backlog:__ Lista de todas as funcionalidades do projeto.
- __Sprint Backlog:__ Lista das funcionalidade que serão implemntadas na sprint atual.
- __To Do:__ Lista de funcionalidades que devem ser feitas.
- __In Progress:__ Lista de funcionalidade que estão sendo desenvolvidas.
- __Review:__ Lista de funcionalidades que devem ser revisadas.
- __In Test:__ Lista de funcionalidades que devem ser testadas.
- __Done:__ Lista de funcionalidades já desenvolvidas.

### 2.3 eXtreme Programming
[//]: <> (Mariano)
> "Extreme Programming (XP) é uma estrutura de desenvolvimento de software ágil que visa produzir software de maior qualidade e maior qualidade de vida para a equipe de desenvolvimento."[Agile Aliance]( https://www.agilealliance.org)

Serão utilizados pela equipe as seguintes práticas:
- Small Realeases - Pequenas entregas.
- Testing - Cobertura de código testado de 90%.
- Refactoing - Existência de uma sprint de refatoração a cada 3 sprints.
- Pair Programing - Programação em pares com rotatividades para gestão do conhecimento.
- Coding Standard: Padronização do código com folha de estilo.

### 2.4 Planning Poker
[//]: <> (Moretti)
"O Planning Poker é uma técnica gamificada baseada em consenso para estimativa, usada principalmente para timeboxing em princípios ágeis. No pôquer de planejamento, os membros do grupo fazem estimativas jogando cartas numeradas viradas para baixo na mesa, em vez de pronunciá-las em voz alta. As cartas são reveladas e as estimativas são então discutidas. Ao ocultar os números dessa maneira, o grupo pode evitar o viés cognitivo da ancoragem , onde o primeiro número falado em voz alta abre um precedente para estimativas subsequentes." [Wikipédia, 2022](https://en.wikipedia.org/wiki/Planning_poker)

No nosso projeto utilizamos como referência a sequência de Fibonacci.

## 3. Plano de Comunicação
[//]: <> (Mateus)
O Plano de Comunicação vem para assegurar que exista uma comunicação transparente entre a equipe, bem como documentar e organizar o conjunto de informações que a equipe gera durante todo o processo. Para que isto seja possível utilizaremos algumas ferramentar, tais como:
 - Discord - dailys remotas.
 - Telegram - diálogo diaŕio e decisões de baixo impacto.
 - Drive - informações da equipe e insumos para viabilizar o projeto.
 - Github- armazenamento de código fonte, transparência na realização de tarefas,documentação de iterações.

## 4. Interação entre Membros e Treinamentos
[//]: <> (Mariano)
> "Gamificação é a utilização de técnicas de design de jogos para incentivar produtividade e/ou mudanças de comportamento."

Visando manter a produtividade, o Colaborativismo e a melhoria continua da relação entre membros a equipe utilizará de tecnicas de gamificação, tais como:

- Sharing Knowledge: Incentivar compartilhamento de conhecimento.
- Certificates: Reconhecimento atráves de certificados, medalhas e etc.

Vale lembrar que algumas dessas tecnicas serão intrisicamente aplicadas pela equipe gestora.

Obs.: As técnicas foram escolhidas com base no perfil que foi traçado da equipe. Essa informação pode ser encontrada [aqui](https://docs.google.com/spreadsheets/d/1temwG93TrqvCTuy1u52Qbi-JIHFtpjNwILdbRSehMHg/edit?usp=sharing).

## 5. Referências
[//]: <> (Todos)

Manifesto Ágil. Disponível em: https://www.manifestoagil.com.br/

Metodologia Scrum. Disponível em: https://www.desenvolvimentoagil.com.br

Scrum Guides. Disponível em: https://scrumguides.org/scrum-guide.html

Bartle, R. a. (1999). Players Who Suit MUDs. Retrieved March 22, 2015, from http://mud.co.uk/richard/hcds.htm

Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. The American Psychologist, 55, 68–78. http://doi.org/10.1037/0003-066X.55.1.68

Pink, D. H. (2009). Drive: The surprising truth about what motivates us. Distribution (p. 256). Canongate. Most of the icons are available at game-icons.net. For more information, check the icons accreditation info here.

Sigmund, K., & Hauert, C. (2002). Altruism. Current Biology. https://doi.org/10.1016/S0960-9822(02)00797-2

Extreme Programing Glossary. Disponível em: https://www.agilealliance.org

When should Extreme Programming be Used?. Disponível em: http://www.extremeprogramming.org

What is Extreme Programming?. Disponível em: https://ronjeffries.com/xprog/what-is-extreme-programming/

Planning Poker. Disponível em: https://en.wikipedia.org/wiki/Planning_poker
