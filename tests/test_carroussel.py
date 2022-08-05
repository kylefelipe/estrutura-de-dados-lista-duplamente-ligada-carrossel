# Testes do Carousel

from carousel import Carousel, Empty
import pytest


def test_validar_Carousel_esta_vazio():
    carroussel = Carousel([])
    assert carroussel.is_empty == True


def test_valida_ir_para_proximo_em_Carousel_vazia():
    expect_text = 'Carousel está vazio!'
    carroussel = Carousel([])
    with pytest.raises(Empty, match=expect_text):
        assert carroussel.next()


def test_valida_ir_para_anterior_em_Carousel_vazia():
    expect_text = 'Carousel está vazio!'
    carroussel = Carousel([])
    with pytest.raises(Empty, match=expect_text):
        assert carroussel.prev()


def test_adiciona_item_num_Carousel():
    carrossel = Carousel([])
    assert len(carrossel) == 0
    carrossel.append(1)
    assert len(carrossel) == 1


def test_remove_ultimo_item_do_Carousel():
    carrossel = Carousel(list(range(5)))
    assert len(carrossel) == 5
    removido = carrossel.pop()
    assert len(carrossel) == 4
    assert removido == 4

def test_remove_item_do_Carousel_pelo_indice():
    carrossel = Carousel(list(range(5)))
    removido = carrossel.pop(1)
    assert len(carrossel) == 4
    assert removido == 1


def test_item_atual_deve_ser_None():
    carrossel = Carousel(list(range(5)))
    assert carrossel.atual is None


def test_deve_retorna_item_atual_sem_remover():
    carrossel = Carousel(list(range(5)))
    atual = next(carrossel)
    assert atual == 0
    assert len(carrossel) == 5


def test_deve_ir_para_proximo():
    carrossel = Carousel(list(range(5)))
    assert next(carrossel) == 0


def test_deve_ir_para_anterior():
    carrossel = Carousel(list(range(5)))
    assert carrossel.prev() == 4


def test_deve_avancar_em_loop():
    carrossel = Carousel(list(range(5)))
    count = 0
    while count <= 5:
        carrossel.next()
        count += 1
    assert carrossel.atual == 0


def test_deve_retroceder_em_loop():
    carrossel = Carousel(list(range(5)))
    count = 0
    while count <= 5:
        carrossel.prev()
        count += 1
    assert carrossel.atual == 4
