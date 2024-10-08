#Encontrar Numero mayor y menor de una lista
list = [1,2,3,4,5,6,7,8]
alto = max(list)
bajo = min(list)
print( "El numero mayor es: ", alto, "\nEl numero menor es: ", bajo)

#Rendondear un Numero Flotante a 'n' cantidad de decimales (la cantidad de decimales se especifica en el numero despues de la coma)
numero = round(12.32588925861258,2)
print( "El numero: ", numero)

#Retorna False si le pasamos cero, false o nada / da True si se le pasa cualquier caracter o valor en True o Numero Natural
resultado_bool = bool(None)
print(resultado_bool)

#Devuelve True si todos los valores son verdaderos o cadenas de texto o Numeros Naturales ( se le debe pasar en formato lista)
resultado_all = all([True, 'oscar', True, 25])
print(resultado_all)

#Suma todos los valores de un Iterable
suma_total = sum(list)
print(suma_total)