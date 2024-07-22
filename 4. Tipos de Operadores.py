
#! 1. Operadores Aritméticos
#? Estos operadores se utilizan para realizar operaciones matemáticas.

# Suma (+): Suma dos valores.

# Resta (-): Resta el segundo valor del primero.

# Multiplicación (*): Multiplica dos valores.

# División (/): Divide el primer valor por el segundo.

# División Entera (//): Divide el primer valor por el segundo y devuelve el resultado entero.

# Módulo (%): Devuelve el resto de la división del primer valor por el segundo.

# Exponente (**): Eleva el primer valor a la potencia del segundo.

# Operadores Aritméticos
a = 10
b = 3

print(a + b)  # Salida: 13
print(a - b)  # Salida: 7
print(a * b)  # Salida: 30
print(a / b)  # Salida: 3.3333...
print(a // b) # Salida: 3
print(a % b)  # Salida: 1
print(a ** b) # Salida: 1000

#! 2. Operadores de Comparación
#? Estos operadores comparan dos valores y devuelven un valor booleano (True o False).

# Igual a (==): Verifica si dos valores son iguales.

# Distinto de (!=): Verifica si dos valores son diferentes.

# Mayor que (>): Verifica si el primer valor es mayor que el segundo.

# Menor que (<): Verifica si el primer valor es menor que el segundo.

# Mayor o igual que (>=): Verifica si el primer valor es mayor o igual que el segundo.

# Menor o igual que (<=): Verifica si el primer valor es menor o igual que el segundo.

# Operadores de Comparación
a = 10
b = 3

print(a == b)  # Salida: False
print(a != b)  # Salida: True
print(a > b)   # Salida: True
print(a < b)   # Salida: False
print(a >= b)  # Salida: True
print(a <= b)  # Salida: False

#! 3. Operadores de asignación
#? Estos operadores se utilizan para asignar valores a las variables.

# Asignación (=): Asigna un valor a una variable.

# Suma y asignación (+=): Suma el valor y lo asigna.

# Resta y asignación (-=): Resta el valor y lo asigna.

# Multiplicación y asignación (*=): Multiplica el valor y lo asigna.

# División y asignación (/=): Divide el valor y lo asigna.

# División entera y asignación (//=): Realiza la división entera y lo asigna.

# Módulo y asignación (%=): Calcula el módulo y lo asigna.

# Exponente y asignación (**=): Calcula la potencia y lo asigna.

# Operadores de Asignación
a = 10
a += 5  # a = a + 5
print(a)  # Salida: 15

a -= 3  # a = a - 3
print(a)  # Salida: 12

a *= 2  # a = a * 2
print(a)  # Salida: 24

a /= 4  # a = a / 4
print(a)  # Salida: 6.0

#! Operadores Lógicos
#? Estos operadores se utilizan para combinar expresiones condicionales.

# AND (and): Devuelve True si ambas expresiones son True.

# OR (or): Devuelve True si al menos una de las expresiones es True.

# NOT (not): Invierte el valor de la expresión.

x = True
y = False

print(x and y) # Salida: False
print(x or y)  # Salida: True
print(not x)   # Salida: False