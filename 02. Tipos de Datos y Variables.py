# --- DATOS SIMPLES

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


# --- DATOS COMPUESTOS

# Listas (Array)
lista = ['oscar', 27, True, ]
print(lista)
print(lista[1]) #Si deseamos referirnos a un dato especifico de la lista/array colocamos entre corchetes el indice despues del nombre del arreglo

# Modificacion de un Elemento (Se hace uso del Index para escificar que elemento de la Lista se va Modificar)
lista[0] = 'Ernesto'
print(lista)

# Tuplas (A diferencia de las Listas estas no se puede modificar el contenido posteriormente a la declaracion y asigancion)
tupla = ('oscar', 27, False)
print(tupla)
print(tupla[1]) #Si deseamos referirnos a un dato especifico de la lista/array colocamos entre corchetes el indice despues del nombre del arreglo

# Conjunto (Listas pero sin orden definido no permite buscar elementos por el indice y tampoco acepta datos duplicados)
conjunto = {'ernesto', 27, False}
print(conjunto)

# Diccionario (Objeto en JS)
diccionario = {
    'nombre' : 'Ernesto',
    'edad' : 27,
    'casado' : False
}
print(diccionario)

# Modificacion de un Elemento (Para hacer la Modificacion se debe usar La clave para modificar el valor de dicho elemento)
diccionario['nombre'] = 'Oscar'
print(diccionario)

# VERIFICAR TIPO DE DATOS (Devuelve el Tipo de Dato)
print(type(1))
print(type('Ernesto'))
print(type(False))

