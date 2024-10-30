# --- FUNCIONES -------------------------------------------------------------------------------------------------------

# --- Creacion de una Funcion

def saludar(): #Definicion y Nombramiento de una Funcion
    print('que onda neto') #Codigo que ejecutara dicha Funcion
saludar() #Se llama la ejecucion de la Funcion 

# --- Crear Funciones con Parametros
# Los Parametros son Datos que van dentro de parentesis estos son llevados dentro del codigo para operarlos o manipularlos dentro de la funcion

def saludos(nombre): #Al momento de definir la funcion se inicializa una valiable que funcionara para distinguir y almacenar dicho parametro
    print('Hola',nombre) #Dentro de la Funcion se hace uso de dicha variable
saludos('Juan') #El parametro o dato de la variable que ya definimos en la definicion de la funcion la colocamos en los apretesis durante la llamada a ejecucion de la funcion

def saludox(nombre,sexo): #Se pueden definir mas de un parametro en la funcion
    sexo = sexo.lower()
    if sexo == 'hombre':
        print('Hola viejo',nombre)
    else:
        print('hola vieja',nombre)
saludox('Juan','hombre') #Tomar en cuenta que el orden de los valores debe coincidir con el significado de cada parametro segun lo establecimos en la definicion de la funcion

# --- Crear un funcion que retorne Valores (Generador de Contraseña)
# A la hora de manipular un dato que usaremos como parametro hay momentos en que necesitamos que la funcion no termine con la ejecucion de una orden sino que termine coon la devolucion de un valor que despues nosotros le daremos otro uso segun nuestra necesidad en ese caso hacemos uso de 'return' al final de una funcion un ejemplo de esto puede ser  operar dos numeros si nosotros queremos que nos de solamente el valor para luego nosotros seguirlo operando usaremos funciones con devolucion

input = input('Ingresa Un Numero para generar tu Clave') #Solicitamos Un Dato al Usuario y lo almecenamos en uan variable

def contra(num): #El codigo se ejecutara en base al dato que el usuarioo va proporcionar que este caso esta en el parametro 'num'
    char = 'abcdefghijklmnopqrstuvwxyz'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f'{char[c1]}{char[c2]}{char[c3]}{num*2}'
    return contrasena #Devolvera el dato resultado de la ejecucion del Codigo

Pasword = contra(input) #Aca suceden 3 cosas
#1. Todo el proceso anterior se esta almecenando en la Variable 'Pasword'
#2. Al hacer el llamado de la Funcion le estamos pasando como Parametro el Dato que solicitamos previamente en el Input
#3. Toda la ejecucion del coodigo de la funcion termina con el almacenamiento del dato final en 'contrasena' y como al mismo tiempo estamos almacenando en la variable 'pasword' entonces ahora el dato de 'pasword' sera el mismo de 'contrasena'

print(f'tu contraseña es: {Pasword}') #Imprimimos el Resultado Obtenido



# --- FUNCIONES INTEGRADAS -------------------------------------------------------------------------------------------------------

# --- Encontrar Numero mayor y menor de una lista
list = [1,2,3,4,5,6,7,8]

alto = max(list) #Se le pasa como parametro un arreglo de datos y lo almacenamos en variable para obtener el dato mayor
bajo = min(list) #Se le pasa como parametro un arreglo de datos y lo almacenamos en variable para obtener el dato menor

print( "El numero mayor es: ", alto, "\nEl numero menor es: ", bajo)

# --- Rendondear un Numero Flotante a 'n' cantidad de decimales

numero = round(12.32588925861258,2) #Aca se usan dos parametros el primero es el numero a redondear y el segundo especifica la cantidad de decimales
print( "El numero: ", numero)

# --- Retorna False si le pasamos cero, false o nada / da True si se le pasa cualquier caracter o valor en True o Numero Natural

resultado_bool = bool(None)
print(resultado_bool)

# --- Devuelve True si todos los valores son verdaderos o cadenas de texto o Numeros Naturales

resultado_all = all([True, 'oscar', True, 25]) #El parametro se deve pasar en formato lista osea que dentro de los paretesis del parametro la lista de datos debe ir dentro de corchetes
print(resultado_all)

# --- Suma todos los valores de un Iterable

suma_total = sum(list) 
print(suma_total)

# --- OPERADOR ARGS -------------------------------------------------------------------------------------------------------
# A la hora de pasar parametros sabemos que la cantidad de parametros a la hora de inicializar la funcion debe coincidir con la cantidad de variables que definimos en la Funcion pero y si queremos pasar un conjunto de datos para que los opere al mismo tiempo habiendo inicializado una sola variable en la funcion ... Para eso funciona el Operador Args

# --- Realizar una Suma con el operador Args

def suma_total(numeros): #Inicializamos la Funcion con una sola Variable
    return sum([*numeros]) #Dicha Variable dentro del codigo de ejecucion la colocamos entre corchetes y precedida de un '*' (EL CUAL ES EL OPERADOR ARGS) esto le indicara al codigo que operara varios datos y no solamente uno solo

resultado = suma_total([1,2,3,4,5,6,7,8,9,10]) #Llamamos funcion, almacenamos en variable pero a la vez le estamos pasando varios datos (recordar pasarlos en foormato lista, osea dentro de corchetes)
print(resultado)

# --- Realizar el mismo proceso pero usando el Operador como parametro (OPTIMO)

def suma(*numeros2): #Aca haremos uso del operador args pero desde la variable inicializada desde la definicion de la funcion de esta forma no hace falta coloocar los corchetes para indicar que es formarto lista
    return sum(numeros2)

resultado2 = suma(1,2,3,4,5,6,7,8,9,10) #Llamamos funcion, almacenamos en variable pero a la vez le estamos pasando varios datos (ya no es necesario pasarlos en formato lista)
print(resultado2)

# --- FUNCIONES CON PARAMETROS POR DEFECTO -------------------------------------------------------------------------------------------------------

# --- Creando funciuones con valores por defecto
#Esta solemente sirve para establecer valores por defecto dentro de las variables de la inicializacion de la funcion los cuales pueden ser modificados posteriormente a hacer el llamado de la funcion asignando nuevos parametros

def saludo(nombre = 'oscar', apellido = 'portillo', adjetivo = 'capo'):
    return f'hola {nombre} {apellido} {adjetivo}'

print(saludo())
print(saludo('juan', 'pablo'))
print(saludo('juan', 'pablo', 'maestro'))

"""
CABE ACALARAR QUE EL ORDEN EL CUAL PASEMOS LOS PARAMETROS NO IMPORTA SIEMPRE Y CUANDO ESPECIFIQUEMOS COMO SE VAN IMPRIMIR/DEVOLVER SALDRAN DE ESA FORMA Y NO CON EL ORDEN QUE LE MANDAMOS LOS PARAMETROS
"""

# --- FUNCIONES LAMBDA -------------------------------------------------------------------------------------------------------
#Las Funcioones lambda sirven para ejecutar funciones mas simples en estructura y que a la vez carecen de nombre al definirlas idenficandose por el 'lambda' a la hora de definirlas

# --- Estructura
lambda x : x*2 #La funcion se define al poner lambda seguido del parametro (no ira entre parentesis) y despues de los dos puntos el codigo a ejecutar

# --- Uso
multiplicacion = lambda x : x*2 #Podemos almacenar de forma mas facil la funcion completa dentro de una variable
print(multiplicacion(5)) #Luego Dicha variable le colocamos el parametro dentro de parentesis

# Usando Filter forma no Optima
#Veamos el siguiente codigo de una funcion que se encarga de formar un subconjunto solamente con numeros pares
numeros = [1,2,3,4,5,6,7,8] #Conjunto Iterable de datos a manipular

def par(num):
    if num%2 == 0:
        return True #Devuelve true si el numero es par

pares = filter(par,numeros) #Almacenamos en una Variable el resultado de coomparar el obejeto iterable donde al hacer uso de la funcion filter() si un dato del iterable al pasar por la funci devuleve true sera enviado a la variable pares

print(list(pares)) #El resultado se convierte a formato de lista para ser impreso

# Forma Optima con Lambda
numeros_pares = filter(lambda numeros: numeros%2 == 0,numeros)
# Almacenamos el resultado del uso de filter(), primero definimos la varibale luego despues de los dos puntos la comparacion para ver si es par y despues de una coma el objeto que usaremos como parametro, si hay true en la comparacion del numero se almacenara dentro de la variable
print(list(numeros_pares))#El resultado se convierte a formato de lista para ser impreso


