## Histórico de versões

|Data|Versão|Descrição|Autor|
|-|-|-|-|
|27/01/2022|0.1|Abertura Documento de Visão|Caio|
|27/01/2022|0.2|Adição dos tópicos 1, 2 e 3|Caio|
|28/01/2022|0.3|Continuação do tópico 3|Lucas|
|28/01/2022|0.4|Adição tópico 4 -Visão geral de produto|Matheus|
|29/01/2022|0.5|Continuação do tópico 4|Letícia|
|30/01/2022|0.6|Adição do tópico 5|Vitor|
|31/01/2022|0.7|Adição do tópico 7|Caio|
|31/01/2022|0.8|Correção de erros|Letícia|
|17/02/2022|0.9|Adição do Tópico 6 sobre Requisitos|Caio|
|05/03/2022|0.9.1|Correção do Documento|Gabriel Mariano|
|05/03/2022|0.9.2|Correção do Documento|Letícia|

## 1. <a name="1">Introdução</a>

### 1.1 <a name ="1_1">Propósito</a>

<p align="justify"> &emsp;&emsp; O presente documento visa apresentar o produto,
 mostrando suas características, tanto funcionais como não funcionais.
 Além disso será mostrado como foi o desenvolvimento, relatos dos envolvidos e
 informações para melhor entendimento do projeto. </p>

### 1.2 <a name=1_3>Siglas e seus significados</a>

Tabela com o significado de abreviações para termos usados ao longo do documento.

|Sigla |Significado |
--|--
|**UnB**| Universidade de Brasília
|**FGA**| Faculdade do Gama 
|**MDS**| Métodos de Desenvolvimento de Software
|**SIGAA**| Sistema Integrado de Gestão das Atividades Acadêmicas
|**RF**| Requisitos Funcionais
|**RNF**| Requisitos Não Funcionais

### 1.3 <a name="1_2">Escopo</a>

<p align="justify"> &emsp;&emsp;  No contexto da pandemia, a gestão de espaços se tornou fundamental para o bom funcionamento da UnB. Nesse contexto, a equipe de coordenação voltou seus esforços para propiciar uma boa divisão das disciplinas e atividades no geral de acordo com o espaço existente. Para tal, a visualização da divisão dos espaços de acordo com os períodos do dia é essencial para uma melhor tomada de decisões pelos gestores, o que impactará diretamente a execução das atividades acadêmicas da universidade.</p>
 
<p align="justify"> &emsp;&emsp; Nesse contexto, o objetivo desse projeto é propiciar uma melhor organização das informações 
disponibilizadas pelo nosso site acadêmico. Sendo assim, os coordenadores terão a possibilidade de visualizar a quantidade 
de disciplinas por curso, a quantidade de vagas ofertadas, a quantidade de alunos matriculados e a quantidade 
de salas disponíveis. Por meio dessas funcionalidades, a análise, o compartilhamento e o monitoramento
de informações será mais simples, ajudando tanto a parte 
de gerenciamento e controle da disponibilização de disciplinas por parte dos coordenadores como a própria matrícula em disciplina por parte dos discentes. </p>
  
## 2. <a name="2">Posicionamento</a>

### 2.1 <a name="2_2">Descrição do problema</a>

| O problema é | que afeta | cujo impacto é | uma boa solução seria |
| ------------ | --------- | -------------- | ----------------------|
| Dificuldade na busca por informações simples pelo SIGAA. | Coordenação acadêmica, alunos e professores | A carência de informações necessárias para atividades acadêmicas | Organização das informações em uma aplicação de fácil entendimento. |

### 2.2 <a name="2_3">Descrição do posicionamento do produto</a>

<p align="justify">&emsp;&emsp; O produto final consistirá em uma aplicação, onde será possível visualizar 
 um painel com informações sobre os cursos ofertados. Funcionando como um filtro, com o uso de 
 palavras chaves para focar a busca por elementos específicos. Consequentemente, a gestão por parte da coordenação acadêmica, assim como as atividades regulares de docentes e discentes se tornará uma tarefa simples. </p>
 
 ### 2.3 <a name="2_1">Oportunidade de negócio</a>

<p align="justify">&emsp;&emsp; O produto possibilita que o usuário busque por matérias específicas com relação ao curso em questão, evitando a confusão com outras disciplinas aparecendo na tela ao mesmo tempo. Desta forma, com toda essa 
 disponibilidade de informação, é possível obter uma melhor gestão e organização tanto para a escolha de disciplinas 
 por parte do estudante, quanto para a análise de dados por parte da coordenação ou pelos próprios professores. </p>

 ## 3. <a name="3">Descrição dos usuários e envolvidos</a>
 
 ### 3.1 <a name="3.1">Descrição dos usuários</a>
 
|**Nome**|**Descrição**|
|:-|:-|
| Coordenadores| Comunidade administrativa da UnB que visa, através dos dados disponibilizados relativos à gestão de espaços da universidade, tomar decisões que otimizem a organização destes. |
| Professores da UnB | Professores analisando as matérias ofertadas, verificando disponibilidade de salas ou quantidade de alunos matriculados em suas matérias. |
| Estudantes da UnB | Estudantes buscando informações para organização de horário, visando a matrícula em disciplina ou verificando a quantidade de vagas. |
| Outros | Quaisquer indivíduos que optarem por acessar dados relativos aos cursos da UnB. |

### 3.2 <a name="3.2">Descrição dos envolvidos</a>
|**Nome**|**Descrição**|**Responsabilidade**|
|:-:|:-:|:-:|
|Grupo de desenvolvimento| Estudantes de MDS |Projetar, desenvolver, testar, manter e gerir o software proposto e todos os documentos relacionados.|
|Grupo de avaliação| Professora e monitores de MDS |Ajudar o grupo de desenvolvimento com conselhos e feedback sobre o projeto.|

### 3.3 <a name="3.3">Principais necessidades dos usuários</a>
|**Usuário**|**Necessidade**|**Solução Atual**|**Solução Proposta**|
|:-:|:-:|:-:|:-:|
| Coordenadores da UnB | Analisar e otimizar a gestão de espaços da universidade de acordo com os dados disponibilizados pelo SIGAA | Procurar e analisar, manualmente (ou de maneira não automatizada), os dados disponibilizados no SIGAA | Tratar e dispor os dados necessários de maneira automatizada, prática e visual |
| Professores da UnB | Analisar informações relativas a disciplinas ofertadas no SIGAA  | Caso precise, pedir ajuda para técnicos disponíveis  | Tornar o processo de adquirir a informação necessária mais fácil |
| Estudantes da UnB | Compreender informações necessárias, porém não encontradas com facilidade, no SIGAA | Tentar entender como encontrar essas informações baseado na ajuda de colegas  | Tornar o próprio processo de adquirir a informação mais fácil, tornando o SIGAA um pouco mais user-friendly  |

### 3.4 <a name="3.4">Perfis dos envolvidos</a>
#### 3.4.1 <a name="3.4.1">Grupo de desenvolvimento</a>

Grupo 1:

| Papel  |  Descrição  |
| ----- | -------------------- |
| Scrum Master | Laura Pinos de Oliveira  |
| Product Owner | Caio César Oliveira |
| Arquiteto de Software | Lucas Henrique Lima de Queiroz |
| DevOps |  Vitor Eduardo Kühl Rodrigues |
| Desenvolvedor | Matheus Costa Gomes |
| Designer | Letícia Assunção Aires Moreira |

Grupo 3:

| Papel  |  Descrição  |
| ----- | -------------------- |
| Scrum Master | Matheus Pimentel Leal |
| Product Owner | Adne Moretti Moreira |
| Arquiteto de Software | Guilherme Barbosa Ferreira|
| DevOps | Gabriel Mariano da Silva |
| Desenvolvedor | Gabriel Moretti de Souza |

Grupo 4:

| Papel  |  Descrição  |
| ----- | -------------------- |
| Scrum Master | Mateus Vinícius Ferreira Franco |
| Product Owner | Pedro Augusto Santos Siqueira |
| Desenvolvedor | Guilherme dos Santos Araujo <br /> Thiago Oliveira Cunha <br /> João Paulo da Silva Freitas <br /> Arthur Taylor de Jesus Popov <br /> Thiago Vivan Bastos <br /> |

#### 3.4.2 <a name="3.4.2">Grupo de avaliação</a>
|**Representantes**|**Tipo**|**Responsabilidade**|**Critério de Sucesso**|**Envolvimento**|
|:---:|:-:|:-:|:-:|:-:|
| Carla Rocha | Professora de MDS | Auxiliar o grupo de desenvolvimento com feedback e conselhos | Entrega do projeto dentro do prazo limite |Baixo

### 3.5 <a name="3.5">Perfis dos Usuários</a>

#### 3.5.1 <a name="3.5.2">Coordenadores da UnB</a>
|**Representantes**|**tipo**|**Responsabilidade**|**Critério de sucesso**|**Envolvimento**|
|:-:|:-:|:-:|:-:|:-:|
| Responsáveis pela gestão de espaços da UnB interessados em otimizar esse processo | Coordenadores e Gestores da UnB | Desfrutar do produto e disponibilizar o feedback | Encontrar informações (outrora complicadas de se achar) com facilidade | Alto

#### 3.5.2 <a name="3.5.2">Professores da UnB</a>
|**Representantes**|**tipo**|**Responsabilidade**|**Critério de sucesso**|**Envolvimento**|
|:-:|:-:|:-:|:-:|:-:|
| Responsáveis por disciplinas acadêmicas interessados em conseguir administrá-las com mais facilidade | Professores da UnB | Desfrutar do produto, disponibilizando, também, feedback| Encontrar informações (outrora complicadas de se achar) com facilidade | Baixo

#### 3.5.3 <a name="3.5.1">Estudantes da UnB</a>
|**Representantes**|**tipo**|**Responsabilidade**|**Critério de sucesso**|**Envolvimento**|
|:-:|:-:|:-:|:-:|:-:|
| Interessados em adquirir informações necessárias, encontradas apenas no SIGAA, para cumprir demandas acadêmicas | Alunos da UnB | Desfrutar do produto, disponibilizando, também, feedback | Encontrar informações (outrora complicadas de se achar) com facilidade | Baixo

#### 3.5.4 <a name="3.5.3">Outros</a>
|**Representantes**|**tipo**|**Responsabilidade**|**Critério de sucesso**|**Envolvimento**|
|:-:|:-:|:-:|:-:|:-:|
| Quaisquer pessoas que quiserem acessar os dados disponibilizados pelo SIGAA com facilidade | Quaisquer pessoas | Desfrutar do produto | Encontrar informações com facilidade | Baixo/Nenhum




## 4. <a name="4">Visão Geral do Produto</a>

### 4.1.  <a name="4.1">Perspectivas</a>

<p align="justify">&emsp;&emsp;O projeto tem como fito elaborar um painel com os indicadores da lista de ofertas do SIGAA, de forma a possibilitar, ao usuário, visualização facilitada referente à quantidade de: disciplinas ofertadas; contingente de vagas; alunos matriculados, bem como salas disponíveis por curso. Desse modo, viabilizando o acesso fácil e rápido à informações tanto para o corpo docente como discente e, assim, contribuindo para uma maior qualidade do site SIGAA e suas implicações.  

### 4.2.  <a name="4.2">Resumo das Capacidades</a>

<p align="justify">&emsp;&emsp;A aplicação proporcionará uma interface adaptada à experiência de usuário dos gestores, alunos e professores, por meio da utilização de filtros de busca com palavras-chave, dentre outros aspectos os quais influenciarão positivamente na tomada de decisão relativa matrícula em disciplinas, análise de dados e gestão de processos.  
 
## 5. <a name="5">Recursos do Produto</a>

### 5.1.  <a name="5.2">Recursos dos coordenadores</a>

<p align="justify">&emsp;&emsp; O coordenador poderá ter acesso aos seguintes recursos:
 
 - Verificar a ocupação dos campus e de suas respectivas disciplinas disponibilizadas.
 - Verificar ocupação de salas pelas disciplinas disponibilizadas.
 - Verificar a disposição das disciplinas ao longo dos dias.
 
### 5.2.  <a name="5.2">Recursos dos docentes</a>

<p align="justify">&emsp;&emsp; O docente poderá ter acesso aos seguintes recursos:
 
 - Verificar disponibilidade de salas.
 - Verificar a quantidade de alunos matriculados em suas matérias.

### 5.3.  <a name="5.1">Recursos dos discentes</a>

<p align="justify">&emsp;&emsp; O discente poderá ter acesso aos seguintes recursos:
 
 - Verificar disciplinas ofertadas.
 - Visualizar os horários das disciplinas de forma fácil.
 - Visualizar salas disponíveis por curso.
 
### 5.3.  <a name="5.3">Filtro</a>

<p align="justify">&emsp;&emsp; A aplicação contará com um sistema de filtragem que dará ao usuário a informação buscada de forma interativa e de forma fácil.
 
 ## 6. Especificação de requisitos
<p align="justify">&emsp;&emsp; Requisitos de software são atribuições que o mesmo deve executar, funcionam como características de um sistema, de modo a se tornarem objetivos e métricas de sucesso para o projeto.
<p align="justify">&emsp;&emsp; Ou seja, um dos critérios para avaliar se o software foi bem sucedido é o quão fiel ele foi aos seus requisitos pré-definidos. Segue abaixo os Requisitos Funcionais e Não Funcionais: 

### 6.1. Funcionais
| **Número**| **Especificação**                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------------|
| RF1 	   	| O sistema deve buscar os cursos e apresentar as matérias                                                      |
|	RF2      	| O sistema deve visualizar a quantidade de disciplinas ofertadas por curso                                     |
| RF3      	| O sistema deve visualizar a quantidade de vagas ofertadas por curso                                           |
| RF4     	| O sistema deve visualizar a quantidade de alunos matriculados por curso                                       |
| RF5     	| O sistema deve visualizar a quantidade de salas disponíveis por curso                                         |
| RF6      	| O sistema deve verificar se a entrada de pesquisa existe, caso não exista, deve exibir uma mensagem de erro   |
| RF7      	| Deve ser possível selecionar qual campus que se deseja visualizar as informações                              |
| RF8      	| O sistema deve mostrar as informações por meio de painéis                                                     |
| RF9      	| O sistema deve sugerir os cursos que possuem as mesmas iniciais do curso preterido no campo de busca          |
| RF10     	| O sistema deve ser claro ao fornecer feedbacks e mensagens de erro ou aviso aos usuários                      |
| RF11    	| O sistema deve ser capaz de filtrar as disciplinas de modo a exibir as que possuem vagas disponíveis          |
| RF12    	| O sistema deve exibir, via gráfico, a porcentagem de ocupação do departamento selecionado                     |
| RF13     	| O sistema deve filtrar as disciplinas ofertadas de acordo com a modalidade (Presencial/Remoto/Semipresencial) |
| RF14    	| O sistema deve permitir que o usuário altere a forma de exibição do horário                                   |

### 6.2. Não Funcionais
| **Número**| **Especificação**                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------------|
| RNF1 	   	| O sistema deve atualizar as informações em tempo real conforme o SIGAA                                        |
|	RNF2    	| A parte de Back-End do sistema deve ser desenvolvido em Python/Django REST/Selenium                           |
| RNF3     	| A parte de Front-End do sistema deve ser desenvolvido em React                                                |
| RNF4     	| O sistema deve ser desenvolvido em orientação a objetos                                                       |
| RNF5     	| O sistema deverá ser resistente a falhas de software                                                          |
| RNF6     	| O sistema deverá ter baixo acoplamento e alta coesão                                                          |
| RNF7     	| O sistema deve ser multiplataforma: Windows, distribuições Linux e MAC                                        |
| RNF8     	| O sistema deve ser responsivo                                                                                 |
| RNF9     	| O sistema deve armazenar dados em um banco de dados                                                           |
 
## 7. <a name="5">Referências</a>
 
 RAFAEL E VITOR; et al. Documento de Visão - Anunbis. Disponível em: <https://fga-eps-mds.github.io/2020.2-Anunbis/documentacao/documento-de-visao/>. Acesso em: 31 jan 2022.
 
 NOBRE, Amanda; et al. Documento de Visão - AlligaBot. Disponível em: <https://fga-eps-mds.github.io/2021.1-AlligaBot/2021/08/04/documento-de-vis%C3%A3o/>. Acesso em: 31 jan 2022.
 

