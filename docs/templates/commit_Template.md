---
tag: "politicas"
---
Padronização dos commits no projeto. 

## Histórico de Versões


| Data       | Versão | Descrição                      | Autor             |
| :--------: | :----: | :----------:                   | :---------------: |
| 14/02/2022 |  0.1   | Criação da política de commits | [Matheus Pimentel](https://github.com/Matheuspleal)|

## Semântica do Commit

Os commits devem seguir o seguinte padrão:

### Princípios:

#### Commits atômicos
Sempre dividir em pequenos e significativos commits, fazendo com que cada commit tenha apenas uma funcionalidade.

#### Commits em português
Por ser um projeto voltado totalmente para um público brasileiro e por toda equipe ter mais afinidade com o português, foi decidido que todos os commits serão em pt-BR.

### Formato:
```
<tipo>(#número da issue): assunto
```

#### Tipos:
```Para inserir um emoji, basta digitar: ":nome_do_emoji:". Exemplo: ":bulb:"```

[***Lista de emojis disponíveis em markdown***](https://gist.github.com/rxaviers/7360908)

- :bulb: quando adicionar nova funcionalidade
- :repeat: quando alguma alteração for feita
- :cool: quando melhorias de formato/estrutura do código
- :racehorse: quando melhorar o desempenho
- 🚱  quando resolver memory leaks
- :pencil: quando escrever documentação
- :bug: quando consertar um problema
- :fire: quando remover código ou arquivos
- :green_heart: quando consertar problemas de Integração Contínua
- :white_check_mark: quando adicionar testes
- :lock: quando lidar com segurança
- :arrow_up: quando realizar o upgrade de dependências
- :arrow_down: quando realizar downgrade de dependências

#### Assunto:
- Deve possuir no máximo 50 caracteres
- Devem estar em letras minúsculas

*Exemplo de commit:*
```
git commit -m ":bulb:(#02): botão na página inicial"
```

## Referências

DARTORA, João. Tudo o que você precisa saber sobre commits semânticos. *Ilegra*. Disponível em: <https://ilegra.com/blog/tudo-o-que-voce-precisa-saber-sobre-commits-semanticos/>. Acesso em: 09 de ago. de 2021.

Políticas de Commit. Disponível em: <https://fga-eps-mds.github.io/2020.1-Grupo6/policies/commits/>. Acesso em: 09 de ago. de 2021

Políticas de Commit. Disponível em: <https://github.com/fga-eps-mds/2021.1-AlligaBot/blob/main/docs/_posts/2021-08-18-commits.md>. Acesso em: 14 de fev. de 2022