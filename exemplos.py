# Exemplos de uso

# Criando instâncias
from carousel import Carousel

# Iniciando um carrossel vazio.
carrossel = Carousel()

# Iniciando um carrossel com uma lista.
carrossel_original = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                              'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])

# Adicionando itens

carrossel_original.append('Firmino')
print(carrossel_original)
# >> ['Profa. Helena Fernandez', 'Maria Joaquina', 'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo', 'Firmino']

# Item atual e a posição atual

print(f'item atual: {carrossel_original.atual}')
# >> None

print(f'Posição atual: {carrossel_original.posicao}')
# >> None

carrossel_original.next()

print(f'item atual: {carrossel_original.atual}')
# >> Profa. Helena Fernandez

print(f'item atual: {carrossel_original.posicao}')
# >> 0

# Carousel.next()

carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                     'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])

print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: None - Item Atual: None

proximo = carrossel.next()
print(f"Próximo item: {proximo}")
print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: 0 - Item Atual: Profa. Helena Fernandez

print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                     'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])
print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: None - Item Atual: None

# Built-in next()
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                     'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])
print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: None - Item Atual: None

proximo = next(carrossel)
print(f"Próximo item: {proximo}")
print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: 0 - Item Atual: Profa. Helena Fernandez

print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

# Carousel.prev()

carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                     'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])
print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: None - Item Atual: None

anterior = carrossel.prev()
print(f"Item anterior: {anterior}")
# > Item anterior: Jaime Palillo
print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# Posição atual: 3 - Item Atual: Jaime Palillo

print(f"Tamanho do carrossel: {len(carrossel)}")
# 6

# Carousel.pop()
print(f"Tamanho antes da inserção: {len(carrossel)}")
carrossel.append('Laurinha')
print(carrossel)
removido = carrossel.pop()
print(f"Tamanho após remoção: {len(carrossel)} - item removido: {removido}")
print(carrossel)
# Removendo o item 0
removido = carrossel.pop(0)
print(
    f"Tamanho após remoção do item 0: {len(carrossel)} - item removido: {removido}")
print(carrossel)

# Iterações ciclicas
# usando next()
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                     'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])

for i in range(len(carrossel) + 3):
    print(f"Próximo {next(carrossel)}")

# usando Carousel.prev()
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                     'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'])

for i in range(len(carrossel) + 3):
    print(f"Anterior {carrossel.prev()}")

# Indicando o atual
carrossel = Carousel(['Profa. Helena Fernandez', 'Maria Joaquina',
                     'Cirilo Rivera', 'Suzana Bustamante', 'Carmen Carrillo', 'Jaime Palillo'], 2)
print(
    f"Posição atual: {carrossel.posicao} - Item Atual: {carrossel.atual}")
# > Posição atual: 2 - Item Atual: Cirilo Rivera

# Excessões
# Carousel vazio

from carousel import Empty

try:
    carrossel_vazio = Carousel()  # ou Carousel([])
    carrossel_vazio.next()
except Empty as err:
    print(err)
# > Carousel está vazio!
