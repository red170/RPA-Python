#Un elemento puede ser iterable si tiene algo que marce como se va iterar desde-hasta

# Elementos sobre los que se pueden iterar: Listas, Tuplas, Diccionario, Cadenas de Texto

# --- Bucle FOR
# /// Listas, Tuplas y Conjuntos

animales = ['perro','gato','tortuga','cocodrilo']
numeros = [23,45,67,89]

#Iterar una Lista
for animal in animales:
    print(f'la variable animal vale {animal}')

#Iterar una lista de numeros y operarla
for numero in numeros:
    resultado = numero * 2
    print(f'El numero multiplicado es {resultado}')

#Iterar dos o mas Listas a la vez (deben tener la misma cantidad de elementos)
for numero,animale in zip(numeros,animales):
    print(f'El numero {numero} corresponde a {animale}')

#Iterar usando Range (si son dos parametros estamos determinando desde/hasta si es solo uno estamos definiendo el hasta)
for num in range(1,10):
    print(f'estas imprimiendo el numero {num}')

#Recorrer una Lista (devolvera tuplas)
for num in enumerate(numeros):
    clave = num[0]
    valor = num[1]
    print(f'el indice {clave} tiene el valor {valor}')

#Usando Else en un For
for numero in numeros:
    print(numero)
else:
    print('termino la lista')

#Saltarse un Elemento e Imprimir todo lo demas
for animal in animales:
    if animal == 'gato':
        continue
    print(animal)
else:
    print('----terminado----')

#Evitar que un bucle se siga ejecutando cuando se cumpla cierta funcion (break impide que se ejecute un else)
for animal in animales:
    if animal == 'gato':
        break
    print(animal)

#Aplicar For para operar una lista de numeros en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
