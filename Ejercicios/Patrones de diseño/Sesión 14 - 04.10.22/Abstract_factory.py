# IS727272 - Abstract Factory Method
from abc import ABC, abstractmethod
from enum import Enum

# [1] Productos (Interfaces)
# Producto A
class Arquero(ABC):
    ''' Clase abstracta para definir arqueros de cualquier civilización '''

    @abstractmethod
    def tirar_flecha(self) -> str:
        ''' Permite al arquero extender el arco y tirar flechas '''

# Producto B
class Aldeano(ABC):
    ''' Clase abstracta para definir aldeanos de cualquier civilización '''

    @abstractmethod
    def recolectar(self) -> str:
        ''' Permite al aldeano recolectar recursos '''

    def construir(self) -> str:
        ''' Permite al aldeano construir objetos '''

    def defender(self) -> str:
        ''' Permite al aldeano defenderse de otras civilizaciones cuando no hay milicia '''

# Producto C
class Milicia(ABC):
    ''' Clase abstracta para definir milicia de cualquier civilización '''
    
    @abstractmethod
    def atacar(self) -> str:
        ''' Permite a la milicia atacar otras civilizaciones '''

# Producto D
class Ariete(ABC):
    ''' Clase abstracta para definir arietes de cualquier civilización '''
    
    @abstractmethod
    def atacar_muro(self) -> str:
        ''' El ariete ataca el muro de una civilización oponente '''


# [2] Productos concretos abstractos
# Producto A1
class ArqueroMaya(Arquero):
    ''' Clase abstracta para definir arquero de cualquier civilización '''
    def __init__(self) -> None:
        self.ataque = 10

    def tirar_flecha(self) -> str:
        return f'El arquero Maya ha disparado una flecha con un ataque de {self.ataque}'

# Producto A2
class ArqueroCelta(Arquero):
    ''' Clase abstracta para definir arquero de cualquier civilización '''
    def __init__(self) -> None:
        self.ataque = 5

    def tirar_flecha(self) -> str:
        return f'El arquero Celta ha disparado una flecha con un ataque de {self.ataque}'

# Producto B1
class AldeanoMaya(Aldeano):
    ''' Clase abstracta para definir aldeanos de cualquier civilización '''

    def recolectar(self) -> str:
        ''' Permite al aldeano recolectar recursos '''
        return f'El aldeano Maya está recolectando recursos en Yucatán'

# Producto B2
class AldeanoCelta(Aldeano):
    ''' Clase abstracta para definir aldeanos de cualquier civilización '''

    def recolectar(self) -> str:
        ''' Permite al aldeano recolectar recursos '''
        return f'El aldeano Maya está recolectando recursos en Irlanda'

# Producto C1
class MiliciaMaya(Milicia):
    ''' Clase abstracta para definir milicia de cualquier civilización '''
    def __init__(self) -> None:
        self.ataque = 15
        self.defensa = 8
    
    def atacar(self) -> str:
        ''' Permite a la milicia atacar otras civilizaciones '''
        return f'La milicia Maya ataca con un daño de {self.ataque}'

# Producto C2
class MiliciaCelta(Milicia):
    ''' Clase abstracta para definir milicia de cualquier civilización '''
    def __init__(self) -> None:
        self.ataque = 11
        self.defensa = 7
    
    def atacar(self) -> str:
        ''' Permite a la milicia atacar otras civilizaciones '''
        return f'La milicia Celta ataca con un daño de {self.ataque}'

# Producto D1
class ArieteMaya(Ariete):
    ''' Clase abstracta para definir arietes de cualquier civilización '''
    def __init__(self) -> None:
        self.ataque = 100
        self.defensa = 80

    def atacar_muro(self) -> str:
        ''' El ariete ataca el muro de una civilización oponente '''
        return f'El ariete Maya ataca el muro causando un daño de {self.ataque}'

# Producto D2
class ArieteCelta(Ariete):
    ''' Clase abstracta para definir arietes de cualquier civilización '''
    def __init__(self) -> None:
        self.ataque = 80
        self.defensa = 40

    def atacar_muro(self) -> str:
        ''' El ariete ataca el muro de una civilización oponente '''
        return f'El ariete Celta ataca el muro causando un daño de {self.ataque}'


# [3] Fábrica abstracta
class Civilizacion(ABC):
    ''' Interface común para todas las civilizaciones '''

    @abstractmethod
    def crear_arquero(self) -> Arquero: # Desacople de código
        ''' Crea un arquero independiente de una civilización '''
        pass

    @abstractmethod
    def crear_aldeano(self) -> Aldeano: # Desacople de código
        ''' Crea un aldeano independiente de una civilización '''
        pass
    @abstractmethod
    def crear_milicia(self) -> Arquero: # Desacople de código
        ''' Crea una milicia independiente de una civilización '''
        pass
    @abstractmethod
    def crear_ariete(self) -> Arquero: # Desacople de código
        ''' Crea un ariete independiente de una civilización '''
        pass

# [4] Fábricas concretas
class Maya(Civilizacion):
    def crear_arquero(self) -> Arquero: # Desacople de código
        ''' Crea un arquero independiente de una civilización '''
        return ArqueroMaya()

    def crear_aldeano(self) -> Aldeano: # Desacople de código
        ''' Crea un aldeano independiente de una civilización '''
        return AldeanoMaya()
    
    def crear_milicia(self) -> Milicia: # Desacople de código
        ''' Crea una milicia independiente de una civilización '''
        return MiliciaMaya()
    
    def crear_ariete(self) -> Ariete: # Desacople de código
        ''' Crea un ariete independiente de una civilización '''
        return ArieteMaya()

class Celta(Civilizacion):
    def crear_arquero(self) -> Arquero: # Desacople de código
        ''' Crea un arquero independiente de una civilización '''
        return ArqueroCelta()

    def crear_aldeano(self) -> Aldeano: # Desacople de código
        ''' Crea un aldeano independiente de una civilización '''
        return AldeanoCelta()
    
    def crear_milicia(self) -> Milicia: # Desacople de código
        ''' Crea una milicia independiente de una civilización '''
        return MiliciaCelta()
    
    def crear_ariete(self) -> Ariete: # Desacople de código
        ''' Crea un ariete independiente de una civilización '''
        return ArieteCelta()

class Aldea:
    class TipoCivilizacion(Enum):
        #name       # value
        MAYA        = Maya()
        CELTA       = Celta()
    
    @staticmethod
    def crear(tipo: TipoCivilizacion) -> None:
        ''' Crea una nueva civilización '''
        return tipo.value

# Funcionamiento
if __name__ == '__main__':
    # Código que posiblemente se modificaría
    civilizacion = Aldea.crear(Aldea.TipoCivilizacion.MAYA)

    # Código que ya no se modifica en versiones posteriores
    print(civilizacion.crear_arquero().tirar_flecha())