import re

texto = '''hola hermano, que tal estas weon. 1 fin
esta es la segunda linea. 223 - solamente por relleno
y esta es la tercera. 3. - mas relleno aun
y esta es la tercera. 3. - mas relleno aun'''

#Busqueda Simple de String y devuleve la cantidad de Coincidencias
resultado = re.search('hola',texto)
#Busqueda de Todas las Palabras que coincidan con el parametro indicado (Tomar en cuenta que es Case Sentitive)
resultado1 = re.findall('esta',texto)
#Busqueda de Todas las Palabras que coincidan con el parametro indicado (Ignorando el Case Sentitive)
resultado2 = re.findall('HOLA',texto,flags=re.IGNORECASE)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#\d > busca digitos Numericos del 1-9
resultado3 = re.findall(r'\d',texto)

#\D > busca todo menos digitos Numericos del 1-9 (devuleve caracter por caracter)
resultado4 = re.findall(r'\D',texto)

#\w > Busca Caracteres Alfanumericos: a-z, A-Z, 0-9, _(EN PYTHON EL _ ES CONSIDERADO ALFANUMERICO)(devuleve caracter por caracter)
resultado5 = re.findall(r'\w',texto)

#\W > Busca todo menos Caracteres Alfanumericos: a-z, A-Z, 0-9, _(EN PYTHON EL _ ES CONSIDERADO ALFANUMERICO)(devuleve caracter por caracter)
resultado6 = re.findall(r'\W',texto)

#\s > Busca espacios en Blanco o Saltos de Linea
resultado7 = re.findall(r'\s',texto)

#\S > Busca todo menos espacios en Blanco o Saltos de Linea
resultado8 = re.findall(r'\S',texto)

#. > Busca todo menos Saltos de Linea
resultado9 = re.findall(r'.',texto)

#\n > Busca Saltos de Linea
resultado10 = re.findall(r'\n',texto)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#\ > Cancelar los Caracteres Especiales para buscar uno en especifico
resultado11 = re.findall(r'\.',texto)

#^ > Ubicar la busqueda en el comienzo de una Linea (se usa en conjunto de otro parametro por si solo no da resultado deseado)
resultado12 = re.findall(r'^',texto)

#$ > Ubicar la Ubicar la busqueda en el final de una Linea (se usa en conjunto de otro parametro por si solo no da resultado deseado)
resultado12 = re.findall(r'$',texto)

#{n} > Buscar un valor que se repita n cantidad de veces
resultado13 = re.findall(r'\d{3}',texto)

#{n, m} > Buscar un valor que cumpla con un rango de repeticiones
resultado14 = re.findall(r'\d{1,3}',texto)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Buscar un Numero que luego vaya seguido de un punto y despues de un espacio
result1 = re.findall(r'\d\.\s',texto)

#Busqueda en especifico al principio de la linea (Primera Linea de una cadena solamente)
result2 = re.findall(f'^hola',texto)

#Busqueda en especifico al principio de la linea (Toma en cuenta todas las lineas de la cadena)
result3 = re.findall(f'^esta',texto,flags=re.M)

#Busqueda en especifico al final de la linea (Toma en cuenta todas las lineas de la cadena)
result5 = re.findall(f'aun$',texto,flags=re.M)

print(resultado14)