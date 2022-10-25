# IS727272 - Cordero Hernández, Marco Ricardo
# Relación de asociación

from __future__ import annotations


class Estudiante:
    ''' Clase A '''

    def __init__(self, nombre: str, escuela: Escuela) -> None:
        self.__nombre = nombre
        self.__escuela = escuela    # Se define relación de asociación por medio de atributo

    @property
    def nombre(self) -> str:
        # return self.__nombre
        return f'--{self.__nombre}--'

    def __str__(self) -> str:   # Dunder | Magic method
        ''' Retorna la representación del objeto Estudiante '''
        return f'{self.nombre} estudia en {self.__escuela}'


class Escuela:
    ''' Clase B '''

    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    def __str__(self) -> str:
        ''' Retorna la representación del objeto Escuela '''
        return self.nombre


if __name__ == '__main__':
    escuela = Escuela('ITESO')
    paco = Estudiante('Francisco', escuela)
    print(paco)
