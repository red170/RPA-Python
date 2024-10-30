# --- DESEMPAQUETADO -------------------------------------------------------------------------------------------------------

# Sirve para extraer los datos de un arreglo y ubicarlos en variables idependientes funciona tanto para listas como  para tuplas

# Se decalaran la cantidad de variables necesarias segun la cantidad de elementos dentro de la lista/tupla a desempaquetar y luego a esas variables se les asigna como valor la lista/tupla y automaticamente segun el orden que las hayamos colocados asi se asiganran los valores dentro de las variables nuevas

datos = ('Neto', 'Portillo')
nombre,apellidos = datos

print(nombre)
print(apellidos)


