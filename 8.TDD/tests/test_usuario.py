#aqui estaremos utilizando o pytest no lugar do unittest
from dominio import Usuario , Lance , Leilao
import pytest

@pytest.fixture
def vini():
    return Usuario('Vini',100.0)

@pytest.fixture
def leilao():
    return Leilao("Celular")

def test_teste_deve_subtrair_a_carteira_do_usuario_quando_este_propor_um_lance(vini ,leilao):
    vini.propoe_lance(leilao,50.0)

    assert vini.carteira == 50.0 #equivalente ao assert do unitest

def test_deve_permitir_propor_um_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(vini ,leilao):
    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0

def test_deve_permitir_propor_um_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini ,leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0

def test_nap_deve_permitir_propor_um_lance_quando_o_valor_eh_maior_que_o_valor_da_carteira(vini ,leilao):
    with pytest.raises(ValueError):
        vini.propoe_lance(leilao, 101.0)