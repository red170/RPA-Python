#Creando conjuntos con 'set'
conjunto = set(['dato1','dato2'])

#Meter un conjunto dentro de otro Conjunto
conjunto1 = frozenset(['dato1', 'dato2', 'dato3'])
conjunto2 = {conjunto1,'dato3'}

print(conjunto2)