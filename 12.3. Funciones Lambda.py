# Crear una Funcion
multiplicacion = lambda x : x*2
print(multiplicacion(5))

# Usando Filter forma no Optima
numeros = [1,2,3,4,5,6,7,8]

def par(num):
    if num%2 == 0:
        return True


pares = filter(par,numeros)

print(list(pares))

# Forma Optima con Lambda
numeros_pares = filter(lambda numeros: numeros%2 == 0,numeros)
print(list(numeros_pares))



