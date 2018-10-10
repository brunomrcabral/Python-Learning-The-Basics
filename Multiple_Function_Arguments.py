#Todas as funcoes em Python recebem um numero fixo de argumentos
#E possivel declarar uma funcao que recebe como arguemnto o numero de argumentos

def foo(first,second,*therest):
	print("First : %s" % first)
	print("Second: %s" % second)
	print("And all the rest.. %s" % list(therest))
	print

foo(1,2,3,4,5)

#Outro exemple de uma funcao que recebe multiplos argumentos
def bar(first, second, third, **options):
	if options.get("action") == "sum":
		print("The sum is %d" %(first+ second + third))

	if options.get("number") == "first":
		return first
	if options.get("number") == "second":
		return second

result = bar(1, 2, 3, action = "sum", number = "second")
print("Result: %d" % result)
print

def foo(a, b, c, *args):
    return len(args)
    
def bar(a, b, c, **kargs):
	print(kargs)
	if kargs["magicnumber"] == 7:
		return True
	else: 
		return False
 
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")
