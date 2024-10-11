#Abriri el Archivo
with open('./Resources/Test.txt', encoding='utf-8') as archivo:
    
    #Leer el Archivo
    contenido = archivo.read()
    
    #Mostar el Contenido
    print(contenido)
    
