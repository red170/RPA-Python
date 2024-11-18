# Las clases son como "plantillas" o "moldes" que nos permiten crear objetos con características (atributos) y comportamientos (métodos) específicos. Piensa en ellas como una forma de crear tus propios tipos de datos.
# Aquí te muestro un ejemplo simple:
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")
    
    def cumpleanos(self):
        self.edad += 1
# En este ejemplo:

# class Perro: Define una clase llamada "Perro"
# __init__: Es el constructor que se ejecuta cuando creamos un nuevo perro
# self: Se refiere al objeto específico que estamos creando
# Los métodos ladrar() y cumpleanos() son comportamientos que puede realizar cada perro

# Podemos usar esta clase así:
mi_perro = Perro("Max", 3)
mi_perro.ladrar()  # Imprime: Max dice: ¡Guau!
mi_perro.cumpleanos()  # Aumenta la edad en 1
print(mi_perro.edad)  # Imprime: 4

#################################################################################################################

# Los objetos son instancias específicas de una clase - es decir, son como "ejemplares" creados a partir de esa "plantilla" que es la clase. Siguiendo con el ejemplo:
# Creamos diferentes objetos (perros) de la clase Perro
perro1 = Perro("Max", 3)
perro2 = Perro("Luna", 5)
perro3 = Perro("Rocky", 2)

# Cada uno de estos objetos:

# Es independiente de los otros
# Tiene sus propios valores para los atributos (nombre y edad)
# Puede usar todos los métodos definidos en la clase

# Por ejemplo:
# Cada perro tiene su propio nombre y edad
print(perro1.nombre)  # Imprime: Max
print(perro2.nombre)  # Imprime: Luna

# Cada perro puede ladrar
perro1.ladrar()  # Imprime: Max dice: ¡Guau!
perro2.ladrar()  # Imprime: Luna dice: ¡Guau!

# Podemos modificar los atributos de cada perro independientemente
perro1.cumpleanos()  # Solo Max cumple años
print(perro1.edad)   # Ahora es 4
print(perro2.edad)   # Sigue siendo 5
# Es como si la clase fuera el concepto de "perro" en general, y los objetos fueran perros específicos, cada uno con sus propias características pero compartiendo los mismos tipos de comportamientos.
# Algunas características importantes de los objetos:

# Encapsulación: Cada objeto mantiene sus datos (atributos) protegidos
# Estado: Los atributos representan el estado actual del objeto
# Comportamiento: Los métodos definen qué puede hacer el objeto
