# --- TUPLAS -------------------------------------------------------------------------------------------------------

#Creacion De Tuplas
tupla = ('elemento1', 'elemento2')

#Creacion con 'Tuple'
tupla1 = tuple(['elemento1', 'elemento2'])

#Creacion sin Parentesis
tupla2 = 'dato1', 'dato2',

#Creacion de Tupla de un dato sin parentesis
tupla3 = 'dato1',

# --- CONJUNTOS  -------------------------------------------------------------------------------------------------------

#Creando conjuntos con 'set'
conjunto = set(['dato1','dato2'])

#Meter un conjunto dentro de otro Conjunto
conjunto1 = frozenset(['dato1', 'dato2', 'dato3'])
conjunto2 = {conjunto1,'dato3'}

print(conjunto2)

# --- Teoria de Conjuntos

con1 = {1,3,5,7,9}
con2 = {2,32,51}

#Verificar si un Conjunto es un Subcoinjunto de Otro
res1 = con2.issubset(con1)
res2 = con2 <= con1
print(res2)

#Verificar si un Conjunto es un Superconjunto de otro
res3 = con1.issuperset(con2)
res4 = con1 >= con2
print(res3)

#Verificar si existe al menos un elemento en comun (Aca verifica a la inversa si existe alguna concidencia dara false pero si todos son diferentes dara true)
res5 = con2.isdisjoint(con1)
print(res5)

# --- DICCIONARIOS  -------------------------------------------------------------------------------------------------------

#Creacion de Diccionarios con Dict, Para crear un Diccionario en una sola Linea
dic = dict(nombre='ernesto', apellido='portillo')
print(dic)

#Las Tuplas pueden actuar como Clave de un diccionario (las listas no)
dic2 = {frozenset(['ernesto','portillo']):'lol'}
print(dic2)

#Crear Diccionaro con Fromkeys (todos los valores seran None)
dic3 = dict.fromkeys(['a','b','c','d'])
print(dic3)

#Usando Fromkeys para darles valores por defecto a las claves
dic4 = dict.fromkeys(['a','b','c','d'],'sepa')
print(dic4)