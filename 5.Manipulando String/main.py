from ExtratorArgumentosUrl import ExtratorArgumentosUrl

#url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
print(ExtratorArgumentosUrl.isUrl(url))
argumentosUlr = ExtratorArgumentosUrl(url)

moedaOrigem,moedaDestino = argumentosUlr.extraiArgumentos()
valor = argumentosUlr.extraiValor()
print(moedaOrigem,moedaDestino,valor)