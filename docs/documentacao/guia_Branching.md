# Políticas de branch

## As branches criadas neste repositório devem seguir os padrões a seguir:

Uma breve explicação sobre o fluxo de trabalho:
### main

- A branch _main_ representa uma versão estável do produto, contendo código já testado, versionado e revisado, pronto para ser entregue ao usuário final. Esta branch partirá através da branch _develop_ através de pull requests aprovados ao final de cada release.

Regras:

1. Existe apenas UMA branch _main_.
2. **Não** são permitidos commits feitos diretamente na branch _main_.

### develop
- A branch _develop_ contém a versão mais atualizada do código que está sendo desenvolvido. Esta branch está sempre sincronizada com a _main_ e é base para as branches _feature_.

Regras:

1. Existe apenas UMA branch _develop_.
2. Esta branch sempre é mesclada à branch _main_.

### feature
- As branches _feature_ representam as funcionalidades do sistema a serem desenvolvidas. Elas devem ter a branch _develop_ como sua origem e fim.

Regras de nomenclatura:

```
feature/(#Id-da-issue)-título-da-issue
```

### release
- A branch _release_ representa o conjunto de funcionalidades provenientes de um ponto específico da branch _develop_. Esta branch contém funcionalidades prontas que, provavelmente, estarão presentes na próxima versão estável do produto. Apenas **bug fixes** são permitidos nesta branch.

Regras:

1. Esta branch é criada sempre a partir da branch _develop_.
2. Esta branch é mesclada às branches _develop_ e _main_.
3. Esta branch aceita apenas mesclagens de branches do tipo _bugfix_.


Regras de nomenclatura:

```
release/vNúmero-da-versão
```

### bugfix
- As branches do tipo _bugfix_ são utilizadas para implementar soluções para bugs, encontrados através de testes realizados em releases específicas, na branch _release_. Isso significa que a branch _bugfix_ deve ter a branch _release_ como sua origem e fim.

Regras:

1. Esta branch sempre é criada a partir da branch _release_.
2. Esta branch sempre é mesclada à branch _release_.

Regras de nomenclatura:

```
bugfix/(#Id-da-issue)-título-da-issue
```

### hotfix
- A branch _hotfix_ é utilizada para implementar soluções para problemas urgentes encontrados no ambiente de produção. Isso significa que esta branch deve ter a branch _main_ como sua origem e fim.

Regras:

1. Esta branch sempre é criada a partir da branch _main_.
2. Esta branch sempre é mesclada à branch _main_.

Regras de nomenclatura:

```
hotfix/(#Id-da-issue)-título-da-issue
```