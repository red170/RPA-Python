diccionario = {
    'nombre': 'Ernesto',
    'apellido': 'Portillo',
    'edad': 27
}

#Obtener las claves de de un Diccionario
for key in diccionario:
    print(key)

#Obetner las claves y valores de un Diccionario en Formato Tupla
for value in diccionario.items():
    print(value)

#Obtener las claves/valores dentro de variables para manejarlas
for datos in diccionario.items():
    clave = datos[0]
    valor = datos[1]
    print(f'{clave}: {valor}')

