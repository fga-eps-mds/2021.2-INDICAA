# Dicionário de Dados

## Entidade: Unidade

|Atributo|Propriedades do atributo|Tipo de dado|Tamanho|Descrição|Exemplo|
|-|-|-|-|-|-|
|nome|Chave primária<br>Obrigatório|varchar|255|Nome do departamento|"Faculdade do Gama"|

## Entidade: Materia

|Atributo|Propriedades do atributo|Tipo de dado|Tamanho|Descrição|Exemplo|
|-|-|-|-|-|-|
|codigoMateria|Chave primária<br>Obrigatório|varchar|7|Codigo da Materia|"FGA0003"|
|cargaHoraria|Obrigatório|varchar|3|Carga Horária da Matéria|"60h"|
|nome|Obrigatório|varchar|255|Nome da Matéria|"COMPILADORES 1"|

## Entidade: Turma

|Atributo|Propriedades do atributo|Tipo de dado|Tamanho|Descrição|Exemplo|
|-|-|-|-|-|-|
|docente|Chave primária<br>Obrigatório|varchar|50|Nome completo do docente|"FABIO MACEDO MENDES"|
|codigoTurma|Chave primária<br>Obrigatório|varchar|2|Código da Turma|"01" ou "A"|
|horario|Obrigatório|varchar|20|Horário da Turma seguindo o padrão do SIGAA|"5M1234 5T23"|
|vagasOfertadas|Obrigatório|int|---------|Quantidade de vagas ofertadas|40|
|vagasOcupadas|Obrigatório|int|---------|Quantidade de vagas ocupadas|0|
|local|Obrigatório|varchar|40|Local da aula da Turma|"remoto" ou "I10"|
|ano|Obrigatório|int|---------|Ano do Período|2021|
|semestre|Obrigatório|int|---------|Semestre do Período|2|
