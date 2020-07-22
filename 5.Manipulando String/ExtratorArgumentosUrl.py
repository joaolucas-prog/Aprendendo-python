class ExtratorArgumentosUrl:

    def __init__(self,url):
        if self.isUrl(url):
            self.url = url
        else:
            raise LookupError ("URL Invalida !!!!!!!")

    @staticmethod
    def isUrl(url):
        if url:
            return True
        else:
            return False
    def extraiArgumentos(self):

        indiceInicialMoedaDestino = self.url.find("=",15) +1

        indiceInicialMoedaOrigem = self.url.find("=") + 1
        indiceFinalMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[indiceInicialMoedaOrigem : indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaDestino,moedaOrigem