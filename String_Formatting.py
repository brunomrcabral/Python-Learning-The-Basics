#Variavel com valor atribuido imprimir esse valor junto com uma mensagem
name = "Bruno"
print("Hello, %s!" % name  + "\n")

#Imprimir mais do que um valor junto usando tuplos(parenteses)
name = "Bruno"
age  = 23
print("%s is %d years old." %(name, age) + "\n")

#Qualquer objeto que nao seja uma string tambem pode ser formatado usando o %s operador o resultado final e formatado como uma string
mylist = [1,2,3]
print("A list: %s" % mylist + "\n")

#Exercicio escrever a frase "Hello John Doe. Your current balance is $53.44."

#Forma 1
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " %s %s" % (data[0], data[1]) + ". Your current balance is $%.2f." % data[2] + "\n")

#Forma 2 possivelmete a melhor otimizada das duas 
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)