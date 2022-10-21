# IS727272 - Implementación de singleton con decorador
from __future__ import annotations
from datetime import datetime as time

class Bucket:
    ''' Guarda las clases asociadas con singletons '''
    INSTANCIAS = {}

# 1. Definir la estructura del decorador
def Singleton(clase: object) -> None:
    ''' Función principla del decorador '''
    def obtener_instancia(*args, **kwargs):
        ''' Función interna para crear la primer instancia del singleton '''
        if clase not in Bucket.INSTANCIAS:
            Bucket.INSTANCIAS[clase] = clase(*args, **kwargs)
        return Bucket.INSTANCIAS[clase]
    return obtener_instancia

# 2. Clase que implementará el singleton
@Singleton
class Logger:
    ''' Clase que va a escribir a un archivo '''
    def __init__(self) -> None:
        self.file = open('./logfile.txt', 'a+')
    
    def log(self, message:str) -> None:
        ''' Enviar mensaje al archivo '''
        self.file.write(f'{time.now()}\t{message}\n')

    def __str__(self) -> str:
        ''' Retorna el contenido de logfile.txt '''
        self.file.seek(0)
        return self.file.read()
    
    def __del__(self) -> None:
        ''' Asegurar cierre de archivo '''
        try:
            self.file.close()
            print('Se ha cerrado el logger exitósamente')
        except:
            print('Ha ocurrido un error al intentar cerrar el logger')

# Funcionamiento
if __name__ == '__main__':
    a = Logger()
    a.log('Se realizó una escritura en A')
    print(a)