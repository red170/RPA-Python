# Declaración y asignación de variables
x = 5
y = 3.14
nombre = "Alice"
es_activo = True

print(x)         # Salida: 5
print(y)         # Salida: 3.14
print(nombre)    # Salida: Alice
print(es_activo) # Salida: True

# Actualización de variables
contador = 10
print(contador)  # Salida: 10

contador = contador + 1
print(contador)  # Salida: 11

contador += 5
print(contador)  # Salida: 16

# Tipos dinámicos
variable = 10
print(variable)  # Salida: 10

variable = "Ahora soy una cadena"
print(variable)  # Salida: Ahora soy una cadena

variable = 3.14
print(variable)  # Salida: 3.14

# Ejercicio 1
# Solicitar al usuario dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Calcular la suma
suma = numero1 + numero2

# Mostrar el resultado
print(f"La suma de {numero1} y {numero2} es: {suma}")

# Ejercicio 2
# Solicitar al usuario la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")