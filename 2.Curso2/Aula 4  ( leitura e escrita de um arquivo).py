#para abrir um arquivo para escrita open("nomearquivo","w") ,caso exista um arquivo com esse nome ele apaga
#para evitar isso utilize open("nomearquivo","a") "append"

#para abrir um arquivo para leitura open("nomearquivo","r")

#sempre que abrir um arquivo vc deve fecha-lo usando nomearquivo.close()

#para escrever algo no arquivo utili-ze o nomearquivo.write(string)

#para ler o conteúdo do arquivo vc utiliza nomearquivo.read() ele faz uma leitura completa do arquivo
#e só posso ser chamado uma vez pois o "ponteiro" da leitura estará no final

# para ler a linha a linha do arquivo vc faz um laço for
# for linha in open("nomearquivo","r"):
#     print(linha)

#parar ler apenas uma linha arquivo.readline()