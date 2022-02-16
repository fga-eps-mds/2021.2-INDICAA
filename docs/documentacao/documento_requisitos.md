# Histórico de alterações
| **Data**   	| **Versão** 	| **Modificação**                                                  	| **Autor(es)**              	|
|------------	|------------	|------------------------------------------------------------------	|----------------------------	|
| 08/02/2022 	|     0.1    	| Criação do documento de requisitos                              	| Caio Oliveira             	|
| 12/02/2022 	|     0.2    	| Inclusão de requisitos funcionais e não funcionais                | Aberto a todos              |
| 13/02/2022 	|     0.3    	| Revisão e filtragem dos requisitos                                | Adne M., Laura P. e Pedro S.|

## 1. Introdução
Este documento conterá as descrições sucintas dos requisitos funcionais e não funcionais do sistema, sem especificação de prioridade.<br /> O documento está passível à futuras alterações, caso seja identificada a necessidade.

## 2. Especificação de requisitos
Requisitos de software são atribuições que o mesmo deve executar, de modo a se tornarem objetivos e métricas de sucesso para o projeto.<br /> Ou seja, um dos critérios para avaliar se o software foi bem sucedido é o quão fiel ele foi aos seus requisitos pré-definidos. Segue abaixo os Requisitos Funcionais e Não Funcionais: 

### 2.1. Funcionais
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

### 2.2. Não Funcionais
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

- [Versão 1](https://github.com/fga-eps-mds/Projeto01/issues/17#issuecomment-1032683760)
