# IS727272 - Cordero Hernández, Marco Ricardo
# Interface

from __future__ import annotations
from abc import ABC

class Dragon:
    def __init__(self, nombre:str) -> None:
        ''' Inicializa un nuevo dragón '''
        self.nombre:str = nombre
        self.__energia:int = 100

    @property   # GETTER
    def energia(self) -> int:
        ''' Retorna la energía del dragón '''
        return self.__energia

    def alimentar(self, alimento:Alimento) -> None:
        ''' Alimenta al dragón y aumenta su energía '''
        self.__energia += alimento.obtener_energia()


# Interface
class Alimento(ABC):
    def obtener_energia(self) -> int:
        ''' Retorna la energía de alimentación '''
        return self.energia


class Ninio(Alimento):
    def __init__(self) -> None:
        ''' Inicializa un nuevo niño '''
        self.__energia = 30
    
    @property
    def energia(self) -> int:
        ''' Retorna el valor energético del niño '''
        return self.__energia


class Enano(Alimento):
    def __init__(self) -> None:
        ''' Inicializa un nuevo enano '''
        self.__energia = 30
    
    @property
    def energia(self) -> int:
        ''' Retorna el valor energético del enano '''
        return self.__energia

if __name__ == '__main__':
    dragon = Dragon('Smug')
    print(f'Energía inicial: {dragon.energia}')
    dragon.alimentar(Ninio())   # REFACTORIZACIÓN
    dragon.alimentar(Enano())   # REFACTORIZACIÓN
    print(f'Energía final: {dragon.energia}')