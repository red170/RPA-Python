#Metodos de Listas

lista = ['Hola','Soy','Ernesto',170,True]

#Crear una Lista con List (Metodo Extra)
listalist = list(['Hola','Soy','Ernesto',170,True])

#Contar la Cantidad de Elementos de una Lista
length = len(lista)
print(length)

#Agregar un elemento a una Lista (se agregara al Final)
lista.append('Nuevo Elemento Append')
print(lista)

#Agregar un elemento a una Lista, Indicando la posicion
lista.insert(2,'Nuevo Elemento Insert')
print(lista)

#Agregar varios elementos a una lista
lista.extend(['Nuevo Elemento Extend 1','Nuevo Elemento Extend 2'])
print(lista)

#Eliminar un elemento especificando el index
lista.pop(2)
print(lista)