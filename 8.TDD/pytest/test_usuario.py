#aqui estaremos utilizando o pytest no lugar do unittest
from dominio import Usuario , Lance , Leilao

def test_teste_deve_subtrair_a_carteira_do_usuario_quando_este_propor_um_lance():
    vini = Usuario('Vini', 100.0)

    leilao = Leilao("Celular")

    vini.propoe_lance(leilao,50.0)

    assert vini.carteira == 50.0 #equivalente ao assert do unitest