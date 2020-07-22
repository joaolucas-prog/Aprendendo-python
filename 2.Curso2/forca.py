import random

def jogar():
    mensagemBemvindo()
    buscarPalavrasArquivo()
    palavras = buscarPalavrasArquivo()
    enforcou = False
    acertou = False
    palavraSecreta = palavras[random.randrange(0,len(palavras))].upper()#pega uma palavra aleatoria da lista
    letrasAcertadas = ["_" for letra in palavraSecreta]#coloca os "_" pelo tamanho da palavra
    erros = 0
    print(letrasAcertadas)
    while(not enforcou and not acertou ):#famoso game lopping
        chute = pedirChute()
        if(chute in palavraSecreta):
            marcarForca(chute, palavraSecreta , letrasAcertadas)
        else:
            erros +=1
            desenha_forca(erros)
        acertou = ("_" not in letrasAcertadas)
        enforcou = (erros == 7)
        print(letrasAcertadas)
    if(acertou):
        mensagemWinner()
    else:
        mensagemLoser(palavraSecreta)
    mensagemFimJogo()

def marcarForca(chute, palavraSecreta , letrasAcertadas):
    index = 0
    for letra in palavraSecreta:
        if (chute == letra):  # and palavra[index] == "-"):
            # palavra[index]=chute
            letrasAcertadas[index] = chute.upper()
        index += 1

def pedirChute():
    chute = input("digite uma letra :")
    chute = chute.strip().upper()
    return chute
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
def mensagemWinner():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagemLoser(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra secreta é {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagemBemvindo():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

def buscarPalavrasArquivo():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    return palavras

def mensagemFimJogo():
    print("*********************************")
    print("Fim do jogo !!")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()