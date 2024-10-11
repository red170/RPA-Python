with open('./Resources/Test.txt','w', encoding='utf-8') as archivo:
    
    #Sobreescribir el Archivo
    # archivo.write('lololoolooololo')
    
    #Sobreescribir con varias lineas
    archivo.writelines(['hola weon\n',' que tal'])