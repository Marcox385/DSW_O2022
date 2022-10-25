# IS727272 - Abstract Factory Method práctica
# Sesión 15 - 07.10.22

# Se propone un ejercicio acerca de la creación de muebles
# con distintos estilos (art deco, contemporáneo, barroco, etc.)
# Reto: estilos actuales son moderno y contemporáneo, previniendo
# la adición de un estilo adicional denominado retro

from abc import ABC, abstractmethod
from enum import Enum

# Paso 1: Productos abstractos
class Silla(ABC):
    ''' Clase abstracta para construir una silla '''
    
    @abstractmethod
    def construir(self) -> str:
        ''' Permite construir una silla '''

class Sofa(ABC):
    ''' Clase abstracta para construir un sofá '''

    @abstractmethod
    def ensamblar(self) -> str:
        ''' Permite ensamblar un sofá '''

    @abstractmethod
    def empacar(self) -> str:
        ''' Permite empacar un sofá '''

class Mesa(ABC):
    ''' Clase abstracta para construir mesas '''

    @abstractmethod
    def armar() -> str:
        ''' Permite armar una mesa '''
    
    @abstractmethod
    def embalar() -> str:
        ''' Permite embalar una mesa '''

# Paso 2: Productos concretos abstractos
class SillaModerna(Silla):
  ''' Clase abstracta para definir sillas con estilo moderno '''

  def construir(self) -> str:
    return 'Se armó una silla moderna con todas sus partes'

  def __str__(self) -> str:
    return 'Silla moderna'
  
class MesaModerna(Mesa):
  def __init__(self):
    self.anchura = 12
    self.largo = 8
    self.altura = 3
    self.peso = 0
    self.maxPeso = 101
    print('Mesa Moderna creada...')

  def caerse(self):
    if (self.maxPeso > self.peso):
      print(f'-I- La Mesa Moderna se cayó con un peso de {self.peso} (> {self.maxPeso})')

  def construir(self) -> str:
    return 'Se construyó la mesa moderna'

class SofaModerno(Sofa):
  def ensamblar(self) -> str:
    return 'Se ensamblarán las piezas para crear un sofá moderno'

  def empacar(self) -> str:
    return 'Se empacará el sofá moderno para su transporte'

class SofaContemporaneo(Sofa):
  def ensamblar(self) -> str:
    return 'Se ensamblarán las piezas para crear un sofá contemporáneo'

  def empacar(self) -> str:
    return 'Se empacará el sofá contemporáneo para su transporte'

class SillaContemporanea(Silla):
  ''' Clase para definir sillas contemporaneas de cualquiera '''

  def construir(self) -> str:
    return 'Se armará la silla contemporánea con todas sus partes'

  def __str__(self)-> str:
    return 'Silla contemporánea'

class MesaContemporanea(Mesa):
  def construir(self) -> str:
    return 'Se arma una mesa contemporánea'

  def empacar(self) -> str:
    return 'Se empaca la mesa contemporánea'

# Paso 3: Fäbrica abstracta
class MueblesIteso(ABC):
  @abstractmethod
  def crear_mesa(self) -> str:
    ''' Crea una mesa de algún estilo '''
    pass
		
  @abstractmethod
  def crear_silla(self) -> str:
    ''' Crea una silla de algún estilo '''
    pass
		
  @abstractmethod
  def crear_sofa(self) -> str:
    ''' Crea un sofá de algún estilo '''
    pass

# Paso 4: Fábricas concretas
class Modernos(MueblesIteso):
  def crear_mesa(self) -> Mesa:
    ''' Crea una mesa de algún estilo '''
    return MesaModerna()

  def crear_silla(self) -> Silla:
    ''' Crea una silla de algún estilo'''
    return SillaModerna()

  def crear_sofa(self) -> Sofa:
    ''' Crea un sofa de algún estilo '''
    return SofaModerno()

class Contemporaneos(MueblesIteso):
  def crear_mesa(self) -> Mesa:
    ''' Crea una mesa contemporánea '''
    return MesaContemporanea()
		
  def crear_silla(self) -> Silla:
    ''' Crea una silla contemporánea '''
    return SillaContemporanea()
		
  def crear_sofa(self) -> Sofa:
    ''' Crea un sofá contemporáneo '''
    return SofaContemporaneo()

class Auxiliar:
    class TipoEstilo(Enum):
        # name           value  
        CONTEMPORANEO    = Contemporaneos()
        MODERNO          = Modernos()
    
    @staticmethod 
    def crear(tipo: TipoEstilo) -> MueblesIteso:
        ''' Crea un nuevo estilo de muebles '''
        return tipo.value

# Funcionamiento
if __name__ == '__main__':
	sucursal = Auxiliar.crear(Auxiliar.TipoEstilo.MODERNO)
	print(sucursal.crear_sofa().ensamblar())