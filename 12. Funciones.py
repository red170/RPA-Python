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



