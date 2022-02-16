## Histórico de versões

|Data|Versão|Descrição|Autor|
|-|-|-|-|
|30/01/2022|0.1|Abertura Documento de Visão|Guilherme|
|31/01/2022|0.2|Adicionado Tópico de Referências|Guilherme|
|01/02/2022|0.3|Listagem das restrições da arquitetura|Arthur|
|01/02/2022|0.4|Definição do Escopo do Projeto|Guilherme|
|01/02/2022|0.5|Definição de Metas da Arquitetura|Thiago O. e Pedro|
|07/02/2022|0.6|Adicionado Tópico de Visão Geral do projeto|João Paulo|
|15/02/2022|0.7|Adicionado Tópicos faltantes: Visão de Casos de Uso, Visão Lógica, Tamanho e Desempenho. Tópicos 3 e 4 alimentados com novas informações. Pequenos erros corrigidos.|João Paulo|

## 1. <a name="1">Introdução</a>

### 1.1 <a name ="1_1">Objetivo</a>

<p align="justify"> &emsp;&emsp; O objetivo deste documento é oferecer, de modo claro e geral, a visão aquitetural do projeto INDICAA, trazendo consigo as características necessárias para os controles de suas atividades arquiteturais, moldando, assim, todo procedimento para o desenvolvimento do sistema. Esse documento também se dispõe a elucidar quais foram as motivações que levaram a equipe a tomar decisões a respeito dessa arquitetura.  </p>

### 1.2 <a name="1_2">Escopo</a>

<p align="justify"> &emsp;&emsp; Esse documento aplica-se ao projeto INDICAA, um sistema que agrupa diversas informações importantes para organização dos alunos e professoraes da UNB. Os alunos terão a possibilidade de visualizar a quantidade de disciplinas por curso, a quantidade de vagas ofertadas, a quantidade de alunos matriculados e a quantidade de salas disponíveis. E, por meio dessas funcionalidades, a análise, o compartilhamento e o monitoramento de informações será mais simples, ajudando tanto a parte estudantil da UnB, quanto a parte de gestão e controle de processos como a própria matrícula em disciplina. Esse projeto será desenvolvido pelos alunos da disciplina de Métodos de Desenvolvimento de Software da Universidade de Brasília - Campus Gama</p>

### 1.3 <a name=1_3>Definições, acrônimos e abreviações</a>

Tabela com o significado de abreviações para termos usados ao longo do documento.

|Sigla |Significado |
--|--
|**UnB**| Universidade de Brasília
|**FGA**| Faculdade do Gama 
|**MDS**| Métodos de Desenvolvimento de Software
|**SIGAA**| Sistema Integrado de Gestão das Atividades Acadêmicas

### 1.4 <a name=1_4>Referências</a>
 MATHEUS, Davi; et al. Documento de Arquitetura - Cheery Up. Disponível em: <https://fga-eps-mds.github.io/2020.2-CheeryUP/#/./wiki/Documents/Documento_de_Arquitetura?id=documento-de-arquitetura>. Acesso em: 30 jan 2022.
 
 CARVALHO, Durval; et al. Documento de Arquitetura - Acácia. Disponível em: <https://fga-eps-mds.github.io/2019.2-Acacia/#/architecture_document?id=documento-de-arquitetura>. Acesso em: 30 jan 2022.
 
EDUARDO, Victor; et al. Documento de Arquitetura - AlligaBot. Disponível em: <https://fga-eps-mds.github.io/2021.1-AlligaBot/2021/08/03/documento-de-arquitetura/>. Acesso em: 07/02/2022.

### 1.5 <a name=1_4>Visão Geral</a>

<p align="justify"> &emsp;&emsp; Este documento está dividído em 6 grandes tópicos, com subdivisões, com o objetivo final de detalhar as características arquiteturais do projeto, bem como seus requisitos e motivações:</p>

| |Tópico |Descrição |
|-|-|-|
|**1**|**Introdução**| Fornece ao leitor uma visão geral do conteúdo abordado no documento
|**2**|**Representação Arquitetural**| Detalha a arquitetura utilizada no projeto e como ela está organizada
|**3**|**Metas e Restrições da Arquitetura**| Descreve os objetivos do projeto, bem como suas restrições, do ponto de vista arquitetural
|**4**|**Visão dos Casos de Uso**| Descreve as partes significativas do ponto de vista da arquitetura do modelo de casos de uso
|**5**|**Visão Lógica**| Descreve as partes significativas do ponto de vista da arquitetura do modelo de design
|**6**|**Tamanho e Desempenho**| Descreve as características de desempenho do Software, bem como as restrições estabelecidas e possíveis falhas


## 2. <a name="2">Representação da Arquitetura</a>
<p align="justify">&emsp;&emsp; (descrição rápida do funcionamento do Software INDICAA com uma imagem exemplo) </p>

### 2.1 <a name="2_1">Tecnologias</a>

<p align="justify">&emsp;&emsp; (lista com as ferramentas utilizadas para desenvolvimento do software se possível com uma imagem/logo para ilustrar) </p>
 
 
## 3. <a name="3">Metas e Restrições da Arquitetura</a>
 
 ### 3.1 <a name="3_1">Metas</a>
 
<p align="justify">&emsp;&emsp; Este projeto tem como meta fazer um painel com o intuito de mostrar os respectivos indicadores da lista de oferta do SIGAA listados a seguir:  </p>
<p align="justify">&emsp;&emsp; •	Quantidade de disciplinas ofertadas por curso </p>
<p align="justify">&emsp;&emsp; •	Quantidade de vagas ofertadas por curso </p>
<p align="justify">&emsp;&emsp; •	Quantidade de alunos matriculados por curso </p>
<p align="justify">&emsp;&emsp; •	Quantidade de salas disponíveis por curso </p>
<p align="justify">&emsp;&emsp; Para cumprir tais metas, será necessário a utilização de um Webcrawler com o intuito de retirar as informações do SIGAA, salvá-las em um banco de dados e utilizar ferramentas de BI (Business Intelligence) para a amostragem dos indicadores. </p>

### 3.2 <a name="3_2">Restrições</a>

<p align="justify">&emsp;&emsp; • Possuir conexão com a internet </p>
<p align="justify">&emsp;&emsp; • Dependência da plataforma SIGAA </p>
<p align="justify">&emsp;&emsp; • Eventual demora no tempo de resposta para atualização das informações no SIGAA </p>

## 4. <a name="4">Visão de Casos de Uso</a>

<p align="justify">&emsp;&emsp; •	Interagir com o menu dos campi </p>
<p align="justify">&emsp;&emsp; •	Pesquisar disciplinas ofertadas </p>
<p align="justify">&emsp;&emsp; •	Pesquisar vagas ofertadas </p>
<p align="justify">&emsp;&emsp; •	Pesquisar alunos matriculados </p>
<p align="justify">&emsp;&emsp; •	Pesquisar salas disponíveis </p>
<p align="justify">&emsp;&emsp; •	Visualizar os gráficos informativos das disciplinas </p>

### 4.1 <a name="4_1">Atores</a>

### 4.2 <a name="4_2">Diagrama de Casos de Uso</a>

### 4.3 <a name="4_3">Prioridade dos Casos de Uso</a>

<p align="justify">&emsp;&emsp; Esse diagrama expõe os seguintes requisitos: </p>
<p align="justify">&emsp;&emsp; •RF1: O sistema deve buscar os cursos e apresentar as matérias </p>
<p align="justify">&emsp;&emsp; •RF2: O sistema deve visualizar a quantidade de disciplinas ofertadas por curso </p>
<p align="justify">&emsp;&emsp; •RF3: O sistema deve visualizar a quantidade de vagas ofertadas por curso </p>
<p align="justify">&emsp;&emsp; •RF4: O sistema deve visualizar a quantidade de alunos matriculados por curso </p>
<p align="justify">&emsp;&emsp; •RF5: O sistema deve visualizar a quantidade de salas disponíveis por curso </p>
<p align="justify">&emsp;&emsp; •RF6: O sistema deve verificar se a entrada de pesquisa existe, caso não exista, deve apresentar uma mensagem de erro. </p>
<p align="justify">&emsp;&emsp; •RF7: Deve ser possível selecionar qual campus que se deseja visualizar as informações </p>
<p align="justify">&emsp;&emsp; •RF8: O sistema deve mostrar as informações por meio de painéis </p>
<p align="justify">&emsp;&emsp; •RF9: No campo de busca, ao inserir as primeiras letras do curso que se deseja visualizar, os cursos que possuírem as mesmas inicias devem aparecer como sugestão </p>
<p align="justify">&emsp;&emsp; •RF10: O sistema deve ser claro ao fornecer feedbacks e mensagens de erro ou aviso aos usuários. </p>
<p align="justify">&emsp;&emsp; •RF11: O sistema deve ser capaz de filtrar as disciplinas de modo a exibir as que possuem vagas disponíveis </p>
<p align="justify">&emsp;&emsp; •RF12: O sistema deve exibir, via gráfico, a porcentagem de ocupação do departamento selecionado </p>
<p align="justify">&emsp;&emsp; •RF13: O sistema deve filtrar as disciplinas ofertadas de acordo com a “modalidade” (Presencial, Remoto ou Semipresencial) </p>
<p align="justify">&emsp;&emsp; •RF14: O sistema deve permitir que o usuário altere a forma de exibição do horário (padronizado ou simplificado) </p>
<p align="justify">&emsp;&emsp; •RNF1: O sistema deve atualizar as informações em tempo real conforme o SIGAA </p>
<p align="justify">&emsp;&emsp; •RNF2: A parte de Back-End  do sistema deve ser desenvolvido em Python/Django REST/Selenium  </p>
<p align="justify">&emsp;&emsp; •RNF3: A parte de Front-End do sistema deve ser desenvolvido em React  </p>
<p align="justify">&emsp;&emsp; •RNF4: O sistema deve ser desenvolvido em orientação a objetos </p>
<p align="justify">&emsp;&emsp; •RNF5: O sistema deverá ser resistente a falhas de software </p>
<p align="justify">&emsp;&emsp; •RNF6: O sistema deverá ter baixo acoplamento e alta coesão </p>
<p align="justify">&emsp;&emsp; •RNF7: O sistema deve ser multiplataforma: Windows, distribuições Linux e MAC. </p>
<p align="justify">&emsp;&emsp; •RNF8: O sistema deve ser responsivo. </p>
<p align="justify">&emsp;&emsp; •RNF9: O sistema deve armazenar dados em um banco de dados. </p>

## 5. <a name="5">Visão Lógica</a>

### 5.1 <a name="5_1">Visão Geral</a>

### 5.2 <a name="5_2">Diagrama de Pacotes</a>

## 6. <a name="6">Tamanho e Desempenho</a>
