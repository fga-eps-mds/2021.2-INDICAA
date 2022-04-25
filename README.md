<div align="center"><img id="indicaa-logo" src="assets/logo.svg"></img></div><br/>

<div align="center">
<img src="https://img.shields.io/github/issues/fga-eps-mds/2021.2-INDICAA?style=for-the-badge"></img> <img src="https://img.shields.io/github/issues-closed/fga-eps-mds/2021.2-INDICAA?style=for-the-badge"></img> <img src="https://img.shields.io/github/issues-pr/fga-eps-mds/2021.2-INDICAA-Wiki?style=for-the-badge"></img> <img src="https://img.shields.io/github/issues-pr-closed/fga-eps-mds/2021.2-INDICAA-Wiki?style=for-the-badge"></img> <img src="https://img.shields.io/github/repo-size/fga-eps-mds/2021.2-INDICAA-Wiki?style=for-the-badge"> <img src="https://img.shields.io/github/license/fga-eps-mds/2021.2-INDICAA?style=for-the-badge"></img> <img src="https://img.shields.io/github/v/release/fga-eps-mds/2021.2-INDICAA?style=for-the-badge"></img> <img src="https://img.shields.io/github/last-commit/fga-eps-mds/2021.2-INDICAA-Wiki?style=for-the-badge"></img>
</div><br/>

[INDICAA](https://indicaa.herokuapp.com/) é um projeto desenvolvido por alunos da matéria de Métodos de Desenvolvimento de Software da [Universidade de Brasília - UnB](https://www.unb.br/) com o objetivo de facilitar o acesso às informações apresentadas pelo site acadêmico [SIGAA oferta](https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino).

Nós somos um projeto que visa a busca e a disponibilização visual de informações acadêmicas relevantes aos coordenadores da Universidade de Brasília - UnB, e também, possibilitar a pesquisa e a filtragem de dados por meio da interface do [Metabase](https://www.metabase.com/).

No contexto da pandemia, a gestão de espaços se tornou fundamental para o bom funcionamento da UnB. Nesse contexto, a equipe de coordenação voltou seus esforços para propiciar uma boa divisão das disciplinas e atividades no geral de acordo com o espaço existente. Para tal, a visualização da divisão dos espaços de acordo com os períodos do dia é essencial para uma melhor tomada de decisões pelos gestores, o que impactará diretamente a execução das atividades acadêmicas da universidade.

-   [Documentação do projeto](https://fga-eps-mds.github.io/2021.2-INDICAA-Wiki/)

Utilizando a interface do _**Metabase**_, é possível visualizar os dashboards já criados pela equipe de desenvolvedores do projeto INDICAA, criar novos dashboards conforme necessidade de obtenção de dados mais específicos, visualizar os dados retirados do site SIGAA e armazenados no banco de dados INDICAA e também, filtrar os dados que estão sendo visualizados com base nas categorias disponíveis.

![image](https://user-images.githubusercontent.com/62526025/163576771-5e0479f7-e859-4d76-9041-e8951c7462fe.png)

## ⌨️🔨 Linguagens e ferramentas utilizadas

<div align="center">
<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white"></img> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"></img> <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white"></img> <img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?&style=for-the-badge&logo=Canva&logoColor=white"></img> <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"></img> <img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white"></img> <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white"></img> <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white"></img> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"></img> <img src="https://img.shields.io/badge/Metabase-509EE3?style=for-the-badge&logo=metabase&logoColor=fff"></img>
</div>

## 📑 Releases previstas

-   <a href="https://github.com/fga-eps-mds/2021.2-INDICAA/releases/tag/v0.1"><img src="https://img.shields.io/badge/Release_1-v0.1-green?style=for-the-badge"></img><img src="https://img.shields.io/badge/Date-07%2F03%2F2022-lightgrey?style=for-the-badge"></img></a>
-   <img src="https://img.shields.io/badge/Release_2-v0.2-yellow?style=for-the-badge"></img><img src="https://img.shields.io/badge/Date-26%2F04%2F2022-lightgrey?style=for-the-badge"></img>

# 🚀💾 Instalação e execução do projeto

## 🌎 Acesso ao projeto em sua versão de produção (na web)

- [Metabase](https://indicaa.herokuapp.com/)
  
- [API](https://indicaa-api.herokuapp.com/)

## 🏭 Rodando o projeto em versão de desenvolvimento (localmente)

### Instalação das tecnologias

🐋 Docker cli:

Confira se o docker está instalado em sua máquina.

```sh
docker version
```
O comando acima deve retornar uma mensagem com a versão do docker instalada em sua máquina. Caso o Docker não esteja instalado, visite a [página oficial de instruções de instalação](https://docs.docker.com/engine/install/ubuntu/) e faça o passo a passo descrito.

É recomendada a utilização de versões >= _**20.10.14**_.

🐍 Python:

Verifique a versão instalada do python.

```sh
python --version
```
ou
```sh
python3 --version
```
Os comandos acima devem retornar algo como: 
```Python 3.9.0```
. Isso significa que o python está instalado e sua versão é a 
3.9.0.

É recomendada a utilização de versões >= _**3.9.x**_. Caso necessário, siga o passo a passo informado na [página oficial de instruções de instalação](https://python.org.br/instalacao-linux/).

#
### Execução

🚀 GitHub Pages

Clonar este repositório:
```sh
git clone https://github.com/fga-eps-mds/2021.2-INDICAA-Wiki 
```
Entrar na pasta em que o clone está localizado:
```sh
cd 2021.2-INDICAA-Wiki
```
Instalar os pacotes _**mkdocs material**_ e _**mkdocstrings**_
```sh
pip install mkdocs-material mkdocstrings
```
Rodar o gitpages localmente:
```sh
mkdocs serve
```
Agora, o git pages (versão de desenvolvimento) deve estar disponível em: ```http://127.0.0.1:6969/```

🧭 API

Clonar o repositório [INDICAA](https://github.com/fga-eps-mds/2021.2-INDICAA/):
```sh
git clone https://github.com/fga-eps-mds/2021.2-INDICAA
```
Entrar na pasta em que o clone está localizado:
```sh
cd 2021.2-INDICAA
```

Com o docker instalado na sua máquina, rodar:
```sh
docker-compose up
```
A instrução acima rodará a ```aplicação``` do INDICAA, ou seja, criará um banco de dados **POSTGRE**, posteriormente é feito o scraping das informações obtidas através do [SIGAA](https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino) e, por fim, será hospedado o Metabase, a partir de uma imagem do **Docker Hub**.

A **API** deve estar disponível em: ```http://127.0.0.1:8000/```

E o **Banco de Dados POSTGRE** deve estar disponível em: ```http://127.0.0.1:5432/```

_**Obs.:**_ Note que terá uma demora na execução e esse processo é totalmente normal.

📊 Metabase

O **Metabase** deve estar disponível em: ```http://127.0.0.1:3000/```

Como é o primeiro acesso a imagem criada pelo **Docker Hub**, será necessário realizar uma configuração prévia, seguindo as etapas descritas na [issue.](https://github.com/fga-eps-mds/2021.2-INDICAA/issues/87#issuecomment-1075163142)



# 🤝 Contribuições

O projeto INDICAA é um projeto Open Source e de software livre desenvolvido por alunos da disciplina de Métodos de Desenvolvimento de software da UnB. Com isso, o projeto é de livre contribuição e reprodução. Vale apenas ressaltar que é necessário que sejam seguidas as [regras de contribuição](https://fga-eps-mds.github.io/2021.2-INDICAA-Wiki/contributing/) e o [código de conduta do projeto](https://fga-eps-mds.github.io/2021.2-INDICAA-Wiki/CODE_OF_CONDUCT/).

# 🔐 Licença

Este projeto está licenciado sob os termos estabelecidos pela [GNU General Public License v3.0](https://github.com/fga-eps-mds/2021.2-INDICAA/blob/main/LICENSE).
