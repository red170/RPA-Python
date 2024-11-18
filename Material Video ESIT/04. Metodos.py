# Los métodos son funciones que pertenecen a una clase y definen el comportamiento que pueden tener los objetos. Vamos a expandir nuestro ejemplo con más métodos:
class Perro:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.energia = 100
        
    # Métodos de instancia (acceden y modifican atributos del objeto)
    def ladrar(self):
        if self.energia >= 10:
            print(f"{self.nombre} dice: ¡Guau!")
            self.energia -= 10
        else:
            print(f"{self.nombre} está muy cansado para ladrar")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo...")
        self.energia = 100
    
    def jugar(self, minutos):
        if self.energia >= minutos:
            print(f"{self.nombre} está jugando por {minutos} minutos")
            self.energia -= minutos
        else:
            print(f"{self.nombre} está muy cansado para jugar")
    
    # Método que devuelve información
    def obtener_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Energía: {self.energia}"
    
    # Método que modifica atributos
    def cumpleanos(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años")
        
# Podemos usar estos métodos así:
# Creamos un perro
mi_perro = Perro("Max", 3)

# Usamos varios métodos
mi_perro.ladrar()          # Max dice: ¡Guau!
mi_perro.jugar(30)         # Max está jugando por 30 minutos
print(mi_perro.energia)    # Mostrará 60 (100 - 10 del ladrido - 30 del juego)
mi_perro.jugar(70)         # Max está muy cansado para jugar
mi_perro.dormir()          # Max está durmiendo...
print(mi_perro.obtener_info())  # Muestra toda la información del perro

# Características importantes de los métodos:

# Siempre reciben self como primer parámetro

# self se refiere al objeto específico que está llamando al método


# Pueden:

# Modificar atributos del objeto
# Recibir parámetros adicionales
# Devolver valores
# Realizar cálculos
# Mostrar información


# Tipos comunes de métodos:

# Métodos de acceso (getters): obtienen información
# Métodos modificadores (setters): cambian atributos
# Métodos de comportamiento: realizan acciones
# Método constructor (init): inicializa el objeto


# Los métodos pueden llamar a otros métodos usando self:

def dia_en_el_parque(self):
        self.jugar(30)
        self.ladrar()
        self.dormir()