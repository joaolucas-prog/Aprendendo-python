import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")
    numeroSecreto =random.randrange(1,101)
    total_tentativas = 0
    numeroValido= True
    pontuação = 0
    print("Escolha a dificuldade do jogo")
    print("(1)Fácil (2) Médio (3) Dificíl")
    while(numeroValido):
        dificuldade = input("Digite a dificuldade :")
        if(int(dificuldade) == 1):
            total_tentativas = 15
            numeroValido = False
        elif(int(dificuldade) == 2):
            total_tentativas = 10
            numeroValido = False
        elif(int(dificuldade) == 3):
            total_tentativas = 5
            numeroValido = False
        else:
            print("Digite uma dificuldade válida")
    for tentativa_atual in range(1,total_tentativas+1):
        print("Tentativa : {} de {} ".format(tentativa_atual,total_tentativas))
        chute_str = input("Digite um número :")
        chute = int(chute_str)
        if(chute <1 or chute >100):
            print("digite um numero entre 1 e 100")
            continue
        acertou = numeroSecreto == chute
        maior =   numeroSecreto < chute
        menor =   numeroSecreto > chute
        if(acertou):
            print("vc acertou!")
            pontuação = round(((total_tentativas) / total_tentativas + tentativa_atual) * 100)
            break
        else:
            if(maior):
                print("Vc chutou um numero maior")
            elif(menor):
                print("Vc chutou um numero menor")

    print("*********************************")
    print("Fim do jogo !!")
    if(not acertou):
        print("O Número secreto era : {}".format(numeroSecreto))
    print("Pontuação : {}".format(pontuação))
if (__name__ == "__main__"):
    jogar()