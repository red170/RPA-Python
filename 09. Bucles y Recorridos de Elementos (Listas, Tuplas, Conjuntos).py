#Un elemento puede ser iterable si tiene algo que marce como se va iterar desde-hasta
# Elementos sobre los que se pueden iterar: Listas, Tuplas, Diccionario, Cadenas de Texto

# --- BUCLE FOR -------------------------------------------------------------------------------------------------------

# --- Listas, Tuplas y Conjuntos

animales = ['perro','gato','tortuga','cocodrilo']
numeros = [23,45,67,89]

#Iterar una Lista (Tomara cada uno de los elementos de Dicha lista y luego hara lo que le Indiquemos)
for animal in animales:
    print(f'la variable animal vale {animal}')  #En este caso Imprimirlo dentro de de un F-String

#Iterar una lista de numeros y operarla (Tomara cada uno de los elementos de Dicha lista y luego hara la operacion que querramos)
for numero in numeros:
    resultado = numero * 2 #Operando el elemento
    print(f'El numero multiplicado es {resultado}') # Imprimiendo el elemento ya operado en un F-String

#Iterar dos o mas Listas a la vez (deben tener la misma cantidad de elementos, y siempre se se seleccionaran por pares de primeros, segundos ... etc)
for numero,animale in zip(numeros,animales):
    print(f'El numero {numero} corresponde a {animale}') # Imprimiendo los Pares

#Iterar usando Range para especificar que tantos elementos debe tomar en listas grandes o si deseamos tomar cierta parte especifica de esa lista 
#(Si son dos parametros estamos determinando desde/hasta si es solo uno estamos definiendo el hasta)
for num in range(1,10):
    print(f'estas imprimiendo el numero {num}')

#Enumerar los Elementos de una Lista (devolvera el indice asignado a cada elemento y el elemento en cuestion)
for num in enumerate(numeros):
    clave = num[0] #se especifica el indice asignado al primer elemento (colocando entre corchetes cero '[0]' lo cual sirve para especificar que se va imprimir el indice de cada iteracion)
    valor = num[1] #se especifica el valor tomado de la lista que sera asignado al indice previamente establecido (colocando entre corchetes uno '[1]' lo cual sirve para especificar que se va imprimir el valor de cada iteracion)
    print(f'el indice {clave} tiene el valor {valor}')

#Usando Else en un For 
#Sirve para imprimir un mensaje cuando termino el recorrido de la Lista
for numero in numeros:
    print(numero)
else:
    print('termino la lista')

#Saltarse un Elemento e Imprimir todo lo demas
for animal in animales: # Inicializacion del recorrido
    if animal == 'gato': # Si en una iteracion el valor coincide con el que especificamos
        continue # Lo omitira ...
    print(animal)
else:
    print('----terminado----')

#Evitar que un bucle se siga ejecutando cuando se cumpla cierta funcion (break impide que se ejecute un else)
for animal in animales:
    if animal == 'gato': # Si en una iteracion el valor coincide con el que especificamos
        break #Se termina el recorrido hasta el elemento anterior del cual coincidio la busqueda
    print(animal)

#Aplicar For para operar una lista de numeros en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

# --- Diccionarios

diccionario = {
    'nombre': 'Ernesto',
    'apellido': 'Portillo',
    'edad': 27
}

#Obtener las claves de de un Diccionario
for key in diccionario: # Recorrer cada uno de los pares Clave/Valor
    print(key) # Imprime solamente la clave

#Obetner las claves y valores de un Diccionario en Formato Tupla
for value in diccionario.items(): # Recorrer cada uno de los pares Clave/Valor
    print(value) # Imprime los pares de Clave/Valor

#Obtener las claves/valores dentro de variables para manejarlas 
# (Se le puede dar un uso similiar al de enumerar las listas/tuplas pero aca en lugar de asiganr en una variable el index y el otro el elemento, aca seri aen una variable la clave y en otra el valor)
for datos in diccionario.items():
    clave = datos[0] #Se guarda en variable la clave agregando el '[0]' despues de la variable del bucle
    valor = datos[1] #Se guarda en variable el valor agregando el '[1]' despues de la variable del bucle
    print(f'{clave}: {valor}') #Se pueden manipular ambas variables dentro de F-String
    
# --- Cadenas de Texto

cadena_de_texto = 'que ondas ernesto'

#Recorrer letra por letra 
# (Imprime letra por letra dicho string)
for letra in cadena_de_texto:
    print(letra)
    
    
# --- BUCLE WHILE -------------------------------------------------------------------------------------------------------
#Mientras que en el Bucle For todo el recorrido depende el contendio de los arreglos de Datos aca el bucle centra su cantidad de iteraciones segun un limitante que nosotros establezcamos dentro de una condicion en el bucle y tendremos una variable que funcionara como contador de iteraciones al contador complir con la condicion especificada se termina la ejecucion del bucle

contador = 0 #Inicializacion del Contador
while contador < 10: #Condicion que indica que mientras se cumpla la condicion se ejecutara el codigo
    contador += 1 #El contador aumentara su valor en cada iteracion
    print(contador) #Codigo a Ejecutar
print("Acabou") #Aviso de FINALIZACION del Bucle


