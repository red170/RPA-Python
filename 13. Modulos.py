"""
Modulos Nativos
Modulos Third Party
Modulos Propios
"""

#Llamar una Funcion / Importar Modulo
# import zmodulo
# saludo = zmodulo.saludar('ernesto')

#Usando operador As para renombrar localmente ese modulo
# import zmodulo as sal
# saludo = sal.saludar("Oscar")
# print(saludo)

# #Importar una Funcion especifica de un Modulo
# from zmodulo import saludar
# saludo = saludar('oscar')
# print(saludo)

#Importar Variable
# from zmodulo import salu2
# print(salu2)

#Importar una Funcion especifica de un Modulo  que esta dentro de una Carpeta fuera de donde esta el archivo
# import sys
# sys.path.append('ruta_de_la_carpeta_contenedora')
# import nombre_del_modulo

#Importar una Funcion especifica de un Modulo  que esta dentro de una Carpeta
from Modulos.zmodulo import saludar
saludo = saludar('oscar')
print(saludo)

#Importar Variable que esta dentro de una Carpeta
from Modulos.zmodulo import salu2
print(salu2)
