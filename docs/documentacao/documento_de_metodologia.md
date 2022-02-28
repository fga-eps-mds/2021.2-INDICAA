# Plano de Metodologia e Processos

## Histórico de Versão

| Data | Versão | Descrição | Autor(es/as) |
| :--: | :----: | :-------: | :-------: |
| 26/02/2022 | 0.1 | Criação do Documento | Gabriel Mariano, Gabriel Moretti, Mateus Franco |
| 27/02/2022 | 0.1.1 | Adição das Referências e Planning Poker | João Paulo |
| 27/02/2022 | 0.1.2 | Alteração dos conceitos e atribuições das personas do Scrum| João Paulo |
| 28/02/2022 | 0.1.3 | Descrição das metodologias e das sprints | Gabriel Mariano |
| 28/02/2022 | 0.1.4 | Descrição do extreme programming e das interações | Gabriel Mariano |
| 28/02/2022 | 0.1.5 | Introdução ao documento e ao Scrum | Gabriel Moretti |

## 1. Introdução
Esse documento visa informar todas as metodologias, processos e práticas que serão utilizadas ao longo da execução do projeto do INDICAA, as descrevendo e detalhando como necessário.

## 2. Metodologias
Para a viabilização e o efetivo desenvolvimento do projeto serão utilizadas metodologias baseadas majoritariamente no Manifesto Ágil, de modo a promover alterações constantes e que sigam um planejamento com constantes mudanças. Um dos pilares do [Manifesto Ágil](https://agilemanifesto.org/iso/ptbr/manifesto.html) é a maior valorização de indivíduos e interações em detrimento a processos e ferramentas, fator que será de grande importância para o processo de desenvolvimento de software e para a consequente aprendizagem por parte de todos os indivíduos envolvidos mo projeto. Dentre as metodologias a serem utilizadas, estão o Scrum, o Kanban, o Extreme Programming (XP) e o Planning Poker.

### 2.1 Scrum
> "A estrutura do Scrum procura aproveitar a maneira como as equipes de fato trabalham, fornecendo ferramentas para se auto-organizarem e otimizarem em pouco tempo a rapidez e a qualidade do trabalho." Scrum: a arte de fazer o dobro do trabalho na metade do tempo, 2016

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
- __Sprint:__ Sprints são os eventos principais do Scrum, tendo duração previamente projetada e constante durante todo o projeto. Uma sprint pode ter duração igual ou menor a um mês, sendo utilizado neste projeto o período fixado de uma semana. Na sprint são desenvolvidas todas as atividades do projeto conforme o planejado ao início desta.
- __Sprint Planning:__ O Sprint Planning é o evento que inicia a sprint, reunindo os membros da equipe para a definição do Sprint Backlog, um artefato que define as metas e atividades que devem ser executadas ao decorrer da sprint.
- __Sprint Backlog:__ O Sprint Backlog é um artefato gerado no Sprint Planning, conforme descrito no tópico anterior. Nele estão contidos os itens do product backlog a serem realizados pelos desenvolvedores.
- __Sprint Review:__ Realizada no final de cada sprint, o objetivo do Sprint Review é verificar o trabalho realizado durante a sprint e debater as mudanças que ocorreram no projeto.
- __Sprint Retrospective:__ A Sprint Retrospective é o último evento da sprint, tendo o objetivo de levantar pontos positivos e negativos do decorrer da sprint e debater como a produtividade e a qualidade do produto desenvolvido podem ser incrementadas. Basicamente a Sprint Retrospective busca avaliar o que foi bom ou ruim durante a sprint e agir para que os pontos positivos sejam mantidos e os pontos negativos sofram alterações.

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

### 2.3 Extreme Programming (XP)
> "XP é um apelido carinhoso de uma nova metodologia de desenvolvimento designada Extreme Programming, com foco em agilidade de equipes e qualidade de projetos, apoiada em valores como simplicidade, comunicação, feedback e coragem [...]". [DevMedia](https://www.devmedia.com.br/extreme-programming-conceitos-e-praticas/1498)

O Extreme Programming (XP) é uma metodologia ágil que visa o desenvolvimento de sistemas que entreguem o que é pedido pelo cliente, melhorando também o ambiente de trabalho dos desenvolvedores, de modo a propiciar a realização de trabalhos simples e de qualidade.
Dentre os pilares do XP, estão a **simplicidade**, a **comunicação**, o **feedback**, **respeito** e a **coragem** (de dizer NÃO).

Poderão ser utilizadas pelas equipes as seguintes práticas:
- **Small Releases** (Pequenas Entregas).
- **Acceptance Tests** (Testes de Aceitação).
- **CI/CD** (Integração Contínua/Entrega Contínua).
- **Pair Programing** (Programação em Pares).
- **Simple Design** (Simplicidade de Projeto).
- **Coding Standards** (Padronização do Código).

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
A interação entre os membros dos grupos envolvidos no projeto **INDICAA** se dará através de grupos em plataformas digitais, como o _Telegram_ e o _Discord_, além da eventual comunicação nos comentários das _issues_ do GitHub.

O compartilhamento de informações e o apoio em eventuais dúvidas e dificuldades é fortemente incentivado por todos os membros do projeto, atuando como pilar de uma "cultura" das equipes. Além disso, a proatividade e a interação entre membros de diferentes equipes são fatores importantes no desenvolvimento do projeto.

O incentivo à tais práticas parte, principalmente, dos(as) gestores(as) das equipes (Scrum Masters e Product Owners), todavia pode ser executado por quaisquer membros à disposição.

Durante a execução do projeto serão criadas issues para pesquisa de novas tecnologias e práticas de desenvolvimento, de modo a incentivar os membros à pesquisar e compartilhar conhecimento. Alem disso, aqueles(as) que possuem conhecimento prévio em determinadas tecnologias podem se voluntariar a instruir os outros em treinamentos, que serão realizados preferencialmente de maneira síncrona e podem ser disponibilizados para consulta posterior.

## 5. Referências
[//]: <> (Todos)

"Metodologia Ágil e Scrum". Disponível em: <https://metodologiaagil.com/>.

Manifesto Ágil. Disponível em: <https://agilemanifesto.org/iso/ptbr/manifesto.html>.

"O Guia Definitivo para o Scrum: As Regras do Jogo", por Ken Schwaber e Jeff Sutherland. Disponível em: <https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR.pdf>.

"Extreme Programming (XP): o que é, valores e benefícios". Disponível em: <https://www.objective.com.br/insights/extreme-programming-xp-o-que-e-e-beneficios/>.

"Extreme Programming – Conceitos e Práticas", por Manoel. Disponível em: <https://www.devmedia.com.br/extreme-programming-conceitos-e-praticas/1498#Releases>.

SUTHERLAND, Jeff: Scrum. A Arte de Fazer o Dobro do Trabalho na Metade do Tempo. Editora LeYa, 2016.


[//]: <> (A partir daqui estão as referências utilizadas anteriormente pela equipe do Acácia)

Metodologia Scrum. Disponível em: https://www.desenvolvimentoagil.com.br

Bartle, R. a. (1999). Players Who Suit MUDs. Retrieved March 22, 2015, from http://mud.co.uk/richard/hcds.htm

Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. The American Psychologist, 55, 68–78. http://doi.org/10.1037/0003-066X.55.1.68

Pink, D. H. (2009). Drive: The surprising truth about what motivates us. Distribution (p. 256). Canongate. Most of the icons are available at game-icons.net. For more information, check the icons accreditation info here.

Sigmund, K., & Hauert, C. (2002). Altruism. Current Biology. https://doi.org/10.1016/S0960-9822(02)00797-2

Extreme Programing Glossary. Disponível em: https://www.agilealliance.org

When should Extreme Programming be Used?. Disponível em: http://www.extremeprogramming.org

What is Extreme Programming?. Disponível em: https://ronjeffries.com/xprog/what-is-extreme-programming/

Planning Poker. Disponível em: https://en.wikipedia.org/wiki/Planning_poker