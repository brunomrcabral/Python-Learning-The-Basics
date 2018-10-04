#Operacoes aritmeticas
number = 1 + 2 * 3 / 4.0
print(number)

#Resto
remainder = 11 % 3 
print(remainder)

#Usar dois sinais de multiplicacao serve para elevar ao quadrado, cubo , etc
squared = 7 ** 2
print("Squared ---> %d" % squared)
cubed   = 2 ** 3
print("Cubed   ---> %d" % cubed)

#Python suporta concatenacao
helloworld ="Hello" + " " + "World" + "." 
print(helloworld)

#Python suporta multiplicar strings 
lotsofhellos = "Hello" * 10
print(lotsofhellos)
#Ou entao no seguinte formato 
lotsofhellos ="Hello"
print(lotsofhellos*10)

#Concatenar listas 
even_numbers = [2,4,6,8,10]
odd_numbers  = [1,3,5,7,9]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#Repeticao tambem resulta com listas
print([1,2,3] * 3)


#Exercicio de trabalhar com listas objetos condicoes if e mais
x = object()
y = object

x_list   = [x] * 10
y_list   = [y] * 10
big_list = x_list + y_list

print("x_list   contains %d object" % len(x_list))
print("y_list   contains %d object" % len(y_list))
print("big_list contains %d object" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
	if big_list.count(x) == 10 and big_list.count(y) == 10: 
		print("Great \n Size of big_list is %d" % len(big_list) + "\nContent of big_list is %s" % big_list)
	else: 
		print("Almost there...")	