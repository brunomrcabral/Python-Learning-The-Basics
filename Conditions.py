#Devolve Booleano
x = 2 
print(x == 2)
print(x == 3)
print(x > 3)

#Operadores and e or
name = "John"
age  = 23
if name == "John" and age == 23:
	print("Your name is John, and you are also 23 years old")

if name == "John" or name == "Rick":
	print("Your name is either John or Rick")	

#Operador in
name = "John"
if name in ["John","Rick"]:
	print("Your name is on the list")

#If else
x = 2 
if x == 2:
	print("x equals two!")
else:
	print("x does not equal to two")

#Operador is ao contrario do == nao avalia o valor das variaveis em si mas sim o valor das instancias
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

#Operador not se for usado antes de uma expressao booleana invertea 
print(not False)
print( (not False) == ( False))