# Estrutura de dados - lista duplamente ligada (Carrossel)

Praticando o [Python](www.python.org) tentando implementar uma estrutura ciclica, onde sempre fosse possível ir para o próximo item (`next()`) e quando chegasse no último item, ele retornasse para o primeiro.  
A idéia é fazer o _carrossel_ de um parque de diversões, só que nesse exemplo, o carrossel consegue rodar no sentido contrário também, remover e adicionar novos itens.

## Preparação

Para rodar os testes, pode criar um ambiente virtual isolado.  

```Shel
python3 -m venv .venv

source .venv/bin/activate # Ativando o ambiente - considere o shel que estiver usando

(.venv) pip install -r dev_requirements # Instalar as libs necessárias no python do ambiente
```

Para rodar os testes:

```shell
python -m pytest
```

## Modo uso

o Carrossel não precisa de lib especial para ser utilizado, por isso não criei um `requirements`.

### Criando instâncias

Para usar, basta importar o carrossel em um arquivo python que deseja e criar uma instância.

```Python
from carousel import Carousel

# Iniciando um carrossel vazio.
carrossel = Carousel()

# Iniciando um carrossel com uma lista.
carrossel_original = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])
```

### Adicionando itens

Para adicionar itens em um carrossel, podemos usar o metodo `<Caroussel>.append(item)`, e o item será adicionado ao final.

```Python
carrossel_original.append('Firmino')
print(carrossel_original)
#>> ['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo', 'Firmino']
```

### Item atual e a posição atual

O Carousel tem um metodo para retornar o item atual e outro para retornar posição atual(index), caso tenha acabado de criar a instância, ambos retornarão `None`:

```Python

print(f'item atual: {carrossel_original.atual}')
#>> None
print(f'Posição atual: {carrossel_original.posicao}')
#>> None

carrossel_original.next()

print(f'item atual: {carrossel_original.atual}')
#>> Profa. Helena Fernandez

print(f'item atual: {carrossel_original.posicao}')
#>> 0
```

> Observe que, quando o item atual é `None` ao usarmos o `next()` o Carousel vai para o começo.

### Avançando e retrocedendo

O para iterar com os itens do carrossel, podemos usar os métodos `<Carousel>.next()` ou `<Carousel>.prev()`, esses métodos não removem o item retornado:  

> Caso não tenha ocorrido nenhuma iteração, o item atual será sempre `None`

#### Carousel.next()

Vai para o próximo item do Carousel, caso o item atual seja `None` vai para o primeiro item.

```Python
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])
print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

print(f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: None - Item Atual: None

proximo = carrossel.next()
print(f"Próximo item: {proximo}")
print(f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: 0 - Item Atual: Profa. Helena Fernandez

print(f"Tamanho do carrossel: {len(carrossel)}")
# 6
```

Podemos usar o metodo built-in do [Python](www.python.org) `next()` para ir para o próximo também.

```Python
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])
print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

print(f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: None - Item Atual: None

proximo = next(carrossel)
print(f"Próximo item: {proximo}")
print(f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: 0 - Item Atual: Profa. Helena Fernandez

print(f"Tamanho do carrossel: {len(carrossel)}")
# 6
```

#### Carousel.prev()

Vai para o item anterior do Carousel, caso o item atual seja `None` vai para o último item.

```Python
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])
print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

print(f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: None - Item Atual: None

anterior = carrossel.prev()
print(f"Item anterior: {anterior}")
#> Item anterior: Jaime Palillo

print(f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: 3 - Item Atual: Jaime Palillo

print(f"Tamanho do carrossel: {len(carrossel)}")
# Tamanho do carrossel: 6
```

### Carousel.pop()

O método `Carousel.pop([i])` remove um item do Carosel e o retorna no index informado, caso não seja passado nenhum indice, o último item será removido.

```python
print(f"Tamanho antes da inserção: {len(carrossel)}")
#> Tamanho antes da inserção: 6
carrossel.append('Laurinha')
print(carrossel)
#> ['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo', 'Laurinha']
removido = carrossel.pop()
print(f"Tamanho após remoção: {len(carrossel)} - item removido: {removido}")
#> Tamanho após remoção: 6 - item removido: Laurinha
print(carrossel)
# Removendo o item 0
removido = carrossel.pop(0)
print(f"Tamanho após remoção do item 0: {len(carrossel)} - item removido: {removido}")
#> Tamanho após remoção do item 0: 5 - item removido: Profa. Helena Fernandez
print(carrossel)
#> ['Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo']
```

### Iteranções cíclicas

O interessante desse Carousel é que pode haver infitas iterações em seus item sem nunca termos um erro disparado.

> Cuidado com loops eternos

```python
# Usando next()
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])

for i in range(len(carrossel) + 3):
print(next(carrossel))

# usando Carousel.prev()
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])

for i in range(len(carrossel) + 3):
  print(f"Anterior {carrossel.prev()}")
```

## Indicando a possição atual

Ao criar um Carousel é possível indicar uma posição (index) por onde iniciar, esse index será a posição atual.

```python
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                     'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'], 2)
print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# > Posição atual: 2 - Item Atual: Cirilo Rivera
```

## Excessões (Erros)

### Carousel vazio

Em alguns métodos, quando o Carousel estiver vazio, uma excessão `Empty` será disparada, são eles:

* `.atual`
* `.next() | next(<Carousel>`
* `.posicao`
* `.pop()`
* `.prev()`

Exemplo:

```Python
from carousel import Empty

try:
  carrossel_vazio = Carousel() # ou Carousel([])
  carrossel_vazio.next()
except Empty as err:
  print(err)
#> Carousel está vazio!
```

## Observações

Foram usados os personagens da novela [Carrossel](https://pt.wikipedia.org/wiki/Elenco_de_Carrossel) para exemplificar os usos.
