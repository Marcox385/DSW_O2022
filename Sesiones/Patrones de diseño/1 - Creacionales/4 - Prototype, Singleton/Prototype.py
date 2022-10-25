# IS727272 - Prototype
# Sesión 18 - 18.10.22
from __future__ import annotations
from abc import ABC, abstractmethod
from copy import copy, deepcopy
from random import randint

# [1] Clase abstracta para el prototype
class FiguraAbstracta(ABC):
    ''' Clase abstracta del prototipo '''

    @abstractmethod
    def clonar(self) -> object:
        ''' Shallow copy '''

    @abstractmethod
    def deep(self) -> object:
        ''' Deep copy que incluye a las clases padre y subclases '''

# [2] Clase concreta
class Figura(FiguraAbstracta):
    ''' Clase concreta del prototipo '''

    def __init__(self, pos_x: int = 0, pos_y: int = 0) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.__id = randint(100, 1000)
    
    @property # Getter
    def id(self) -> int:
        ''' Retorna el identificador de la figura '''
        return self.__id
    
    def clonar(self) -> Figura:
        ''' Implementación de un shallow copy '''
        return copy(self)
    
    def deep(self) -> Figura:
        ''' Implementación de un deep copy '''
        return deepcopy(self)

# Subclases
class Rectangulo(Figura):
    ''' Primera subclase del prototipo '''
    def __init__(self, ancho: int = 0, alto: int = 0) -> None:
        super().__init__()
        self.ancho = ancho
        self.alto = alto
    
    def __copy__(self,) -> Rectangulo: # Shallow copy
        ''' Dunder/Magic method que define el comportamiento de la copia o del prototipo '''
        return Rectangulo(self.ancho, self.alto)

    def area(self) -> int:
        ''' Retorna el área del rectángulo '''
        return self.ancho * self.alto
        

# Funcionamiento
if __name__ == '__main__':
    rect_o = Rectangulo(4, 3)
    rect_c = rect_o.clonar()

    print('-' * 75)
    print(f'{"RECTANGULO":^70}')
    print('-' * 75)
    print(f'{"Nivel":^15}{"Atributo":<20}{"Original":^20}{"Copia":^20}')
    print('-' * 75)
    print(f'{"Subclase":^15}{"Ancho":<20}{rect_o.ancho:^20}{rect_c.ancho:^20}')
    print(f'{"Subclase":^15}{"Alto":<20}{rect_o.alto:^20}{rect_c.alto:^20}')
    print(f'{"Padre":^15}{"ID":<20}{rect_o.id:^20}{rect_c.id:^20}')
    print('-' * 75)