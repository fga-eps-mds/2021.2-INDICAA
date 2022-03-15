# Plano de Gerenciamento de Riscos

## Histórico de versões
| **Data** | **Versão** | **Descrição** | **Autor** |
| --- | --- | --- | --- |
| 03/03/2022 | 1.0 | Criação da primeira versão do documento | Adne Moretti, Gabriel Moretti, Pedro Siqueira e Vitor Eduardo|

## 1. Introdução
O documento em questão visa informar detalhadamente os riscos que podem afetar o projeto e aplicativo do INDICAA, assim categorizando e descrevendo os mesmos entre as respectivas responsabilidades e papéis e criando a estrutura analítica dos riscos.
## 2. Objetivo
O Plano de Gerenciamento de Riscos tem como objetivo principal a documentação e avaliação dos possíveis riscos a serem encontrados no desenvolvimento do projeto, procurando assim guiar os usuários e desenvolvedores às ações diretas para contribuir na mitigação e contenção dos efeitos negativos dos mesmos.
## 3. Estrutura Analítica dos Riscos
Uma forma comum para estruturar categorias dos riscos, representadas hierarquicamente, usa a estrutura analítica dos riscos (EAR). Uma EAR possibilita a melhor vizualização de todos as fontes de riscos, sendo útil para identificação e categorização.

![](/docs/assets/Diagrama-EAR.png)
Diagrama de riscos do projeto

### 3.1. Risco Técnico
| **Tipo** | **Descrição** |
| --- | --- |
| Requisitos | Riscos gerados pela falta de mapeamento e elicitação de requisitos |
| Tecnologias | Riscos gerados pela tecnologia usada |
| Complexidade | Riscos gerados pela falta de conhecimento e pela forma na qual a equipe de desenvolvimento se adapta a tecnologia escolhida |
| Qualidade | Riscos decorrentes da qualidade do produto final |
### 3.2. Risco de Gerenciamento
| **Tipo** | **Descrição** |
| --- | --- |
| Estimativa | Riscos que podem afetar o tempo de produção do projeto|
| Controle | Riscos relacionados ao controle de atividades |
| Planejamento | Riscos relacionados ao planejamento de confecção do projeto |
| Comunicação | Riscos relacionados às atividades e meio de comunicação, como ruídos ou falta de comunicação da equipe |
### 3.3. Risco Organizacional
| **Tipo** | **Descrição** |
| --- | --- |
| Recursos | Riscos gerados pela falta de recursos humanos e/ou tecnológicos, como perda ou defeitos em equipamentos ou membros que abandonam o projeto |
| Priorização | Riscos gerados pela má escolha de histórias de usuários na Sprint |
| Dependências | Riscos que podem afetar a evolução do projeto |
### 3.4. Risco Externo
| **Tipo** | **Descrição** |
| --- | --- |
| Cliente | Riscos gerados pelo cliente em relação ao produto, como mudanças no escopo devido a um pedido do cliente |
| Pandemia | Riscos gerados pela pandemia |
## 4. Identificação dos Riscos
| **ID** | **Risco** | **Causa** | **O impacto será** | **Categoria EAR** |
| --- | --- | --- | --- | --- |
| RN01 | O projeto não atender aos requisitos levantados | Falha no levantamento de requisitos e validação constante com o projeto | e possível refatoração do projeto e redefinição dos requisitos| Requisitos
| RN02 | Membros dos times trancarem a matéria ou abandonarem projeto | Desmotivação, problemas pessoais | Sobrecarga em outros membros do projeto e redefinição de papéis | Recursos/Pandemia
| RN03 | Dificuldade de adaptação da equipe com as tecnologias | Falta de conhecimento e incompatibilidade com o projeto | Atraso na entrega e redefinição de tecnologia | Complexidade
| RN04 | Houver problemas de comunicação entre os grupos | Não utilização dos meios de comunicação definidos pela equipe | Desorganização, falta de alinhamento da equipe e dificuldade de gerenciamento pelos Scrum Masters | Comunicação
| RN05 | As tarefas não forem finalizadas no prazo | Planejamento incoerente da sprint ou falta de empenho de membros do grupo | Atraso no roadmap do projeto | Planejamento
| RN06 | As tecnologias e ferramentas utilizadas apresentarem inconstâncias | Do proprietário | Necessidade de troca de tecnologia por uma semelhante, atraso na entrega do produto | Tecnologias |
| RN07 | Divergência de horários disponíveis entre os membros | Rotina dos membros | Dificuldade de marcar reuniões e treinamentos entre os membros  | Comunicação
| RN08 | Problemas de equipamento e configuração do ambiente dos membros da equipe | Falha na internet, energia ou problemas nas máquinas | Atraso na entrega de tarefas por parte dos membros do grupo | Recursos
| RN09 | Documentação incoerente com o projeto | Documentação não for atualizada no decorrer do projeto | Confusão no entendimento do projeto por partes não envolvidas| Controle
| RN10 | Baixa qualidade do software entregue | Falta de conhecimento em design, usabilidade e tecnologias | Insatisfação por parte do cliente | Qualidade
| RN11 | Os arquitetos não conseguirem planejar e garantir a execução da arquitetura | Da falta de conhecimento e experiência com as tecnologias do projeto | Dificuldade na organização do projeto | Complexidade |
| RN12 | Alteração no escopo do projeto | Da falha no planejamento ou confusão em relação ao escopo | Replanejamento, necessidade de refazer partes do projeto | Planejamento |
| RN13 | Não houver evolução de conhecimento de membros da equipe | Falha nos treinamentos e membros não comprometidos com o projeto | Membros desnivelados e dificuldade no desenvolvimento do projeto | Dependências
| RN14 | Houver desentendimento entre membros que atrapalhe o desenvolver do projeto | Opniões e ideias divergentes | Dificuldade de comunicação e de desenvolvimento do projeto | Comunicação
| RN15 | Histórias de usuário mal descritas e definidas | Descrição confusa e de difícil entendimento | Implementação errada e trabalho refeito | Planejamento
| RN16 | Requisitos levantados não atendem às necessidades do cliente | Falta de comunicação e validação dos requisitos com o cliente | Insatisfação e requisitos levantados novamente | Cliente/Requisitos 
| RN17 | Estimativas incoerentes com as issues | Pouca noção de quanto esforço a issue demanda | Issue não finalizar no tempo previsto | Complexidade

## 5. Interpretação
| **ID** | **Impacto** | **Probabilidade** | **Avaliação** | **Contigência** | **Mitigação** |
| --- | --- | --- | --- | --- | --- |
| RN01 | Crítico | Muito Alta | 25 | Revalidar todos os requisitos com o Product Owner e com o cliente, e aplicar validação constante nos requisitos levantados | Realização de reuniões constantes com os membros da equipe, juntamente do cliente, para obter melhor compreensão do escopo do projeto 
| RN02 | Grande | Muito Alta | 20 | Maior qauntidade de tarefas e realocação de atividades para os membros permanecentes | Reunião para reafirmar a importância do projeto e realizar a realocação de atividades
| RN03 | Crítico | Alta | 20 | Indicar treinamentos para a equipe de desenvolvimento sobre a tecnologia escolhida | Estabelecer treinamentos constantes sobre a tecnologia escolhida 
| RN04 | Crítico | Muito Alta | 25 | Reafirmar a necessidade de um alto grau de comunicação e promover as mudanças necessárias, desde realização de daily meetings mais objetivas a mudanças de ferramentas para comunicação | Criando o Plano de comunicação em que a equipe demonstre comum acordo
| RN05 | Crítico | Alta | 20 | Realizar a entrega na próxima Sprint como dívida técnica e, talvez, realocá-la para uma dupla com mais facilidade com a tecnologia | Planejar as atividades e dividi-las nas sprints com base nos pesos e dificuldade definida no planning poker 
| RN06 | Crítico | Baixa | 10 | Trocar para uma tecnologia equivalente | Escolher uma tecnologia com melhor suporte
| RN07 | Grande | Baixo | 8 | Quem estiver na reunião passar o conteúdo para quem não compareceu | Verificar horários onde a maioria pode comparecer
| RN08 | Crítico | Alta | 20 | Indicar treinamentos para a equipe de desenvolvimento sobre a tecnologia escolhida | Estabelecer treinamentos constantes sobre a tecnologia escolhida | 
| RN09 | Crítico | Alta | 20 | Atualizar o documento para que fique coerente | Avaliação do documento por dois ou mais membros participantes do projeto
| RN10 | Crítico | Alta | 20 | Realizar refatoração de código, testes e validação com o cliente | Realizar treinamentos de todas as tecnologias utilizadas, garantir a realização de testes, boas práticas de programação e validação com o cliente 
| RN11 | Grande | Alta | 16 | Procurar ajuda de alunos, professores, pessoas de fora do ambiente universitário e aumentar a carga de estudos | Realização de pesquisas constantes e consultoria com outros alunos, professores e pessoas de fora do ambiente universitário
| RN12 | Grande | Alta | 16 | Realizar replanejamento da sprint utilizando a priorização do backlog do produto | Montar o backlog da sprint utilizando a priorização do backlog do produto
| RN13 | Grande | Alta | 16 | Ter consciência do projeto e se dedicar mais | Reuniões constantes e motivações por metas
| RN14 | Critico | Alta | 20 | Realizar reuniões com o grupo com o objetivo de mitigar desentendimentos | Atividades do grupo serem realizadas por votação da maioria 
| RN15 | Grande | Muito Alta | 20 | Realizar um replanejamento das histórias para que entrem em conformidade com os requisitos | Realizar constantes reuniões entre os membros da equipe, com o cliente e pesquisas necessárias para obtenção de conhecimento e compreensão sobre o escopo do projeto
| RN16 | Crítico | Alta | 20 | Realizar refatoração de código, testes e validação com o cliente | Realizar treinamentos de todas as tecnologias utilizadas, garantir a realização de testes, boas práticas de programação e validação com o cliente 
| RN17 | Grande | Alta | 16 | Reuniões para analisar os erros e não cometer novamente | Reuniões constantes para resoluções de issues em conjunto

### 5.1. Tabela de Probabilidade
| **Probabilidade** | **Intervalo** | **Peso** |
| --- | --- | --- |
| Muito Baixa | menor que 10% | 1 |
| Baixa | de 10% a 25% | 2 |
| Média | de 25% a 50% | 3 |
| Alta | de 50% a 75% | 4 |
| Muito Alta | maior que 75% | 5 |

### 5.2. Tabela de Impacto
| **Impacto** | **Descrição** | **Peso** |
| --- | --- | --- |
| Insignificante | Impacto insignificante para o andamento do projeto | 1 |
| Pequeno | Impacto com pouca influência no andamento do projeto | 2 |
| Médio | Impacto notável para o andamento do projeto | 3 |
| Grande | Impacto grave para o andamento do projeto | 4 |
| Crítico | Impacto crítico para o andamento do projeto | 5 |


### 5.3. Avaliação dos Riscos
| **Impacto/Probabilidade** | **Muito Baixa** | **Baixa** | **Média** | **Alta** | **Muito Alta** |
| --- | --- | --- | --- | --- | --- |
| Insignificante | 1 | 2 | 3 | 4 | 5
| Pequeno | 2 | 4 | 6 | 8 | 10
| Médio | 3 | 6 | 9 | 12 | 15
| Grande | 4 | 8 | 12 | 16 | 20
| Crítico | 5 | 10 | 15 | 20 | 25

## 6. Referências
"Gerenciamento dos riscos: O que é, objetivo e processos". Disponível em https://escritoriodeprojetos.com.br/gerenciamento-dos-riscos-do-projeto

BRASIL, Brasil; Ada - Plano de Gerenciamento de Riscos. Disponível em: https://fga-eps-mds.github.io/2019.1-ADA/#/docs/project/risk_management_plan

VILARINS, Augusto; FRANÇA, Emanoel; SOARES, Ingrid. GamesBI - Riscos. Disponível em: https://fga-eps-mds.github.io/2018.2-GamesBI/viabilidade/riscos.html
