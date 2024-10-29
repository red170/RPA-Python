import csv

with open ("./Resources/test.csv") as archivo:
    # print(archivo.read())
    
    #Imprimir con Formato
    reader = csv.reader(archivo)
    for row in reader:
        print(row)