# Guia de Estilo e Identidade Visual

# Histórico de Revisão
| Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 15/03/2022 | 0.1 | Criação da versão inicial do documento| Mateus Franco |
| 15/03/2022 | 0.2 | Adição da introdução | Matheus Costa |
| 16/03/2022 | 0.3 | Adição das instruções da fonte | Mateus Franco |
| 17/03/2022 | 0.4 | Adição do nome da aplicação | Adne Moretti |
| 21/03/2022 | 0.5 | Adição da paleta de cores | Letícia Aires |

# 1. Introdução
Pensando em manter uma consistência na identidade visual do nosso projeto, este Guia visa documentar estilos, fontes, cores, dentre outros aspectos visuais importantes estabelecidos para o projeto, a fim de que se siga um padrão de desenvolvimento.

# 2. Detalhamento e Justificativas

## 2.1. Nome da aplicação

A respeito da escolha do nome da aplicação, surgiu a ideia de INDICAA.

Esse nome foi escolhido por se tratar de uma aplicação que utiliza Business Intelligence para apresentar indicadores com informações presentes no SIGAA, que é o site utilizado pelos coordenadores, alunos e professores da UnB. Sendo assim, fez-se a junção de **indicadores** com **SIGAA**, o que originou **INDICAA**.

Assim, esse nome se relaciona com o objetivo do projeto.

## 2.2. Fontes

A principal fonte à ser utilizada no desenvolvimento do projeto será: 

 - **UnB Pro** (Link para download: [download](http://marca.unb.br/fontesunb.php).)

Adotamos a fonte UnB Pro pois é uma das principais famílias tipográficas oficiais da UnB. Além disso, a fonte UnB Pro é compatível com os sistemas operacionais Linux, Windows e MacOS e está disponível gratuitamente para a toda a comunidade universitária sob licença de software livre. 

Para realizar a instalação local da fonte: Na página de downloads das Fontes, escolha o formato de arquivo desejado e clique para baixar. Depois de baixar, descompacte o arquivo e instale na pasta Fonts do sistema operacional. Se você tem alguma versão mais antiga das Fontes UnB no seu computador, desinstale antes de instalar a nova versão que você acaba de baixar.

### Utilização no projeto:
Primeiramente, deve-se incluir a pasta da fonte que foi realizado o donwload no próprio projeto, para assim incluir no HTML e CSS.
#### Incluindo no HTML

Coloca-se no <head> o seguinte trecho de código:

	<link href="caminho_da_pasta_da_fonte" rel="stylesheet">
Observação: O caminho da pasta será onde você colocou seu arquivo com as fontes. 
Por exemplo: 
    "C:\Users\userIndicaa\Downloads\UnB_Pro_v1.0\UnB_Pro_v1.0"
	

#### Incluindo no CSS

Coloca-se no css, para a utilização das fonte:

    font-family: 'UnB Pro';
	font-style: normal;

## 2.3. Paleta de cores
[comment]: <> (Responsável por Paleta de cores: Leticia)

![paleta de cores](https://user-images.githubusercontent.com/72623771/159377863-86b8210d-93eb-41c2-8929-ffc0a38105a9.png)

As cores foram selecionadas em se analisando características do produto e sua finalidade, bem como a acessibilidade, ou seja, de forma a construir um software adequado para a gestão institucional, optou-se por utilizar paleta da própria UnB. 
A ferramenta utilizada para construi-la foi a aplicação web [coolors](https://coolors.co/376996-56a3a6-364259-ef476f-edc841). 

As cores primárias são **#003366** e **#006633**, já **#F6F6F6** é secundária e a cor **#1D1D1D** é acento.

Com relação ao contraste, foram feitos testes e é recomendado ter estes números em mente para posterior utilização das cores.

<img src="https://user-images.githubusercontent.com/72623771/159379543-c3632383-70fe-4208-b014-c7c6ec90a9df.png" width="200"/>
<img src="https://user-images.githubusercontent.com/72623771/159380333-030eb755-e5ef-449b-b2d5-9b802746f3a5.png" width="200"/>
<img src="https://user-images.githubusercontent.com/72623771/159380545-3f31e9a7-4706-4d0c-bca0-153c2628b6cd.png" width="200"/>
<img src="https://user-images.githubusercontent.com/72623771/159380652-d7ab08f9-a29e-4f70-bb7f-9e2b11b302f9.png" width="200"/>
<img src="https://user-images.githubusercontent.com/72623771/159380788-6542f966-6778-407f-8810-e315df2dc4eb.png" width="200"/>
	
	
	
[comment]: <> (Responsável por Logo: Vitor)
	
A logo escolhida visou apresentar uma arte minimalista que representasse bem a UnB, tanto nas cores quanto no estilo.

<img src="/docs/assets/logo/logo.png" alt="contraste" width="200"/>
