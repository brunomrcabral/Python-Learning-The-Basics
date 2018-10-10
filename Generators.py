import random 

def lottery():
	#Devolve 6 numeros entre 1 e 40
	for i in range(6):
		yield random.randint(1, 40)
		print 
	# O setimo numero gerado e entre 1 e 15
	yield random.randint(1, 15)

x = 0 
for random_number in lottery():
 	++x
	print("O seu numero %d aleatorio e %d !" % (x,random_number))