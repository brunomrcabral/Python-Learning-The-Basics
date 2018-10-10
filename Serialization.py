#Importar o modulo de json
import json

#Para carregar do JSON para data structure temos de usar 
#json.loads(json_string)


#Dadods em Json sao objetos tem de ser convertidos antes de poderem ser usados
#Json dumps recebe um objeto e devolve uma string
json_string = json.dumps([1,2,3,"a","b","c"])
print(json_string)

#Python tem um data serialization method chamado pickle uma alternativa mais rapida e o cpickle
import pickle
pickle_string = pickle.dumps([1,2,3,"a","b","c"])
print(pickle.loads(pickle_string))