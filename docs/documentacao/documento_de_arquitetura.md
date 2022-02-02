## Histórico de versões

|Data|Versão|Descrição|Autor|
|-|-|-|-|
|30/01/2022|0.1|Abertura Documento de Visão|Guilherme|
|31/01/2022|0.2|Adicionado Tópico de Referências|Guilherme|
|01/02/2022|0.3|Listagem das restrições da arquitetura|Arthur|
|01/02/2022|0.4|Definição do Escopo do Projeto|Guilherme|
|01/02/2022|0.5|Definição de Metas da Arquitetura|Thiago O. e Pedro|

## 1. <a name="1">Introdução</a>

### 1.1 <a name ="1_1">Objetivo</a>

<p align="justify"> &emsp;&emsp; O objetivo deste documento é oferecer, de modo claro e geral, a visão aquitetural do projeto INDICAA, trazendo consigo as características necessárias para os controles de suas atividades arquiteturais, moldando, assim, todo procedimento para o desenvolvimento do sistema. Esse documento também se dispõe a elucidar quais foram as motivações que levaram a equipe a tomar decisões a respeito dessa arquitetura.  </p>

### 1.2 <a name="1_2">Escopo</a>

<p align="justify"> &emsp;&emsp; Esse documento aplica-se ao projeto INDICAA, um sistema que agrupa diversas informações importantes para organização dos alunos e professoraes da UNB. Os alunos terão a possibilidade de visualizar a quantidade de disciplinas por curso, a quantidade de vagas ofertadas, a quantidade de alunos matriculados e a quantidade de salas disponíveis. E, por meio dessas funcionalidades, a análise, o compartilhamento e o monitoramento de informações será mais simples, ajudando tanto a parte estudantil da UnB, quanto a parte de gestão e controle de processos como a própria matrícula em disciplina. Esse projeto será desenvolvido pelos alunos da disciplina de Métodos de Desenvolvimento de Software da Universidade de Brasília - Campus Gama</p>

### 1.3 <a name=1_3>Siglas e seus significados</a>

Tabela com o significado de abreviações para termos usados ao longo do documento.

|Sigla |Significado |
--|--
|**UnB**| Universidade de Brasília
|**FGA**| Faculdade do Gama 
|**MDS**| Métodos de Desenvolvimento de Software
|**SIGAA**| Sistema Integrado de Gestão das Atividades Acadêmicas

  
## 2. <a name="2">Represetanção de Arquitetura</a>

### 2.1 <a name="2_1">Padrão Arquitetural</a>

<p align="justify">&emsp;&emsp; (documentação da arquitetura do software) </p>

### 2.2 <a name="2_2">Tecnologias</a>

<p align="justify">&emsp;&emsp; (tabela com as ferramentas utilizadas para desenvolvimento do software) </p>
 
 ### 2.3 <a name="2_3">Diagrama de Pacotes</a>

<p align="justify">&emsp;&emsp; (descreve os pacotes ou pedaços do sistema divididos em agrupamentos lógicos mostrando as dependências entre eles) </p>
 
 ## 3. <a name="3">Metas e Restrições da Arquitetura</a>
 
 ### 3.1 <a name="3.1">Metas</a>
 
<p align="justify">&emsp;&emsp; Este projeto tem como meta fazer um painel com o intuito de mostrar os respectivos indicadores da lista de oferta do SIGAA listados a seguir:  </p>
<p align="justify">&emsp;&emsp; •	Quantidade de disciplinas ofertadas por curso </p>
<p align="justify">&emsp;&emsp; •	Quantidade de vagas ofertadas por curso </p>
<p align="justify">&emsp;&emsp; •	Quantidade de alunos matriculados por curso </p>
<p align="justify">&emsp;&emsp; •	Quantidade de salas disponíveis por curso </p>
<p align="justify">&emsp;&emsp; Para cumprir tais metas, será necessário a utilização de um Webcrawler com o intuito de retirar as informações do SIGAA, salvá-las em um banco de dados e utilizar ferramentas de BI (Business Intelligence) para a amostragem dos indicadores. </p>



### 3.2 <a name="3.2">Restrições da Arquitetura</a>

<p align="justify">&emsp;&emsp; • Nescessidade de acesso à internet </p>
<p align="justify">&emsp;&emsp; • Instabilidade da plataforma (SIGAA) </p>
<p align="justify">&emsp;&emsp; • Demora para atualização das informações no SIGAA </p>
<p align="justify">&emsp;&emsp; • Extensão pode ser incompatível com alguns navegadores </p>

## 4. <a name="4">Visão de Casos de Uso</a>
(o que é possível fazer com o software?)

(fazer topicalizado)


## 5. <a name="4">Referências</a>
 
 MATHEUS, Davi; et al. Documento de Arquitetura - Cheery Up. Disponível em: <https://fga-eps-mds.github.io/2020.2-CheeryUP/#/./wiki/Documents/Documento_de_Arquitetura?id=documento-de-arquitetura>. Acesso em: 30 jan 2022.
 
 CARVALHO, Durval; et al. Documento de Arquitetura - Acácia. Disponível em: <https://fga-eps-mds.github.io/2019.2-Acacia/#/architecture_document?id=documento-de-arquitetura>. Acesso em: 30 jan 2022.
 
