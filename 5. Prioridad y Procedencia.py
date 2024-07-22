
#! Prioridad y Precedencia de los Operadores
# La prioridad y precedencia de los operadores determinan el orden en el que se evalúan las expresiones. En Python, los operadores tienen diferentes niveles de precedencia, y los operadores con mayor precedencia se evalúan antes que los operadores con menor precedencia.

# Ejemplo 1
resultado = 3 + 2 * 2
# Multiplicación tiene mayor precedencia que la suma.
# Primero se evalúa 2 * 2 = 4, luego 3 + 4 = 7
print(resultado)  # Salida: 7

# Ejemplo 2
resultado = (3 + 2) * 2
# Los paréntesis tienen mayor precedencia.
# Primero se evalúa 3 + 2 = 5, luego 5 * 2 = 10
print(resultado)  # Salida: 10

#? Lista de precedencia de operadores
# Aquí tienes una tabla resumida de la precedencia de operadores en Python, de mayor a menor precedencia:

#1 Paréntesis: ()

#2 Exponente: **

#3 Negación unaria: -, +

#4 Multiplicación, División, Módulo y División Entera: *, /, %, //

#5 Suma y Resta: +, -

#6 Operadores de Comparación: ==, !=, >, <, >=, <=

#7 Operadores Lógicos: not, and, or