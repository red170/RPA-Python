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