# --- Operadores Aritmeticos
Suma = 1+1
Resta = 1-1
Multiplicacion = 1*1
Division = 1/1 #Devuelve Dato Flotante
Potenciacion = 1**1
Division_Baja = 1//1 #Devuelve Entero Redondeado a la Baja 
Modulo = 1%1 #El restante de una Division no Exacta

print(f'Suma:{Suma} - Resta:{Resta} - Multiplicacion:{Multiplicacion} - Division:{Division} - Potenciacion:{Potenciacion} - Division Baja:{Division_Baja} - Modulo:{Modulo}')

# --- Operadores de Comparacion

"""
== Es Igual Que
!= Es Distinto Que
< Es Mejor Que
<= Es Menor o Igual Que
> Es Mayor Que
>= Es Mayor o Igual Que

"""
# --- Operadores Logicos

#!AND da False si hay una condicion que sea False
r1 = True & True #True
r2 = False & True #False
r3 = True & False #False
r4 = False & False #False

#!OR da True si hay una condicion que sea True
r5 = True | True #True
r6 = False | True #True
r7 = True | False #True
r8 = False | False #False

#!NOT intercambia el Valor Logico ingresado
r9 = not True #False
r10 = not False #True

# --- Operadores de Pertenencia (Si el primer elemento/variable esta contenido o no dentro del segundo elemento/variable)

print( "ola" in "bienvenida" ) #Devuelve true/false si se cumple la condicion
print( "ola" not in "bienvenida" ) #Devuelve true/false si se cumple la condicion

# --- Operadores de Identidad (Si el primer elemento/variable es igual o no al segundo elemento/variable)

print(10 is 10) #Devuelve true/false si se cumple la condicion
print(10 is not 10) #Devuelve true/false si se cumple la condicion