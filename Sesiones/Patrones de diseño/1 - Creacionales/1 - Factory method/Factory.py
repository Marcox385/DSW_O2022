# IS727272 - Factory Method
# Sesión 12 - 27.09.22

from abc import ABC, abstractmethod
from enum import Enum

# [1] Producto (Interface)
class Bloque(ABC):
    ''' Producto principal del juego '''

    @abstractmethod
    def colocar(self) -> str:
        ''' Retorna el nombre del bloque con una leyenda '''
        pass # Omisible

    def minar(self) -> bool:
        ''' Retorna True si el bloque se minó correctamente '''
        pass # Omisible

# [2] Productos concretos abstractos
class Pasto(Bloque):
    def colocar(self) -> str:
        return 'El bloque de pasto se colocó correctamente'

class Granito(Bloque):
    def colocar(self) -> str:
        return 'El bloque de granito se colocó correctamente'

class Horno(Bloque):
    def colocar(self) -> str:
        return 'El horno se colocó correctamente'

class Piedra(Bloque):
    def colocar(self) -> str:
        return 'La piedra se colocó correctamente'

class CamaPiedra(Bloque):
    def colocar(self) -> str:
        return 'La cama de piedra se colocó correctamente'

class Agua(Bloque):
    def colocar(self) -> str:
        return 'Este es un bloque de agua'

# [3] Clase creadora
class Mundo:
    ''' Clase creadora para el juego '''
    def crear_bloque(self) -> Bloque: # Factory method
        ''' Factory method usado para crear bloques en distintos modos o mundos '''
        pass

    def colocar(self, tipo_bloque:object) -> str:
        ''' Regresa el nombre del bloque con una leyenda '''
        return self.crear_bloque(tipo_bloque).colocar()

    def crear_bloque(self, tipo_bloque:object) -> Bloque: # Factory method
        ''' Factory method usado para crear bloques en distintos modos o mundos '''
        return tipo_bloque.value

# [4] Creadores concretos
class ModoSupervivencia(Mundo):
    class TipoBloque(Enum):
        # name      value
        PASTO   =   Pasto()
        PIEDRA  =   Piedra()
        HORNO   =   Horno()
        AGUA    =   Agua()

class ModoCreativo(Mundo):
    class TipoBloque(Enum):
        # name      value
        PASTO   =   Pasto()
        PIEDRA  =   Piedra()
        GRANITO =   Granito()

# Funcionamiento
if __name__ == '__main__':
    modo = ModoCreativo()

    # Este código está ligado a un botón perteneciente a una librería o framework
    # No puede ser modificado

    # bloque = modo.crear_bloque(modo.TipoBloque.GRANITO)
    # print(bloque.colocar())

    print(modo.colocar(modo.TipoBloque.GRANITO))