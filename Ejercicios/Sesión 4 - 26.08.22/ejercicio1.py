# IS727272 - Cordero Hernández, Marco Ricardo
# Videocasetera ; Relación de dependencia

from __future__ import annotations  # Biblioteca auxiliar 

class Videocasetera:
    ''' Clase A '''
    def __init__(self) -> None:
        pass

    # La relación de dependencia se da a través de argumentos los métodos
    def iniciar(self, canal:Canal) -> str:  # Se define relación de dependencia
        ''' Inicia la reproducción de contenido '''
        return f'Iniciando la reproducción... {canal.sintonizar()}'

    def detener(self) -> str:
        ''' Detiene la reproducción de contenido '''
        return 'Deteniendo la reproducción'


class Canal:
    ''' Clase B '''
    def __init__(self, canal:int = 3) -> None:
        self.__canal = canal

    @property
    def canal(self) -> int:
        ''' Propiedad getter de canal '''
        return self.__canal

    @canal.setter
    def canal(self, canal:int) -> None:
        ''' Propiedad setter de canal '''
        self.__canal = canal

    def sintonizar(self) -> str:
        ''' Sintonizando canal '''
        return f'Sintonizando el canal {self.__canal}'


if __name__ == '__main__':
    print(Videocasetera().iniciar(Canal(4)))