#Condicional Simple
edad = 4
if edad == 18:
    print('sos mayor de edad')
else:
    print('no sos mayor de edad')

#Condicional Variado
numero = 0
if numero > 0:
    print('es un numero positivo')
elif numero == 0:
    print('es cero')
else:
    print('es numero negativo')

#Condicional Anidado
salario = 365
departamento = 'san miguel'

if departamento == 'san miguel':
    if salario == 365:
        print('todo correcto')
    else:
        print('solamente cumples una condicion')
else:
    print('no aplicas en ese departamento')
    