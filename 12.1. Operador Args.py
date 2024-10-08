#Realizar una Suma con el operador Args
def suma_total(numeros):
    return sum([*numeros])
resultado = suma_total([1,2,3,4,5,6,7,8,9,10])
print(resultado)

#Realizar el mismo proceso pero usando el Operador como parametro
def suma(*numeros2):
    return sum(numeros2)
resultado2 = suma(1,2,3,4,5,6,7,8,9,10)
print(resultado2)