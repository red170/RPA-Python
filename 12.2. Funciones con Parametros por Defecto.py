#Craendo funciuones con valores por defecto
def saludo(nombre = 'oscar', apellido = 'portillo', adjetivo = 'capo'):
    return f'hola {nombre} {apellido} {adjetivo}'

print(saludo())
print(saludo('juan', 'pablo'))
print(saludo('juan', 'pablo', 'maestro'))

"""
CABE ACALARAR QUE EL ORDEN EL CUAL PASEMOS LOS PARAMETROS NO IMPORTA SIEMPRE Y CUANDO ESPECIFIQUEMOS COMO SE VAN IMPRIMIR/DEVOLVER SALDRAN DE ESA FORMA Y NO CON EL ORDEN QUE LE MANDAMOS LOS PARAMETROS
"""