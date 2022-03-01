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
| 01/03/2022 | 0.1.6 | Alteração da descrição do Timebox | Gabriel Moretti |
| 01/03/2022 | 0.1.7 | Descrição do Product Backlog, papéis no Scrum e Kanban | Mateus Franco |
| 01/03/2022 | 0.2 | Pequenas Correções e Finalização do Documento | Gabriel Mariano |

## 1. Introdução
Esse documento visa informar todas as metodologias, processos e práticas que serão utilizadas ao longo da execução do projeto do INDICAA, as descrevendo e detalhando como necessário.

## 2. Metodologias
Para a viabilização e o efetivo desenvolvimento do projeto serão utilizadas metodologias baseadas majoritariamente no Manifesto Ágil, de modo a promover alterações constantes e que sigam um planejamento com constantes mudanças. Um dos pilares do [Manifesto Ágil](https://agilemanifesto.org/iso/ptbr/manifesto.html) é a maior valorização de indivíduos e interações em detrimento a processos e ferramentas, fator que será de grande importância para o processo de desenvolvimento de software e para a consequente aprendizagem por parte de todos os indivíduos envolvidos mo projeto. Dentre as metodologias a serem utilizadas, estão o Scrum, o Kanban, o Extreme Programming (XP) e o Planning Poker.

### 2.1 Scrum
> "A estrutura do Scrum procura aproveitar a maneira como as equipes de fato trabalham, fornecendo ferramentas para se auto-organizarem e otimizarem em pouco tempo a rapidez e a qualidade do trabalho." Scrum: a arte de fazer o dobro do trabalho na metade do tempo, 2016

#### 2.1.1 Product Backlog
Lista emergente e ordenada do que é necessário para o desenvolvimento e melhora do produto. Nele contém as funcionalidades à serem implementadas, alterações em funcionalidades já existentes e correções de falhas. Mudanças no Product Backlog devem sempre ser um processo colaborativo e serem realizadas em todas as etapas da construção do produto.

#### 2.1.2 Pápeis 
- __Scrum Master:__ É o responsável pela eficiência do grupo, auxiliando a todos no entendimento do framework Scrum e atuando na gestão do grupo.
- __Product Owner:__ Responsável por aumentar o valor do produto a ser desenvolvido e na gestão do Product Backlog, comunicando com o time sobre o objetivo a ser atingido.
 - __DevOps:__ Atua na configuração do ambiente de desenvolvimento e homologação do produto. Visa também automatizar processos, como os testes. Visa atuar para que o projeto forneça uma entrega e integração contínuas.
 - __Arquiteto:__ Atua na decisão das melhores tecnologias a serem utilizadas pelo grupo durante o desenvolvimento do projeto. Atua em suporte ao DevOps.
 - __Desenvolvedor:__ Atua no desenvolvimento e teste do produto, criando o Sprint Backlog e adaptando seu plano de modo a atingir o objetivo definido ao final da Sprint.
 -  __Designer:__ Atua nas responsabilidades, operações, atributos e relacionamentos de elementos do design do produto, assegurando também que esse esteja consistente com a arquitetura do software.

#### 2.1.3 Sprints
- __Sprint:__ Sprints são os eventos principais do Scrum, tendo duração previamente projetada e constante durante todo o projeto. Uma sprint pode ter duração igual ou menor a um mês, sendo utilizado neste projeto o período fixado de uma semana. Na sprint são desenvolvidas todas as atividades do projeto conforme o planejado ao início desta.
- __Sprint Planning:__ O Sprint Planning é o evento que inicia a sprint, reunindo os membros da equipe para a definição do Sprint Backlog, um artefato que define as metas e atividades que devem ser executadas ao decorrer da sprint.
- __Sprint Backlog:__ O Sprint Backlog é um artefato gerado no Sprint Planning, conforme descrito no tópico anterior. Nele estão contidos os itens do product backlog a serem realizados pelos desenvolvedores.
- __Sprint Review:__ Realizada no final de cada sprint, o objetivo do Sprint Review é verificar o trabalho realizado durante a sprint e debater as mudanças que ocorreram no projeto.
- __Sprint Retrospective:__ A Sprint Retrospective é o último evento da sprint, tendo o objetivo de levantar pontos positivos e negativos do decorrer da sprint e debater como a produtividade e a qualidade do produto desenvolvido podem ser incrementadas. Basicamente a Sprint Retrospective busca avaliar o que foi bom ou ruim durante a sprint e agir para que os pontos positivos sejam mantidos e os pontos negativos sofram alterações.

#### 2.1.4 Time-Box
> "O Timebox é uma estratégia de gestão do tempo baseada em metas que ajuda a aumentar a produtividade e a reduzir a procrastinação. Quando se cria uma “caixa de tempo”, em tradução livre, também se define uma meta para que uma determinada tarefa seja realizada dentro de um intervalo predefinido." [Asana, 2021](https://asana.com/pt/resources/what-is-timeboxing)

 __Sprints:__
  
  Duração de 7 dias : Início na terça e término na segunda da outra semana. Poderão ser menores devido às releases : Mais curtas ou longas, conforme decisão do Scrum Master.
- __Daily Meeting:__ As dailies da equipe serão realizadas diariamente por meio do telegram, prioritariamente no período da manhã. Todos os membros têm como obrigação informar a respeito do andamento das suas atividades. Têm duração de 15 minutos.
- __Sprint Review:__ Ocorrerá ao final das sprints, na segunda ou no início da terça-feira, com duração de 30 minutos.
- __Sprint Retrospective:__ Ocorrerá ao final das sprints, na segunda ou no início da terça-feira, com duração de 30 minutos.
- __Sprint Planning:__ Será realizado ao início da sprint, na terça-feira, com duração de 2 horas.

Obs.: Por motivos externos ou decisão dos Scrum Masters, os processos citados no Time-Box podem ter sua duração ou horários alterados.

### 2.2 Kanban
> "A palavra japonesa 'kanban', que significa 'placa visual'."

Utilizaremos como um método de gerenciamento de fluxo de trabalho para definir, gerenciar e melhorar processos que fornecem trabalho de conhecimento, objetivando a visualização rápida do trabalho à ser realizado e a maximização da eficiência e produtividade.

Utilizaremos quadros Kanban para visualização do progresso do trabalho com as seguintes colunas: 
- __Product Backlog:__ Lista de todas as funcionalidades do projeto.
- __Sprint Backlog:__ Lista das funcionalidade que serão implementadas na sprint atual.
- __To Do:__ Lista de funcionalidades à serem realizadas.
- __In Progress:__ Lista de funcionalidade que estão sendo desenvolvidas.
- __Review:__ Lista de funcionalidades que devem ser revisadas.
- __In Test:__ Lista de funcionalidades que devem ser testadas.
- __Done:__ Lista de funcionalidades já desenvolvidas.
### 2.3 Extreme Programming (XP)
> "XP é um apelido carinhoso de uma nova metodologia de desenvolvimento designada Extreme Programming, com foco em agilidade de equipes e qualidade de projetos, apoiada em valores como simplicidade, comunicação, feedback e coragem [...]".  [DevMedia](https://www.devmedia.com.br/extreme-programming-conceitos-e-praticas/1498)

O Extreme Programming (XP) é uma metodologia ágil que visa o desenvolvimento de sistemas que entreguem o que é pedido pelo cliente, melhorando também o ambiente de trabalho dos desenvolvedores, de modo a propiciar a realização de trabalhos simples e de qualidade.
Dentre os pilares do XP, estão a **simplicidade**, a **comunicação**, o **feedback**, **respeito** e a **coragem** (de dizer "não").

Poderão ser utilizadas pelas equipes as seguintes práticas:
- **Small Releases** (Pequenas Entregas).
- **Acceptance Tests** (Testes de Aceitação).
- **CI/CD** (Integração Contínua/Entrega Contínua).
- **Pair Programing** (Programação em Pares).
- **Simple Design** (Simplicidade de Projeto).
- **Coding Standards** (Padronização do Código).

### 2.4 Planning Poker
> "O Planning Poker é uma técnica gamificada baseada em consenso para estimativa, usada principalmente para timeboxing em princípios ágeis. No pôquer de planejamento, os membros do grupo fazem estimativas jogando cartas numeradas viradas para baixo na mesa, em vez de pronunciá-las em voz alta. As cartas são reveladas e as estimativas são então discutidas. Ao ocultar os números dessa maneira, o grupo pode evitar o viés cognitivo da ancoragem , onde o primeiro número falado em voz alta abre um precedente para estimativas subsequentes." [Wikipédia, 2022](https://en.wikipedia.org/wiki/Planning_poker)

No nosso projeto utilizamos como referência a sequência de Fibonacci.

## 3. Plano de Comunicação
O Plano de Comunicação vem para assegurar que exista uma comunicação transparente entre a equipe, bem como documentar e organizar o conjunto de informações que a equipe gera durante todo o processo. Para que isto seja possível utilizaremos algumas ferramentar, tais como:
 - Discord - reuniões diárias, treinamentos e decisões relevantes do projeto.
 - Telegram - diálogo rápido, organização de eventos e decisões de baixo impacto.
 - Github - armazenamento de código fonte, transparência na realização de tarefas e documentação de iterações.

## 4. Interação entre Membros e Treinamentos
A interação entre os membros dos grupos envolvidos no projeto **INDICAA** se dará através de grupos em plataformas digitais, como o **Telegram** e o **Discord**, além da eventual comunicação nos comentários das **issues** do GitHub.

O compartilhamento de informações e o apoio em eventuais dúvidas e dificuldades é fortemente incentivado por todos os membros do projeto, atuando como pilar de uma "cultura" das equipes. Além disso, a proatividade e a interação entre membros de diferentes equipes são fatores importantes no desenvolvimento do projeto.

O incentivo a tais práticas parte, principalmente, dos(as) gestores(as) das equipes (Scrum Masters e Product Owners), todavia pode ser executado por quaisquer membros à disposição.

Durante a execução do projeto serão criadas issues para pesquisa de novas tecnologias e práticas de desenvolvimento, de modo a incentivar os membros a pesquisar e compartilhar conhecimento. Alem disso, aqueles(as) que possuem conhecimento prévio em determinadas tecnologias podem se voluntariar a instruir os outros em treinamentos, que serão realizados preferencialmente de maneira síncrona e podem ser disponibilizados para consulta posterior.

## 5. Referências

"Metodologia Ágil e Scrum". Disponível em: <https://metodologiaagil.com/>.

Manifesto Ágil. Disponível em: <https://agilemanifesto.org/iso/ptbr/manifesto.html>.

"O Guia Definitivo para o Scrum: As Regras do Jogo", por Ken Schwaber e Jeff Sutherland. Disponível em: <https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR.pdf>.

"Extreme Programming (XP): o que é, valores e benefícios". Disponível em: <https://www.objective.com.br/insights/extreme-programming-xp-o-que-e-e-beneficios/>.

"Extreme Programming – Conceitos e Práticas", por Manoel. Disponível em: <https://www.devmedia.com.br/extreme-programming-conceitos-e-praticas/1498#Releases>.

SUTHERLAND, Jeff: Scrum. A Arte de Fazer o Dobro do Trabalho na Metade do Tempo. Editora LeYa, 2016.

"O que é Timebox? 14 exemplos e casos de uso.". Disponível em <https://asana.com/pt/resources/what-is-timeboxing>.

Planning Poker. Disponível em: <https://en.wikipedia.org/wiki/Planning_poker>
