#Creando una Excepcion Perzonalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'Impresionante, Cometiste el siguiente error: {err}')

#Lazando mi Primera Excepcion        
try: 
    raise MiExcepcion('eroooooooooororororororo')
except:
    print('como vas a cometer ese error')