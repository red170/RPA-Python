#Creando un Funcion que sume 2 numeros
def suma():
    #Iniciar el Bucle
    while True:
        #Pidiendo los Valores
        a = input('Numero 1: ')
        b = input('Numero 2: ')
        #Intentando convertir los Numeros a Enteros
        try:
            resultado = int(a) + int(b)
        #Si la lanzo una excepcion pide que reingrese los datos
        except:
            print('No te detengas')
        #Terminando el Bucle si todo salio bien
        else:
            break
        #Esto se muestra siempre al terminar la ejecucion y rara vez se usa
        finally:
            print('Terminaste')
    #Mostrar el Resultado
    return resultado

print(suma())