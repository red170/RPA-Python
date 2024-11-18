"""
Una variable es como un contenedor en el que guardamos información dentro de un programa. Imagina que tienes cajas en tu habitación, cada una con un nombre diferente (por ejemplo, "caja de juguetes", "caja de ropa"). En programación, las variables son como esas cajas, pero en lugar de juguetes o ropa, guardan datos como números, texto, valores verdaderos o falsos, etc.

¿Para qué sirven las variables?

    - Almacenar datos: Puedes guardar cualquier tipo de dato que necesites en una variable para usarlo más tarde.
    
    - Realizar cálculos: Puedes hacer operaciones matemáticas con los valores almacenados en las variables.
    
    - Tomar decisiones: Puedes comparar los valores de las variables y ejecutar diferentes partes del código dependiendo del resultado.
    
    - Crear estructuras de datos: Las variables son los bloques básicos para construir estructuras de datos más complejas, como listas y diccionarios.
"""

# Declaracion y Definicion
nombre = 'Oscar Ernesto Portillo'
apellido ='Lopez'
numero = 1

# Modificacion de Variable String
nombre = 'Shulk'

# Modificacion de Variable Numerica
numero += 2 #(El signo previo al igual de la Definicion indica que se le hara al valor original sea suma resta multiplicacion o division con el nuevo operando+)

# Concatenar Strings
nombreCompleto = nombre + apellido

# f-Strings (Template Strings)
saludo = f'hola soy {nombre} y tengo {numero} espada'

# Eliminar una Variable (Toma en cuenta la secuencia de ejecucion si se elimina una variable que despues es incluida o usada en otra variable se elimina la variable orginal pero no el resultado de la otra variable)
del apellido

print(nombre)
print(numero)
print(nombreCompleto)
print(saludo)