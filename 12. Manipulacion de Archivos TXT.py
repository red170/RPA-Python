# --- APERTURA DE TXT -------------------------------------------------------------------------------------------------------
#Abrir un archivo TXT
archivo = open('./Resources/Test.txt')

#Leer un Archivo TXT
# ar = archivo.read()
# print(ar)

#Leer una Linea  (si se le coloca numeros como parametro dvolvera la cantidad de letras segun el numero indicado)
lineax = archivo.readline()
print(lineax)

#Leer linea por linea (lo devolvera en formato de array)
linea = archivo.readlines()
print(linea)

#Cerrar el Archivo (el archivo se cierra pero la informacion almacenada en variables se mantiene con el archivo cerrado)
archivo.close()

# --- APERTURA OPTIMA -------------------------------------------------------------------------------------------------------

#Abriri el Archivo
with open('./Resources/Test.txt', encoding='utf-8') as archivo:
    
    #Leer el Archivo
    contenido = archivo.read()
    
    #Mostar el Contenido
    print(contenido)

# --- SOBREESCRITURA DE TXT  -------------------------------------------------------------------------------------------------------

with open('./Resources/Test.txt','w', encoding='utf-8') as archivo:
    
    #Sobreescribir el Archivo
    # archivo.write('lololoolooololo')
    
    #Sobreescribir con varias lineas
    archivo.writelines(['hola weon\n',' que tal'])
    
# --- AÑADIDO DE CONTENIDO EN TXT  -------------------------------------------------------------------------------------------------------

with open('./Resources/Test.txt','a', encoding='utf-8') as archivo:
    
    #Agregando el Archivo
    archivo.write('lololoolooololo')
    
    #Agregar Contenido usando un Bucle
    archivo.write('\n')
    for i in range(5):
        archivo.write(f'linea {i+1} agregada\n')