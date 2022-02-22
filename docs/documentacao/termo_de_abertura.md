# Termo de Abertura do Projeto
***

### Histórico de Versões
**Data** | **Versão** | **Descrição** | **Autor(es/as)**
--- | --- | --- | --- 
28/01/2022 | 0.1 | Versão Inicial | Matheus Pimentel Leal, Gabriel Mariano da Silva e Guilherme Barbosa Ferreira
31/01/2022 | 0.2 | Pequenas Correções | Gabriel Mariano da Silva
17/02/2022 | 0.3 | Inserção dos Requisitos de Alto Nível | Gabriel Moretti de Souza e Matheus Pimentel Leal
18/02/2022 | 0.3.1 | Pequenas Correções e Adição da descrição ao papel do Designer | Gabriel Moretti de Souza

### Siglas
**Sigla** | **Descrição**
--- | ---
SIGAA | Sistema Integrado de Gestão de Atividades Acadêmicas
INDICAA | Nome dado ao projeto relativo aos indicadores do SIGAA
UnB | Universidade de Brasília
FGA | Faculdade do Gama

## 1. Introdução
Este documento visa informar as principais características do projeto **INDICAA** de forma concisa e clara para a leitura de todos os interessados no projeto e nas suas etapas de execução e decisão. Abaixo serão tratados os seguintes tópicos relacionados a este projeto: descrição, propósito e justificativa, objetivos, partes interessadas (usuários e envolvidos no desenvolvimento), requisitos de alto nível, análise de riscos, requisitos para a aprovação seguindo a definition of done estabelecida e estratégias de comunicação.

## 2. Descrição
O projeto **INDICAA** foi proposto pela profª Carla Silva Rocha Aguiar e consiste em realizar a criação de uma aplicação para facilitar a busca por informações no site SIGAA que é utilizado por alunos e professores da UnB. As informações relacionadas a cada curso, que serão disponibilizadas são:
* Quantidade de disciplinas
* Quantidade de vagas ofertadas
* Quantidade de alunos matriculados
* Quantidade de salas disponíveis

## 3. Propósito e justificativa
Tendo em vista que o contexto pandêmico trouxe uma nova forma de comunicação e interação, dificuldades de manejo das tecnologias são constantemente encontradas por seus usuários no mundo todo. A comunidade acadêmica da UnB não é exceção. Com isso, o **INDICAA** visa trazer uma forma facilitada e intuitiva de busca por informações no SIGAA.

## 4. Objetivos
O objetivo do **INDICAA** é ofertar um painel com os dados da lista de oferta de disciplinas do SIGAA dispostos de maneira intuitiva, de modo a facilitar a visualização das informações necessárias dos cursos, como a quantidade de disciplinas ofertadas, a quantidade de vagas disponíveis, a quantidade de alunos matriculados e a quantidade de salas disponíveis.
Atualmente, a lista de ofertas do SIGAA é composta por uma grande quantidade de dados dispostos separadamente. O _software_ desenvolvido facilitaria o entendimento destes dados e auxiliaria na tomada de decisões com base nas informações disponibilizadas.

## 5. Partes interessadas
### 5.1 Usuários
O público-alvo consiste na comunidade da Universidade de Brasília, isto é, coordenadores, professores e estudantes, basicamente.
**Usuário** | **Descrição**
--- | ---
Coordenadores | Comunidade administrativa da UnB que visa, através dos dados disponibilizados dos cursos, tomar decisões que melhorem a organização destes.
Professores | Comunidade de docentes da UnB que visa obter informações sobre as matérias ofertadas, as salas disponíveis e a quantidade de alunos matriculados em suas matérias.
Estudantes | Comunidade de discentes da UnB que buscam informações relativas às disciplinas, como a quantidade de vagas disponíveis e as respectivas salas.
Outros | Quaisquer indivíduos que optarem por acessar dados relativos aos cursos da UnB.

### 5.2 Equipes e papéis
#### Definição dos papéis:
**Usuário** | **Descrição**
--- | ---
_Scrum Master_ | É o responsável pela eficiência do grupo, auxiliando a todos no entendimento do _framework Scrum_ e atuando na gestão do grupo.
_Product Owner_ | Responsável por aumentar o valor do produto a ser desenvolvido e na gestão do _Product Backlog_, comunicando com o time sobre o objetivo a ser atingido.
Arquiteto de Software | Atua na decisão das melhores tecnologias a serem utilizadas pelo grupo durante o desenvolvimento do projeto. Atua em suporte ao DevOps.
DevOps | Atua na configuração do ambiente de desenvolvimento e homologação do produto. Visa também automatizar processos, como os testes. Visa atuar para que o projeto forneça uma entrega e integração contínuas.
Desenvolvedor | Atua no desenvolvimento e teste do produto, criando o _Sprint Backlog_ e adaptando seu plano de modo a atingir o objetivo definido ao final da _Sprint_.
_Designer_ | Atua nas responsabilidades, operações, atributos e relacionamentos de elementos do _design_ do produto, assegurando também que esse esteja consistente com a arquitetura do software.

#### Grupo 1
**Usuário** | **Descrição**
--- | ---
_Scrum Master_ | Laura Pinos de Oliveira
_Product Owner_ | Caio César Oliveira
Arquiteto de Software | Lucas Henrique Lima de Queiroz
DevOps | Vitor Eduardo Kühl Rodrigues
Desenvolvedor | Matheus Costa Gomes
_Designer_ | Letícia Assunção Aires Moreira

#### Grupo 3
**Usuário** | **Descrição**
--- | ---
_Scrum Master_ | Matheus Pimentel Leal
_Product Owner_ | Adne Moretti Moreira
Arquiteto de Software | Guilherme Barbosa Ferreira
DevOps | Gabriel Mariano da Silva
Desenvolvedor | Gabriel Moretti de Souza

#### Grupo 4
**Usuário** | **Descrição**
--- | ---
_Scrum Master_ | Mateus Vinícius Ferreira Franco
_Product Owner_ | Pedro Augusto Santos Siqueira
Desenvolvedor | Guilherme dos Santos Araújo <br  /> Thiago Oliveira Cunha <br  /> João Paulo da Silva Freitas <br  /> Arthur Taylor de Jesus Popov <br  /> Thiago Vivian Bastos

## 6. Requisitos de alto nível
**Nome** | **Descrição**
--- | --- 
Visualização dos dados | Os dados, por curso, que deverão ser visualizados são: Quantidade de disciplinas, Vagas ofertadas, Alunos matriculados e Salas disponíveis.
Monitoramento de vagas | A ocupação do departamento selecionado deverá ser exibida via gráfico. 
Filtros de exibição | Deverá ser possível filtrar as disciplinas de acordo com a modalidade (Presencial/Remoto/Semipresencial), e também de modo a exibir as que possuem vagas disponíveis.
Interatividade com o usuário | As mensagens do sistema para o usuário devem ser claras, e o usuário deve poder buscar pelos cursos e matérias que desejar.

## 7. Riscos
**Risco** | **Prevenção** | **Ação**
:---: | :---: | :---:
Algum membro contrair COVID-19 | Estar previamente organizado entre os membros do grupo, para que alguém consiga assumir a função do membro em questão. | Organização com a equipe.
Falta de comunicação | Estabelecer canais de comunicação fixos, além de encontros entre as semanas. | Pontuação clara de objetivos durante as sprints e torná-los de fácil acesso para a equipe.
Desistência de algum membro do projeto | Estimular a participação do membro no projeto. | Não sobrecarregar nenhum membro e auxiliar em suas devidas tarefas.
Dificuldade ao adaptar às tecnologias escolhidas | Compartilhamento de links ou aulas para estudo e aprofundamento da tecnologia. | Procurar sobre as tecnologias e incentivar o estudo. 
Mudanças no escopo do projeto | Realizar _reviews_ do projeto e validar se ocorre como o planejado. | Realizar reuniões claras que definam as pendências do projeto.

## 8. Requisitos para a aprovação
* Validação pela professora Dr. Carla Rocha Aguiar.
* Atender às expectativas prévias do projeto.

## 9. Estratégias de comunicação
Para comunicação interna foram utilizadas as seguintes ferramentas: **Discord** e **Telegram**.<br />
Para comunicação com os demais grupos utilizamos, além das ferramentas citadas anteriormente, o **GitHub**.<br />
Para aulas e treinamentos com a professora e monitores, também foi utilizada a ferramenta do **Jitsi Meet**.

## 10. Referências
UNIVERSIDADE DE BRASÍLIA (Brasil). **CheeryUP. Termo de abertura do projeto.** [S. l.], 2021. Disponível em: <https://fga-eps-mds.github.io/2020.2-CheeryUP/#/./wiki/TAP?id=5---riscos>. Acesso em: 28 jan. 2022. <br />
UNIVERSIDADE DE BRASÍLIA (Brasil). **Acácia. Termo de abertura do projeto.** [S. l.], 2019. Disponível em: <https://fga-eps-mds.github.io/2019.2-Acacia/#/project_charter>. Acesso em: 28 jan. 2022. <br />
UNIVERSIDADE DE BRASÍLIA (Brasil). **AlligaBot. Termo de abertura do projeto.** [S. l.], 2021. Disponível em: <https://fga-eps-mds.github.io/2021.1-AlligaBot/2021/08/02/termo-de-abertura-do-projeto/>. Acesso em: 28 jan. 2022. <br />
SCHWABER, Ken; SUTHERLAND, Jeff. **O Guia do Scrum**. [S. l.], 2020. Disponível em: <https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Portuguese-European.pdf>. Acesso em: 28 jan. 2022. <br />
MORETTI, Gabriel. **Issue #6 - Pesquisas - Documentação**. [S. l.], 2022. Disponível em: <https://github.com/fga-eps-mds/Projeto01/issues/6#issuecomment-1022324492>. Acesso em: 28 jan. 2022. <br />
