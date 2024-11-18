# Los parámetros son los valores que podemos pasar a los métodos para que trabajen con ellos.
class Perro:
    # Constructor con parámetros
    def __init__(self, nombre, edad, raza=""):  # raza es un parámetro opcional con valor por defecto
        self.nombre = nombre  # parámetro obligatorio
        self.edad = edad     # parámetro obligatorio
        self.raza = raza     # parámetro opcional
        self.energia = 100
        
    # Método con un parámetro
    def jugar(self, minutos):
        if self.energia >= minutos:
            print(f"{self.nombre} está jugando por {minutos} minutos")
            self.energia -= minutos
        else:
            print(f"{self.nombre} está muy cansado para jugar")
    
    # Método con múltiples parámetros
    def comer(self, comida, cantidad):
        print(f"{self.nombre} está comiendo {cantidad} de {comida}")
        if comida == "croquetas":
            self.energia += cantidad * 2
        elif comida == "premio":
            self.energia += cantidad
            
    # Método con parámetro por defecto
    def pasear(self, distancia=1):
        print(f"{self.nombre} está paseando {distancia} km")
        self.energia -= distancia * 10
        
    # Método con parámetros opcionales y obligatorios
    def entrenar(self, ejercicio, duracion=10, intensidad="normal"):
        energia_gastada = duracion
        if intensidad == "alta":
            energia_gastada *= 2
            
        print(f"{self.nombre} está haciendo {ejercicio} por {duracion} minutos con intensidad {intensidad}")
        self.energia -= energia_gastada
        
# Veamos cómo usar estos diferentes tipos de parámetros:
# Creando perros con diferentes parámetros
perro1 = Perro("Max", 3)                    # Sin usar el parámetro opcional raza
perro2 = Perro("Luna", 5, "Labrador")       # Usando todos los parámetros

# Usando métodos con diferentes parámetros
perro1.jugar(30)                            # Un solo parámetro
perro1.comer("croquetas", 100)              # Múltiples parámetros

# Usando métodos con parámetros por defecto
perro1.pasear()                             # Usa el valor por defecto (1 km)
perro1.pasear(3)                            # Sobrescribe el valor por defecto

# Usando métodos con parámetros opcionales y obligatorios
perro1.entrenar("sentado")                  # Solo el parámetro obligatorio
perro1.entrenar("saltar", 20)               # Obligatorio + duración
perro1.entrenar("correr", 15, "alta")       # Todos los parámetros
# Tipos de parámetros:

    # Parámetros obligatorios:

        # Deben ser proporcionados siempre
        # No tienen valor por defecto
        # Ejemplo: nombre y edad en el constructor


    # Parámetros opcionales:

        # Tienen un valor por defecto
        # Si no se proporcionan, usan ese valor
        # Ejemplo: raza="" en el constructor


    # Parámetros posicionales:

        # Se pasan en el orden definido
        # Ejemplo: Perro("Max", 3)


    # Parámetros nombrados:

        # Se pueden pasar en cualquier orden especificando su nombre

perro3 = Perro(edad=2, nombre="Rocky", raza="Bulldog")
perro1.entrenar(duracion=20, ejercicio="saltar", intensidad="alta")

    # El parámetro self:

        # Es especial y automático
        # Siempre es el primer parámetro en métodos de instancia
        # No se pasa explícitamente al llamar al método