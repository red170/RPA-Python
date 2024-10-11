#Abrir un archivo TXT
archivo = open('./Resources/Test.txt')

#Leer un Archivo TXT
# ar = archivo.read()
# print(ar)

#Leer linea por linea (lo devolvera en formato de array)
linea = archivo.readlines()
print(linea)

#Leer una Linea  (si se le coloca numeros como parametro dvolvera la cantidad de letras segun el numero indicado)
lineax = archivo.readline()
print(lineax)

#Cerrar el Archivo (el archivo se cierra pero la informacion almacenada en variables se mantiene con el archivo cerrado)
archivo.close()