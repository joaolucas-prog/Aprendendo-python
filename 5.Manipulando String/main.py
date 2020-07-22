from ExtratorArgumentosUrl import ExtratorArgumentosUrl

#url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
url = "moedaorigem=real&moedadestino=dolar"
print(ExtratorArgumentosUrl.isUrl(url))
argumentosUlr = ExtratorArgumentosUrl(url)

moedaOrigem,moedaDestino = argumentosUlr.extraiArgumentos()
print(moedaOrigem,moedaDestino)