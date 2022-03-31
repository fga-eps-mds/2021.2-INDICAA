## Histórico de versões

|Data|Versão|Descrição|Autor|
|-|-|-|-|
|30/01/2022|0.1|Abertura Documento de Arquitetura|Guilherme|
|31/01/2022|0.2|Adicionado Tópico de Referências|Guilherme|
|01/02/2022|0.3|Listagem das restrições da arquitetura|Arthur|
|01/02/2022|0.4|Definição do Escopo do Projeto|Guilherme|
|01/02/2022|0.5|Definição de Metas da Arquitetura|Thiago O. e Pedro|
|07/02/2022|0.6|Adicionado Tópico de Visão Geral do projeto|João Paulo|
|15/02/2022|0.7|Adicionado Tópicos faltantes: Visão de Casos de Uso, Visão Lógica, Tamanho e Desempenho. Tópicos 3 e 4 alimentados com novas informações. Pequenos erros corrigidos.|João Paulo|
|02/03/2022|0.8|Adicionado o Diagrama de Pacotes | Guilherme Barbosa e Gabriel Mariano|
|03/03/2022|0.9|Adicionado o Diagrama de Casos de Uso | Guilherme Santos|
|05/03/2022|0.9.1| Revisão geral dos documentos do projeto | Adne Moretti e Matheus Pimentel Leal
|26/03/2022|0.9.2| Atualização do escopo e pequenas correções | Gabriel Moretti e Matheus Pimentel Leal


## 1. <a name="1">Introdução</a>

### 1.1 <a name ="1_1">Objetivo</a>

<p align="justify"> &emsp;&emsp; O objetivo deste documento é oferecer, de modo claro e geral, a visão arquitetural do projeto INDICAA, trazendo consigo as características necessárias para os controles de suas atividades arquiteturais, moldando, assim, todo procedimento para o desenvolvimento do sistema. Esse documento também se dispõe a elucidar quais foram as motivações que levaram a equipe a tomar decisões a respeito dessa arquitetura.  </p>

### 1.2 <a name="1_2">Escopo</a>

<p align="justify"> &emsp;&emsp;  No contexto da pandemia, a gestão de espaços se tornou fundamental para o bom funcionamento da UnB. Nesse contexto, a equipe de coordenação voltou seus esforços para propiciar uma boa divisão das disciplinas e atividades no geral de acordo com o espaço existente. Para tal, a visualização da divisão dos espaços de acordo com os períodos do dia é essencial para uma melhor tomada de decisões pelos gestores, o que impactará diretamente a execução das atividades acadêmicas da universidade.</p>
 
<p align="justify"> &emsp;&emsp; Nesse contexto, o objetivo desse projeto é propiciar uma melhor organização das informações 
disponibilizadas pelo nosso site acadêmico. Sendo assim, os coordenadores terão a possibilidade de visualizar a quantidade 
de disciplinas por curso, a quantidade de vagas ofertadas, a quantidade de alunos matriculados e a quantidade 
de salas disponíveis. Por meio dessas funcionalidades, a análise, o compartilhamento e o monitoramento
de informações será mais simples, ajudando tanto a parte 
de gerenciamento e controle da disponibilização de disciplinas por parte dos coordenadores como a própria matrícula em disciplina por parte dos discentes. </p>

### 1.3 <a name=1_3>Definições, acrônimos e abreviações</a>

Tabela com o significado de abreviações para termos usados ao longo do documento.

|Sigla |Significado |
--|--
|**UnB**| Universidade de Brasília
|**FGA**| Faculdade do Gama 
|**MDS**| Métodos de Desenvolvimento de Software
|**SIGAA**| Sistema Integrado de Gestão das Atividades Acadêmicas
|**FU**| Funcionalidade de Usuário
|**BI**| Business Intelligence

### 1.4 <a name=1_4>Visão Geral</a>

<p align="justify"> &emsp;&emsp; Este documento está dividido em 6 grandes tópicos, com subdivisões, com o objetivo final de detalhar as características arquiteturais do projeto, bem como seus requisitos e motivações. Os tópicos podem ser encontrados a seguir:</p>

| |Tópico |Descrição |
|-|-|-|
|**1**|**Introdução**| Fornece ao leitor uma visão geral do conteúdo abordado no documento
|**2**|**Representação Arquitetural**| Detalha a arquitetura utilizada no projeto e como ela está organizada
|**3**|**Metas e Restrições da Arquitetura**| Descreve os objetivos do projeto, bem como suas restrições, do ponto de vista arquitetural
|**4**|**Visão dos Casos de Uso**| Descreve as partes significativas do ponto de vista da arquitetura do modelo de casos de uso
|**5**|**Visão Lógica**| Descreve as partes significativas do ponto de vista da arquitetura do modelo de design
|**6**|**Desempenho e Qualidade**| Descreve as características de desempenho do Software, bem como as restrições estabelecidas e possíveis falhas
|**7**|**Referências**| Fornece ao leitor uma visão geral das referência utilizadas durante a criação deste documento


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
<p align="justify">&emsp;&emsp; Para cumprir tais metas, será necessário a utilização de um Webcrawler com o intuito de retirar as informações do SIGAA, salvá-las em um banco de dados e utilizar ferramentas de BI para a amostragem dos indicadores. </p>

### 3.2 <a name="3_2">Restrições</a>

<p align="justify">&emsp;&emsp; • Possuir conexão com a internet </p>
<p align="justify">&emsp;&emsp; • Dependência da plataforma SIGAA </p>
<p align="justify">&emsp;&emsp; • Eventual demora no tempo de resposta para atualização das informações no SIGAA </p>

## 4. <a name="4">Visão de Casos de Uso</a>

### 4.1 <a name="4_1">Diagrama de Casos de Uso</a>
![](https://raw.githubusercontent.com/fga-eps-mds/2021.2-INDICAA/main/docs/assets/Diagrama_casos_de_uso.png)

### 4.2 <a name="4_2">Descrição dos Casos de Uso</a>
#### FU01 - Pesquisa
|||
------|------
 **Descrição**| Esta funcionalidade permite o usuário pesquisar tanto por decanato a partir da seleção de um campus |
 **Atores**| Usuário |
 **Pré-condições**| O usuário deve ter selecionado um campus e preencher o campo de pesquisa  |
 **Pós-condições**| O usuário deve ter conseguido realizado a pesquisa por um decanato |
 **Fluxo principal**|1. O usuário abre a aplicação <br> 2. O usuário seleciona um campus <br> 3. O usuário preenche o campo de pesquisa e seleciona o que deve ser pesquisado de acordo com as sugestoes <br> 4. A pesquisa é realizada e o usuário tem acesso ao [FU07] e ao [FU03] o que leva a todos os outros FU's |
 **Fluxo Alternativo**| **FA01 - Não seleção do campus pelo usuário** <br> Caso o usuário nao selecione um campus a pesquisa nao poderá ser realzada|
 **Fluxo de exceção**| **FE01 - Conexão** <br> Se houver algum problema de conexão, a operação pode não ser concluída com sucesso|
 #### FU02 - Visualizar salas disponíveis
|||
------|------
 **Descrição**| Esta funcionalidade permite o usuário visualizar as salas disponíveis de forma mais detalhada pela lista |
 **Atores**| Usuário |
 **Pré-condições**| O usuário deve ter realizado a pesquisa e clicado para detalhar os gráficos |
 **Pós-condições**| O usuário deve ter conseguido visualizar as salas disponíveis de forma detalhada |
 **Fluxo principal**|1. O usuário realiza uma pesquisa[FU01] <br> 2. O usuário clica em detalhar <br> 3. O usuário visualiza uma lista com as informaçoes |
 **Fluxo de exceção**| **FE01 - Conexão** <br> Se houver algum problema de conexão, a operação pode não ser concluída com sucesso|
 #### FU03 - Filtrar Pesquisa
|||
------|------
 **Descrição**| Esta funcionalidade permite o usuário filtrar sua pesquisa a partir do [FU07] ou do [FU04] |
 **Atores**| Usuário |
 **Pré-condições**| O usuário deve ter realizado a pesquisa |
 **Pós-condições**| O usuário deve ter conseguido filtrar sua pesquisa tanto por modalidade quanto por disponibilidade |
 **Fluxo principal**|1. O usuário realiza uma pesquisa[FU01] <br> 2. O usuário visualiza as opçoes de filtragem á esquerda da pagina <br> |
 **Fluxo de exceção**| **FE01 - Conexão** <br> Se houver algum problema de conexão, a operação pode não ser concluída com sucesso|

#### FU07 - Visualizar gráficos
|||
----- | ----- 
**Descrição** | Este caso de uso se refere à funcionalidade que permite que o usuário visualize informações menos detalhadas sobre as vagas e salas ocupadas|
**Atores** | Usuário |
**Pré-condições** | O usuário deverá ter realizado a pesquisa [FU01] |
**Pós-condições** | O gráfico sobre as vagas e salas ocupadas deverá estar apresentado na tela para o usuário |
**Fluxo principal** | 1. O usuário realiza a pesquisa com os filtros desejados[FU01] <br> 2. O gráfico é apresentado na tela <br> 3. O filtro é apresentado a esquerda para o usuário[FU03]  
**Fluxo de exceção** | **FE01 - Conexão** <br>Se houver algum problema de conexão, a operação pode não ser concluída com sucesso


#### FU08 - Manual de Uso

|||
----- | ----- 
**Descrição** | Este caso de uso se refere à funcionalidade que apresenta ao usuário como realizar uma pesquisa |
**Atores** | Usuário |
**Pré-condições** | O usuário deverá passar o cursor sobre o icone de ajuda na margem superior direita |
**Pós-condições** | Será apresentado informações sobre como realizar uma pesquisa e quais as funcionalidades das ferramentas disponíveis |
**Fluxo principal** | 1. O usuário passar o cursor sobre o icone de ajuda  <br> 2. É Apresentado um popup com as infromações de uso 
**Fluxo de exceção** | **FE01 - Conexão** <br>Se houver algum problema de conexão, a operação pode não ser concluída com sucesso

## 5. <a name="5">Visão Lógica</a>

### 5.1 <a name="5_1">Visão Geral</a>

### 5.2 <a name="5_2">Diagrama de Pacotes</a>
![](https://user-images.githubusercontent.com/88190414/156471832-18df42d5-aa06-400b-8f3d-c9e683b89c16.png)

## 6. <a name="6">Desempenho e Qualidade</a>

## 7 <a name=1_4>Referências</a>
 MATHEUS, Davi; et al. Documento de Arquitetura - Cheery Up. Disponível em: <https://fga-eps-mds.github.io/2020.2-CheeryUP/#/./wiki/Documents/Documento_de_Arquitetura?id=documento-de-arquitetura>. Acesso em: 30 jan 2022.
 
 CARVALHO, Durval; et al. Documento de Arquitetura - Acácia. Disponível em: <https://fga-eps-mds.github.io/2019.2-Acacia/#/architecture_document?id=documento-de-arquitetura>. Acesso em: 30 jan 2022.
 
EDUARDO, Victor; et al. Documento de Arquitetura - AlligaBot. Disponível em: <https://fga-eps-mds.github.io/2021.1-AlligaBot/2021/08/03/documento-de-arquitetura/>. Acesso em: 07/02/2022.
