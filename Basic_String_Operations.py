#Imprimir a posiccao de um dado caracter comeca no 0 obiviamente 
astring = "Hello World!"
print("Posicao do primeiro 'o' --> %d" % astring.index("o") + "\n")

#Contar o numero de caracteres numa dada string
astring = "Hello World!"
print("Numero de 'l'           --> %d" % astring.count("l") + "\n")

#Imprimir apenas parte de uma string, imprime tudo da posicao 3 a 6, imprime do 3 para a "frente", imprime do 7 para "tras", imprime apenas o caracter naquela posicao
astring = "Hello World!"
print(astring[3:7])
print(astring[3:])
print(astring[:7])
print(astring[3])
print

#Imprimir do 2 ao 7 saltando caracteres a cada 2 Formato [start:stop:step]
a = [1,2,3,4,5,6,7,8]
print(a[2:7])
print(a[2:7:2])
print

#Inverter uma string com o metodo falado em cima de slice
astring = "Hello World!"
print(astring[::-1])
print

#Converter  tudo em maisculas ou minusculas
astring = "Hello World!"
print(astring.upper())
print(astring.lower())
print

#Ficar a saber se alguma das substrings se encontra presente na string original
astring = "Hello World!"
print(astring.startswith("Hello"))
print(astring.endswith("Hello"))
print

#Dividir a string num dado caracter tanto a esquerda e direita criando uma lista
astring = "Hello World!"
afewwords = astring.split(" ")
print(afewwords)
print

#Ate ao quinto caracter apos reverter a string 
astring = "Hello World!"
print("Ultimos 5 caracteres sao '%s'" % astring[-5:]) 

