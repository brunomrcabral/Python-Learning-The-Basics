#Listas podem conter qualquer tipo de variaveis e um numero infinito de variaveis
 #Delcarar que e uma lista
mylist = [] 
mylist.append(1)
mylist.append(2)
mylist.append(3)

#Ou entao poderia ser usado desta forma 
#mylist = [1,2,3]

print(mylist[0])
print(mylist[1])
print(mylist[2])
print("---- Break ----")

mylist.append(4)
mylist.append(5)
mylist.append(6)

for x in mylist:
	print(x)

#Outra forma de imprimir seria 
print("\nOutra forma de imprimir os valores que estao dentro da lista")
print(mylist)

#Tentar aceder a um index que nao existe gera um erro obviamente
mylist = [1,2,3]
#print(mylist[10])