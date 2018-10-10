#Sets sao listas que nao tem valores duplicados
print(set("My name is Eric and Eric is my name".split()))
print
#Nota-se que o output e uma lista sem palavras repetidas

#Sets sao uma ferramenta poderosa porque permite veridicar dois sets independentes e determinar se existem alguns valores repetidos entre ambos
a = set(["Jake","John","Eric"])
b = set(["John","Jill"])

print(a.intersection(b))
print(b.intersection(a))
print
#O oposto da intersection entre dois sets

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print

#Para determinar quais dos elementos sao exclusivos a uma dos sets
print(a.difference(b))
print(b.difference(a))
print

#Obter uma lista da interseccao de todos os valores sem repetidos
print(a.union(b))
print

