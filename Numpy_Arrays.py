# Numpy Arrays sao parecidos com as listas, sao mais faceis de trabalhar do que listas e permitem fazer operacoes em todo o array

#Neste primeiro exemplo vamos criar duas listas de python e depois vamos importar o numpy package e criar um novo array das listas criadas

height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.16, 88.45]

#importar o numpy
import numpy as np

#Criar 2 numpy arrays a partir da altura e peso 
np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)

print(type(np_height))
print
# Calcular a imc

imc = np_weight / np_height ** 2

print("O seu Indice de Massa Corporal e %s" % imc)
print

# Outra feature do numpy e a abilidade de aplicar um subset se quisermos saber quais valores estao acima de 24 

#Devolve  booleano
print(imc > 24)
print

#Devolve um subset com as observacoes que sao acima de 24 
print(imc[imc > 24])
print

#Exercicio
#Dada uma lista de valores que representao o peso em kg converter os valores para um
# array numpy e depois converter de kg para pound  e no fim imprimir o array
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np_2

np_weight_kg = np_2.array(weight_kg)

weight_pnd = np_weight_kg * 2.2

print(weight_pnd)