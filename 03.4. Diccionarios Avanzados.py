#Creacion de Dirccionarios con Dict
dic = dict(nombre='ernesto', apellido='portillo')
print(dic)

#Las Tuplas pueden actuart como Clave de un diccionario (las listas no)
dic2 = {frozenset(['ernesto','portillo']):'lol'}
print(dic2)

#Crear Diccionaro con Fromkeys (todos los valores seran None)
dic3 = dict.fromkeys(['a','b','c','d'])
print(dic3)

#Usando Fromkeys para darles valores por defecto a las claves
dic4 = dict.fromkeys(['a','b','c','d'],'sepa')
print(dic4)