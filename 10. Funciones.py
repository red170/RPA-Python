# --- FUNCIONES -------------------------------------------------------------------------------------------------------

#Crear la Funcion
def saludar():
    print('que onda neto')
saludar()

#Crear Funciones con Parametros
def saludos(nombre):
    print('Hola',nombre)
saludos('Juan')

def saludox(nombre,sexo):
    sexo = sexo.lower()
    if sexo == 'hombre':
        print('Hola viejo',nombre)
    else:
        print('hola vieja',nombre)
saludox('Juan','hombre')

#Crear un funcion que retorne Valores (Generador de Contraseña)
input = input('Ingresa Un Numero para generar tu Clave')
def contra(num):
    char = 'abcdefghijklmnopqrstuvwxyz'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f'{char[c1]}{char[c2]}{char[c3]}{num*2}'
    return contrasena

Pasword = contra(input)
print(f'tu contraseña es: {Pasword}')



# --- FUNCIONES INTEGRADAS -------------------------------------------------------------------------------------------------------

#Encontrar Numero mayor y menor de una lista
list = [1,2,3,4,5,6,7,8]
alto = max(list)
bajo = min(list)
print( "El numero mayor es: ", alto, "\nEl numero menor es: ", bajo)

#Rendondear un Numero Flotante a 'n' cantidad de decimales (la cantidad de decimales se especifica en el numero despues de la coma)
numero = round(12.32588925861258,2)
print( "El numero: ", numero)

#Retorna False si le pasamos cero, false o nada / da True si se le pasa cualquier caracter o valor en True o Numero Natural
resultado_bool = bool(None)
print(resultado_bool)

#Devuelve True si todos los valores son verdaderos o cadenas de texto o Numeros Naturales ( se le debe pasar en formato lista)
resultado_all = all([True, 'oscar', True, 25])
print(resultado_all)

#Suma todos los valores de un Iterable
suma_total = sum(list)
print(suma_total)

# --- OPERADOR ARGS -------------------------------------------------------------------------------------------------------

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

# --- FUNCIONES CON PARAMETROS POR DEFECTO -------------------------------------------------------------------------------------------------------

#Craendo funciuones con valores por defecto
def saludo(nombre = 'oscar', apellido = 'portillo', adjetivo = 'capo'):
    return f'hola {nombre} {apellido} {adjetivo}'

print(saludo())
print(saludo('juan', 'pablo'))
print(saludo('juan', 'pablo', 'maestro'))

"""
CABE ACALARAR QUE EL ORDEN EL CUAL PASEMOS LOS PARAMETROS NO IMPORTA SIEMPRE Y CUANDO ESPECIFIQUEMOS COMO SE VAN IMPRIMIR/DEVOLVER SALDRAN DE ESA FORMA Y NO CON EL ORDEN QUE LE MANDAMOS LOS PARAMETROS
"""

# --- FUNCIONES LAMBDA -------------------------------------------------------------------------------------------------------

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


