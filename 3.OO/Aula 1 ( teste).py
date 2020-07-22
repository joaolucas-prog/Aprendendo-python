#aqui tentamos criar um "objeto" uma forma de encapsular um obejeto,porem com alguns problemas ainda
#pois como um outro programador saberia quais atributos esse objeto tem
# e como que a gente criaria métodos exclusivos nela nela ?

def criar_conta(numero,titular,saldo,limite):
    conta  = {"numero" : numero,"titular" : titular,"saldo" : saldo ,"limite" : limite}
    return conta

def deposita(conta,valor):
    conta["saldo"]+= valor
def saca(conta , valor):
    conta["saldo"] -= valor
def extrato(conta):
    print("Seu saldo é {}".format(conta["saldo"]))