from dominio import Usuario , Lance , Leilao,Avaliador

gui = Usuario('Gui')
yuri = Usuario("Yuri")

lance_yuri = Lance(yuri,140.0)
lance_gui = Lance(gui,100.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_gui)
leilao.lances.append(lance_yuri)

for lance in leilao.lances:
    print(f" O usuario {lance.usuario.nome} deu um lance de R$ {lance.valor}")

avaliador = Avaliador()

avaliador.avalia(leilao)

print(f"O menor lance foi {avaliador.menor_lance} , e o maior lance foi de {avaliador.maior_lance}")

if (__name__ == "__main__"):
    pass