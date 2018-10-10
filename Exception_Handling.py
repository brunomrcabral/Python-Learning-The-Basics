#O Python usa exceptions para fazer o tratamento de erros
#As vezes quando encontramos erros nao queremos fazer algo por isso para resolver devemos usar um try/except block

def do_stuff(n):
	print(n)

the_list = (1, 2, 3, 4, 5)

for i in range(20):
	try:
		do_stuff(the_list[i])
	except IndexError: #Erro criado quando tentamos aceder a um index que nao existe
		print("Bateu num index que nao existe")
		do_stuff(0)

#Lista de exceptions --> https://docs.python.org/3/library/exceptions.html
#Pode dar jeito      --> https://docs.python.org/3/tutorial/errors.html#handling-exceptions