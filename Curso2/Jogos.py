import Curso1.JogoAdivinhacao
import Curso1.forca

def menuJogos():
    print("*********************************")
    print("***Bem vindo ao menu de jogos!***")
    print("*********************************")
    print("Escolha qual jogo você quer jogar")
    print("     (1)Forca (2)Adivinhação     ")
    jogo = int(input("Digite a opção: "))

    if(jogo == 1):
        Curso1.forca.jogar()
    if (jogo ==2 ):
        Curso1.JogoAdivinhacao.jogar()
if(__name__ == "__main__"):
    menuJogos()