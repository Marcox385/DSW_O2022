# IS727272 - Cordero Hernández, Marco Ricardo
# Polimorfismo

from abc import ABC, abstractmethod
from mimetypes import init

# Abstracción
# class Peluche(ABC): # Al ser abstracta, no puede instanciarse
#     def __init__(self) -> None:
#         pass

#     @abstractmethod
#     def hacer_sonido(self) -> str:
#         ''' Retorna el sonido del objeto en particular '''
#         pass

# Polimorfismo
class Peluche(ABC):
    def hacer_sonido(self) -> str:
        ''' Retorna el sonido del objeto en particular '''
        return self.sonido

class Gato(Peluche):
    def __init__(self) -> None:
        self.sonido = 'Meow!'

    def hacer_sonido(self) -> str:
        return 'Meow!'

class Perro(Peluche):
    def __init__(self) -> None:
        self.sonido = 'Woof!'

    def hacer_sonido(self) -> str:
        return 'Woof!'

if __name__ == '__main__':
    tom = Gato()
    luna = Gato()
    benji = Perro()
    costal = [tom, luna, benji]
    
    for peluche in costal:
        print(peluche.hacer_sonido())