# --- Metodos de Cadenas

cadena1 = 'Hola soy ernesto'


#Cambiar texto a Mayusculas
upper = cadena1.upper()
print(upper)

#Convertir texto a Minusculas
lower = cadena1.lower()
print(lower)

#Convertir la primera letra a Mayusculas
capitalize = cadena1.capitalize()
print(capitalize)

#Buscar una Cadena dentro de otra y devuelve el index de donde empieza el trozo de cadena buscado (al exixtir un error devuelve -1)
find = cadena1.find('a')
print(find)

#Buscar una cadena dentro de otra, igual que el anterior pero al no encontrar la busqueda devuleve un error y no imprime '-1'
index = cadena1.index('a')
print(index)

#Si es numerico devuelve True sino False
isnumeric = cadena1.isnumeric()
print(isnumeric)

#Si es alfanumerico devuelve True sino False (Valores de la 'A' la 'Z' sin valorar espacios)
isalpha = cadena1.isalpha()
print(isalpha)

#Buscar una cadena dentro de otra, y devulve la cantidad de  coincidencias encontradas
count = cadena1.count('a')
print(count)

#Devuelve el largo de una cadena
largo = len(cadena1)
print(largo)

#Verificar si una cadena empieza con otra
start = cadena1.startswith('Hola')
print(start)

#Verificar si una cadena termina con otra
end = cadena1.endswith('hola')
print(end)

#Reemplazar un trozo de la cadena por otro
replace = cadena1.replace('Hola', 'Hola soy')
print(replace)

#Separar cadenas con la cadena que le indiquemos y devuleve una lista
split = cadena1.split(' ')
print(split)
print(split[1])

#Hacer Slicing con unas Cadena (los datso entre los corchetes son los parametros desde-hasta donde se va sacar esa parte del string)
cadena = "0123456789"
print(cadena[2:5])