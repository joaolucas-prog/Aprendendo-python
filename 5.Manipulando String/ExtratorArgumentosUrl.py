class ExtratorArgumentosUrl:

    def __init__(self,url):
        if self.isUrl(url):
            self.url = url.lower()
        else:
            raise LookupError ("URL Invalida !!!!!!!")
    def __len__(self):
        return len(self.url)
    @staticmethod
    def isUrl(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False
    def extraiArgumentos(self):
        buscaMoedaDestino = "moedadestino=".lower()
        buscaMoedaOrigem = "moedaorigem=".lower()
        indiceInicialMoedaDestino = self.encotraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestido = self.url.find("&valor")
        indiceInicialMoedaOrigem = self.encotraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[indiceInicialMoedaOrigem : indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestido]

        return moedaDestino,moedaOrigem
    def encotraIndiceInicial(self,moeda):
        return self.url.find(moeda) + len(moeda)
    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino","real",1)
    def extraiValor(self):
        buscaValor = "valor="
        indiceValorInicial = self.encotraIndiceInicial(buscaValor)
        valor = self.url[indiceValorInicial:]
        return valor