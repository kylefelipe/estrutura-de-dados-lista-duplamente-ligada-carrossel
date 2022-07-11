################################################################################
# Criado por Kyle Felipe
# Criado em 2022/07/10
# Contato: kylefelipe at gmail.com
# Please, se for útil, #citaNois
# repositorio: https://github.com/kylefelipe/estrutura-de-dados-lista-duplamente-ligada-carrossel
# www.kylefelipe.com
################################################################################

class Empty(Exception):
    """Classe de erro quando o Carousel estiver vazio"""
    pass


class Carousel:
    """Itera em loop em um array.
    Parametros opcionais:
    array: Uma lista de itens.
    posittion: Posição por onde começar a iteração com o Carousel
    Metodos:
    is_empty() -> Booleano: Retora true se o Carousel estiver vazio.
    next() -> item: Vai para o próximo item e o retorna, caso o item atual
                    seja  None, vai para o primeiro item, o item retornado não é
                    removido.
    prev() -> item: Vai para o item anterior e o retorna, caso o item atual
                    seja  None, vai para o útlimo item, o item retornado não é
                    removido. 
    append(item): Adiciona um novo item no final do Carousel.
    pop([i]) -> item: Remove um item do Carousel e o retorna, o i padrão é -1.
    atual() -> item: Retorna o item atual do Carousel, o item retornado não é
                    removido
    posicao() -> inteiro: Retorna a posição (indice) atual no Carousel.
    """

    def __init__(self, array=None, position=None):
        self._data = array or []
        self._size = len(self._data)
        self._atual = position

    def __len__(self) -> int:
        """Retorna o número de elementos no Carousel"""
        return self._size

    def is_empty(self) -> bool:
        """Retorna se o Carousel estiver vazio"""

        return self._size == 0

    def __iter__(self):
        return self

    def __next__(self):
        """Vai para o próximo item no Carousel, caso o item atual for None
        vai para o primeiro item.
        Esse método permite que o Carousel seja usado com o next(Carousel)
        """

        if self.is_empty():
            raise Empty('Carousel está vazio!')
        if self._atual is None:
            self._atual = 0
        else:
            self._atual = (self._atual + 1) % self._size

        return self._data[self._atual]

    def __str__(self) -> str:
        """Representação do Carousel"""
        return f'{self._data}'

    def append(self, item) -> None:
        """Adiciona um item no final do Carousel"""
        self._data.append(item)
        self._size += 1

    def pop(self, index=-1):
        """Remove um item do Carousel e o retorna
        Padrão do indice removido é -1"""
        if self.is_empty():
            raise Empty('Carousel está vazio')
        removed = self._data.pop(index)
        self._size -= 1
        return removed

    def prev(self):
        """Vai para o item anterior no Carousel, caso o item atual for None
        vai para o último item, o item retornado não é removido."""
        if self.is_empty():
            raise Empty('Carousel está vazio!')
        if self._atual is None:
            self._atual = self._size - 1
        else:
            self._atual = (self._atual + self._size - 1) % len(self._data)

        return self._data[self._atual]

    def next(self):
        """Chama o método __next__().
        Vai para o próximo item no Carousel, caso o item atual for None
        vai para o primeiro item, o item retornado não é removido.
        """
        return self.__next__()

    def atual(self):
        """Retorna o item atual do Carousel, sem removê-lo"""
        if self.is_empty():
            raise Empty('Carrossel está vazio!')
        if self._atual is None:
            return None
        return self._data[self._atual]

    def posicao(self) -> int:
        if self.is_empty():
            raise Empty('Carousel está vazio!')
        return self._atual
