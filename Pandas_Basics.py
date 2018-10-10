#Panda e uma ferramenta de alto nivel de manipulacao de data e feito tendo como base o package numpy e a principal estrutura de data e o data frame

#Criar um data frame  usando o pandas
dict = {"Country"	: ["Brazil",   "Russia", "India",     "China", "South Africa"],
		"Capital"	: ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
		"Area"   	: [8.516, 17.10, 3.286, 9.597, 1.221],
		"Population": [200.4, 143.5, 1252, 1457, 52.98]}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
print

#O panda atribui index automaticamente se quisermos usar index nosso podemos usar desta forma 
brics.index= ["BR", "RU", "IN", "CH", "SA"]

print(brics)
print

""" Outra forma de criar data frames e importando ficheiros .csv podem ser importados da seguinte forma

import pandas as pd

cars = pd.read_csv('cars.csv')

print(cars)

"""


""" 
#Existem várias formas de indexar Pandas DataFrame uma das formas mais faceis é usando square bracket notation

import pandas as pd

cars = pd.read_csv('cars.csv',index_col = 0)

#Imprimir uma coluna inteira dando lhe o cabecalho

print(cars['cars_per_cap'])

#Imprimir a coluna inteira como Pandas DatafFrame
print(cars[['cars_per_cap']])

#Imprime um DataFrame com country e cars_per_cap
print(cars[['cars_per_cap','country']])
"""

"""
#Square Brackets tambem podem ser usados para aceder a rows do DataFrames

import pandas as pd 
cars = pd.read_csv('cars.csv',index_col = 0) 

#Imprime as 4 primeiras observacoes
print(cars[0:4])

#Imprime a quinta e sexta observacao
print(cars[4:6])

"""

"""
#Podemos tamber usar o loc e o iloc para fazer qualquer operacao de selecao de data 
loc e baseado em labels o que quer dizer que temos de especificar a row e a colum 
ja o iloc e baseado em index 

import pandas as pd 
cars = pd.read_csv('cars.csv',index_col = 0 ) 

#Imprime a observacao nr dois
print(cars.iloc[2])

#Imprime as row que tem como index AUS e EG
print(cars.loc[['AUS','EG']])

"""

