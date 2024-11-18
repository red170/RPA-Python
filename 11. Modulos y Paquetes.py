# --- MODULOS -------------------------------------------------------------------------------------------------------

"""
Modulos Nativos
Modulos Third Party
Modulos Propios
"""

# --- Llamar una Funcion / Importar Modulo
# import zmodulo # Se coloca 'import' seguido del nombre del Modulo si este se encuentra dentro de la misma ruta 
# saludo = zmodulo.saludar('ernesto') # Despues de almacenarlo en una variable llamamos el modulo seguido del nombre de la funcion que vamos a utilizar separados por un punto y asi podemos hacer uso de codigo de otro archivo

# --- Usando operador As para renombrar localmente ese modulo
# import zmodulo as sal #Funciona excatamente igual que el anterior con la particularidad que aca le asignamos un nombre para manipularlo de mejor forma
# saludo = sal.saludar("Oscar")
# print(saludo)

# --- Importar una Funcion especifica de un Modulo
# from zmodulo import saludar # en los anteriores casos llamamos toda la pagina y poo medio de un punto de por medio indicamos que funcioon deseamos ocupar aca solamente cargaremos una sola funcion especifica
# saludo = saludar('oscar')
# print(saludo)

# --- Importar Variable de un Modulo
# from zmodulo import salu2
# print(salu2)

# --- Importar una Funcion especifica de un Modulo  que esta dentro de una Carpeta fuera de donde esta el archivo
# import sys
# sys.path.append('ruta_de_la_carpeta_contenedora')
# import nombre_del_modulo

# --- Importar una Funcion especifica de un Modulo  que esta dentro de una Carpeta
from Modulos.zmodulo import saludar
saludo = saludar('oscar')
print(saludo)
 
# --- Importar Variable que esta dentro de una Carpeta
from Modulos.zmodulo import salu2
print(salu2)

# --- PAQUETES -------------------------------------------------------------------------------------------------------

#Los Paquetes son un cojunto de Modulos los cuales sirven para almacenar todos los modulos en una carpeta y cargarlos todos de una vez
import Modulos.zmodulo

print(Modulos.zmodulo.salu2)
