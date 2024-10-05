# --- Metodos de Diccionarios

diccionario = {
    'nombre': 'Ernesto',
    'apellido': 'Portillo',
    'edad': 27
}


# Devuelve el Objeto Dict_Item (el cual no sirve para iterar)
claves = diccionario.keys()
print(claves)

# Obetener un Valro del Objeto al especificarle su clave correspondiente
get = diccionario.get('nombre')
print(get)

# Eliminar un Elemento del Diccionario
diccionario.pop('nombre')
print(diccionario)

# Obtener un Elemento dict_item iterable
iterable = diccionario.items()
print(iterable)

# Eliminar todo el Diccionario
diccionario.clear()
print(diccionario)