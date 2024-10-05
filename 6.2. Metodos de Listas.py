# --- Metodos de Listas

lista = ['Hola','Soy','Ernesto',170,17,True,False]
lista2 = [1,2,3,4,5,6,8,4,34,65,87,23,656,4,32]


# Crear una Lista con List (Metodo Extra)
listalist = list(['Hola','Soy','Ernesto',170,True])

# Contar la Cantidad de Elementos de una Lista
length = len(lista)
print(length)

# Agregar un elemento a una Lista (se agregara al Final)
lista.append('Nuevo Elemento Append')
print(lista)

# Agregar un elemento a una Lista, Indicando la posicion
lista.insert(2,'Nuevo Elemento Insert')
print(lista)

# Agregar varios elementos a una lista
lista.extend(['Nuevo Elemento Extend 1','Nuevo Elemento Extend 2'])
print(lista)

# Eliminar un elemento especificando el index si se usan numero snegativos empieza a contar el index desde el final
lista.pop(2)
print(lista)

# Eliminar un elemento de la lista por el valor en si
lista.remove('Nuevo Elemento Extend 1')
print(lista)

# Ordenar Elementos de Una Lista
lista2.sort()
print(lista2)

lista2.sort(reverse=True)
print(lista2)

# Invierte los elementos de una Lista
lista.reverse()
print(lista)

# Eliminar Todos los Elementos de la Lista
lista.clear()
print(list)



# --- Metodos de Tuplas

tupla1 = (1,2,4,5,6,7,8,9,10)

#Busca un elemento dentro de la Tupla y devuelve el index
index = tupla1.index(10)
print(index)

#Contar el numero de veces que aparece un dato especifico dentro de la Tupla
count = tupla1.count(2)
print(count)