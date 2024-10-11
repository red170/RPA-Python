with open('./Resources/Test.txt','a', encoding='utf-8') as archivo:
    
    #Agregando el Archivo
    archivo.write('lololoolooololo')
    
    #Agregar Contenido usando un Bucle
    archivo.write('\n')
    for i in range(5):
        archivo.write(f'linea {i+1} agregada\n')