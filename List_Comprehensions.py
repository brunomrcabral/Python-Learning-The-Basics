# Dada uma frase retirar o elemento the e criar uma lista com o comprimento das palavras restantes
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
print 

word_lengths = []
for word in words:
	if word != "the":
		word_lengths.append(len(word))

print(word_lengths)
print

# Utilizando list coprehension podemos representar o programa de cima da seguinte forma
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)
print

# Basicamente pelo que eu entendi e a seguinte forma 
# Variavel x = [valor a dar seguido de condicao]
# word_lenghts = [len(word) for word in words if word != "the"]

#Exercicio dado uma lista de numeros criar uma lista de numeros positivos apenas e inteiros
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)