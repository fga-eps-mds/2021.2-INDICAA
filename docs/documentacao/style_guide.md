# Guia de Estilo e Identidade Visual

# Histórico de Revisão
| Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 15/03/2022 | 0.1 | Criação da versão inicial do documento| Mateus Franco |
| 15/03/2022 | 0.2 | Adição da introdução | Matheus Costa |
| 16/03/2022 | 0.3 | Adição das instruções da fonte | Mateus Franco |

# 1. Introdução
Pensando em manter uma consistência na identidade visual do nosso projeto, este Guia visa documentar estilos, fontes, cores, dentre outros aspectos visuais importantes estabelecidos para o projeto, a fim de que se siga um padrão de desenvolvimento.

# 2. Detalhamento e Justificativas

## 2.1. Nome da aplicação
[comment]: <> (Responsável por Nome da aplicação: Adne)

Sobre a escolha do nome da aplicação, teve-se a ideia de utilizar **Acacia**, em português **Acácia**

O nome foi escolhido por conta da história por trás da planta acácia: A acácia é uma árvore que participa de uma relação **__interespecífica__**, **__harmônica__** e **__facultativa__**, com formigas, chamada de **__Protocooperação__**. Isto é, nem a árvore e nem as formigas, espécies diferentes, tem a necessidade de participar deste processo, mas ambas se beneficiam caso optem por cooperar.

Tal conceito se relaciona com o propósito do nosso projeto de colaboração voluntária e estimulação do senso de comunidade.

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

![paleta de cores](img/identidade/paleta.png)

As cores foram selecionadas observando características do produto e sua finalidade, bem como a acessibilidade, testando-se o contraste. A ferramenta utilizada para construi-la foi [coolors](https://coolors.co/376996-56a3a6-364259-ef476f-edc841). 

A cor primária é a cor #376996, e a cor secundária #56a3a6. A cor #ef476f é acento.

Ainda, em relação ao contraste, foram feitos testes e é recomendado ter estes números em mente para utilização das cores.

<img src="img/identidade/contraste1.png" alt="contraste" width="200"/>

## 2.4. Logo
[comment]: <> (Responsável por Logo: Vitor)
	
A logo escolhida visou escolher uma arte minimalista que representasse bem a UnB, tanto nas cores quanto no estilo.

<img src="assets/logo/logo.png" alt="contraste" width="200"/>