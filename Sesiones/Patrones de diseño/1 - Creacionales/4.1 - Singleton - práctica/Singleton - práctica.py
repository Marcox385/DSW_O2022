# IS727272 - Singleton práctica
# Sesión 19 - 21.10.22
from __future__ import annotations
from datetime import datetime as time

class Logger:
    ''' Clase Singleton '''
    _INSTANCIA:Logger = None

    def __init__(self) -> None:
        if Logger._INSTANCIA == None:
            self.file = open('./logfile.txt', 'a+')
            Logger._INSTANCIA = self
    
    def log(self, message:str) -> None:
        ''' Enviar mensaje al archivo '''
        Logger._INSTANCIA.file.write(f'{time.now()}\t{message}\n')
    
    def __str__(self) -> str:
        ''' Retorna el contenido de logfile.txt '''
        Logger._INSTANCIA.file.seek(0)
        return Logger._INSTANCIA.file.read()

    def __del__(self) -> None:
        ''' Asegurar cierre de archivo '''
        Logger._INSTANCIA.file.close()

# Funcionamiento
if __name__ == '__main__':
    a = Logger()
    a.log('Escribiendo desde A')
    b = Logger()
    b.log('Escribiendo desde B')
    c = Logger()
    c.log('Escribiendo desde C')

    print(a)