#Delimitadas com '' ou ""
mystring = 'hello'
print(mystring)
mystring2 = "hello"
print mystring2
if mystring == mystring2:
	print("Sao iguais!")

"""Usar "" permite incluir ' dentro da quote 
se fosse a outra terminaria a quote"""
mystring ="Don't worry about apostrophes"
print(mystring)

one = 1 
two = 2 
three = one + two 
print(three)

hello = "Hello"
world = "World"
helloworld = hello + " " + world
print(helloworld)

#Assigments podem ser feitos a mais do que uma  variavel ao mesmo tempo
a,b = 3, 4
print(a,b)

#Nao e premitido misturar operadores entre ints e strings
one = 1 
two = 2 
hello = "Hello"
#Da erro
#print(one + two + hello)
 
mystring = "hello"
myfloat = 10.0
myint   = 20

String = "String value is ---- "

if mystring == "hello":
    print(String + "%s" % mystring)

if myfloat == 10.0:
    print("Float  value is ---- %s" % myfloat)
if myint == 20.0:
 	print("Int    value is ---- %s" % myint)