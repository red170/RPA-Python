# --- DATOS SIMPLES  -------------------------------------------------------------------------------------------------------

# Cadenas de Texto Simple
"Hola, Mundo!"
'Hola Mundo!'
# Cadena de  Texto Compuestas
"""
                            Hola
                            Mundo
                            """
'''
                            Hola
                            Mundo
                            '''

# Numero Enteros
10
# Números de punto Flotante (Decimales)
10.5

# Booleanos
True
False

# --- VARIABLES -------------------------------------------------------------------------------------------------------
# Sirven para almacenar Informacion

# Declaracion y Definicion
nombre = 'Oscar Ernesto Portillo'
apellido ='Lopez'
numero = 1

# Modificacion de Variable String
nombre = 'Shulk'

# Modificacion de Variable Numerica
numero += 2 #(El signo previo al igual de la Definicion indica que se le hara al valor original sea suma resta multiplicacion o division con el nuevo operando+)

# Concatenar Strings
nombreCompleto = nombre + apellido

# f-Strings (Template Strings)
saludo = f'hola soy {nombre} y tengo {numero} espada'

# Eliminar una Variable (Toma en cuenta la secuencia de ejecucion si se elimina una variable que despues es incluida o usada en otra variable se elimina la variable orginal pero no el resultado de la otra variable)
del apellido

print(nombre)
print(numero)
print(nombreCompleto)
print(saludo)



# --- DATOS COMPUESTOS -------------------------------------------------------------------------------------------------------

#1. ----- Listas (Array) 
#Las Listas van con Corchetes
lista = ['oscar', 27, True, ] 
print(lista)

#Si deseamos referirnos a un dato especifico de la lista/array colocamos entre corchetes el indice despues del nombre del arreglo
print(lista[1]) 

# Modificacion de un Elemento (Se hace uso del Index para escificar que elemento de la Lista se va Modificar)
lista[0] = 'Ernesto'
print(lista)

#2. ----- Tuplas 
# A diferencia de las Listas estas no se puede modificar el contenido posteriormente a la declaracion y asigancion, Las Tuplas van entre Parentesis
tupla = ('oscar', 27, False)
print(tupla)

#Si deseamos referirnos a un dato especifico de la lista/array colocamos entre corchetes el indice despues del nombre del arreglo
print(tupla[1])

#3. ----- Conjunto 
# Listas pero sin orden definido no permite buscar elementos por el indice y tampoco acepta datos duplicados, Los conjuntos van entre Llaves
conjunto = {'ernesto', 27, False} 
print(conjunto)

#4. ----- Diccionario 
# Conocido como Objeto en JS, se encierran entre llaves con el detalle que aca se especifacn los valores en parejas de Clave-Valor
diccionario = {
    'nombre' : 'Ernesto',
    'edad' : 27,
    'casado' : False
}
print(diccionario)

# Modificacion de un Elemento de un Objeto (Para hacer la Modificacion se debe usar La clave para modificar el valor de dicho elemento)
diccionario['nombre'] = 'Oscar'
print(diccionario)

#*** VERIFICAR TIPO DE DATOS (Devuelve el Tipo de Dato)
print(type(1))
print(type('Ernesto'))
print(type(False))

