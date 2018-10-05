#Funcoes em Python sao definidas usando a keyword def seguido do nome da funcao
def my_function():
	print("Hello From My Function!")

#Funcoes podem tambem ter argumentos
def my_function_with_args(username,greeting):
	print("Hello, %s , From My Function!, I wish you %s" % (username,greeting))

def sum_two_numbers(a, b):
	return a + b

my_function()
my_function_with_args("Bruno","a great year")
x = sum_two_numbers(7,7)	
print(x)

#Exercicio
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()