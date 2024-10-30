# --- METODOS DE CADENAS-------------------------------------------------------------------------------------------------------
cadena1 = 'Hola soy ernesto'


#Cambiar texto a Mayusculas
upper = cadena1.upper()
print(upper)

#Convertir texto a Minusculas
lower = cadena1.lower()
print(lower)

#Convertir la primera letra a Mayusculas de una Cadena
capitalize = cadena1.capitalize()
print(capitalize)

#Busca una Cadena dentro de otra y devuelve el index de donde empieza el trozo de cadena buscado (al exixtir un error devuelve -1)
find = cadena1.find('a')
print(find)

#Buscar una cadena dentro de otra, igual que el anterior pero al no encontrar la busqueda devuleve un error y no imprime '-1'
index = cadena1.index('a')
print(index)

#Si es numerico devuelve True sino False
isnumeric = cadena1.isnumeric()
print(isnumeric)

#Si es alfanumerico devuelve True sino False (Valores de la 'A' la 'Z' sin valorar espacios)
isalpha = cadena1.isalpha()
print(isalpha)

#Buscar una cadena dentro de otra, y devulve la cantidad de  coincidencias encontradas
count = cadena1.count('a')
print(count)

#Devuelve el largo de una cadena
largo = len(cadena1)
print(largo)

#Verificar si una cadena empieza con otra
start = cadena1.startswith('Hola')
print(start)

#Verificar si una cadena termina con otra
end = cadena1.endswith('hola')
print(end)

#Reemplazar un trozo de la cadena por otro
replace = cadena1.replace('Hola', 'Hola soy')
print(replace)

#Separar cadenas con la cadena que le indiquemos y devuleve una lista
split = cadena1.split(' ')
print(split)
print(split[1])

#Hacer Slicing (Sacar una parte de un elemento aun mayor) con una Cadena (los datso entre los corchetes son los parametros desde-hasta donde se va sacar esa parte del string)
cadena = "0123456789"
print(cadena[2:5])

# --- METODOS DE LISTAS-------------------------------------------------------------------------------------------------------

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

# Agregar varios elementos a una lista, se agregaran al final
lista.extend(['Nuevo Elemento Extend 1','Nuevo Elemento Extend 2'])
print(lista)

# Eliminar un elemento especificando el index si se usan numeros negativos empieza a contar el index desde el final
lista.pop(2)
print(lista)

# Eliminar un elemento de la lista por el valor en si
lista.remove('Nuevo Elemento Extend 1')
print(lista)

# Ordenar Elementos de Una Lista de Menor a Mayor
lista2.sort()
print(lista2)

# Ordenar Elementos de Una Lista de Mayor a Menor 
lista2.sort(reverse=True)
print(lista2)

# Invierte el orden de los elementos de una Lista
lista.reverse()
print(lista)

# Eliminar Todos los Elementos de la Lista
lista.clear()
print(list)


# --- METODOS DE TUPLAS -------------------------------------------------------------------------------------------------------

tupla1 = (1,2,4,5,6,7,8,9,10)
tupla2 = ('oscar','ernesto','portillo')

#Busca un elemento dentro de la Tupla y devuelve el index, entre parentesis se coloca el elemento a buscar
index = tupla2.index('portillo')
print(index)

#Contar el numero de veces que aparece un dato especifico dentro de la Tupla
count = tupla1.count(2)
print(count)

# --- METODOS DE DICCIONARIOS -------------------------------------------------------------------------------------------------------

diccionario = {
    'nombre': 'Ernesto',
    'apellido': 'Portillo',
    'edad': 27
}


# Devuelve el Objeto Dict_Item que contiene todas las claves de un Diccionario (el cual nos sirve para iterar)
claves = diccionario.keys()
print(claves)

# Obtener un Valor del Objeto al especificarle su clave correspondiente
get = diccionario.get('nombre')
print(get)

# Eliminar un Elemento del Diccionario
diccionario.pop('nombre')
print(diccionario)

# Obtener un Elemento dict_item iterable cada pareja Clave-Valor funcionara como un elemento dentro de una lista
iterable = diccionario.items()
print(iterable)

# Eliminar todo el Diccionario
diccionario.clear()
print(diccionario)