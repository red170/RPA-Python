# --- Condicional Simple
edad = 4
if edad == 18: #Se hace la comparacion
    print('sos mayor de edad') #Respuesta si se cumple la Condicion
else:
    print('no sos mayor de edad') #Respuesta si NO se cumple la Condicion

# --- Condicional Variado
numero = 0
if numero > 0: #Se hace la primera comparacion
    print('es un numero positivo') #Respuesta si se cumple la primera Condicion
elif numero == 0: #Se hace la segunda comparacion
    print('es cero') #Respuesta si se cumple la segunda Condicion
else:
    print('es numero negativo') #Respuesta si no se cumple ninguna Condicion

# --- Condicional Anidado
salario = 365
departamento = 'san miguel'

if departamento == 'san miguel': #Se hace la primera comparacion
    if salario == 365: #Se hace la segunda comparacion si se cumple la primera comparacion
        print('todo correcto') #Respuesta si se cumple las dos Condiciones
    else:
        print('solamente cumples una condicion') #Respuesta si se cumple la primera pero no la segunda Condicion
else:
    print('no aplicas en ese departamento') #Respuesta si no se cumple la primera Condicion
    