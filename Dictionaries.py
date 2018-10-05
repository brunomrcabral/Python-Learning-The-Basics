#Database the nr de telefone
#Dicitonaries data types parecidos com arrays, mas funcionam com key values em vez de arrays 
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

print(phonebook)
print

#Podem ser iterados com o uma lista contudo nao mantem a ordem para iterar os pares tem de ser usada a seguinte sintaxe
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
for name, number in phonebook.items():
	print("Phone number of %s is %d" % (name,number))
print

#Rerirar um valor
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
print

#Ou usando o pop
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)