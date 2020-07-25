class Estudo:
#__init__ ela inicializa seu objeto e especifica os atributos
    def __init__(self):
        self.variavel = "variavel"
#__len__ Relembrando os metodos especias eles adicionam uma funcionalidade a classe ao chamar um metodo especifico
#por exemplo len(objeto) se eu fizer o len em um objeto de uma classe que eu criei oque ele irá fazer?
#se eu n tiver o metodo especial __len__ ele irá dar um erro mas eu posso da uma funcionalidade
#como retornar algum valor ou qualquer outra coisa
    def __len__(self):
        return 10
#__str__ Ela cria uma definição em string sobre a classe equivalente ao toString() no Java
    def __str__(self):
        return "CLasse secreta , retorna nada n"
#__eq__ ele faz uma comparação com o objeto da sua classe

    def __eq__(self, other):
        return self.variavel == other.variavel

"""__eq__(), chamado pelo operador ==
__ne__(), chamado pelo operador !=
__gt__(), chamado pelo operador >
__lt__(), chamado pelo operador <
__ge__(), chamado pelo operador >=
__le__(), chamado pelo operador <="""