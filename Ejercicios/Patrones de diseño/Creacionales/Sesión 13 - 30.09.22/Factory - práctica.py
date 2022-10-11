# IS727272 - Factory Method práctica

# Se propone un ejercicio acerca de pruebas unitarias para microprocesadores
# en donde se deben automatizar las pruebas de estrés, concurrencia, memoria, etc.
# utilizando una interfaz común, sin embargo, no todos los clientas usan las mismas pruebas
# Resolver la problemática utilizando Factory Method

from abc import ABC, abstractmethod
from enum import Enum

# Paso 1: Interface o clase abstracta para los productos
class Prueba(ABC):
    ''' Producto principal para testing '''

    @abstractmethod
    def ejecutar(self) -> str:
        ''' Ejecuta una prueba y regresa su status '''

    @abstractmethod
    def pausar(self) -> str:
        ''' Pausa la ejecución de la prueba '''

    @abstractmethod
    def detener(self) -> str:
        ''' Detiene completamente la ejecución de la prueba '''

# Paso 2: Productos/Bloques concretos
class PruebaGrafica(Prueba):
    '''Aqui se haran las pruebas de las gráficas'''
    def ejecutar(self) -> str:
      '''Se ejecuta la prueba de gráficas'''
      return f'Ejecutando la prueba de grafica.....'
    def pausar(self)->str:
      '''Pausar la ejecucion de la prueba de gráfica'''
      return f'Se pauso la prueba de gráfica'
    def detener(self)->str:
      '''Detiene la ejecucion de la prueba de gráfica'''
      return f'Se detuvo la prueba de gráfica'
    def __str__(self) ->str:
      return f'Contiene prueba grafica'
      
class PruebaPower(Prueba):
    def ejecutar(self)->str:
      '''se inicia la prueba de power'''
      return 'ejectuando prueba de power'
    def pausar(self)->str:
      '''se pausa la prueba de power'''
      return 'prueba de power pausada'
    def detener(self)->str:
      '''termina la prueba de power'''
      return 'prueba de power detenida'

class PruebaBandwidth(Prueba):
  '''Se ejecutan las pruebas de bandwidth'''
  def ejecutar(self) -> str:
    return 'Ejecutando prueba de bandwidth'
  def pausar(self) -> str:
    return 'Prueba de bandwidth en pausa'
  def detener(self) -> str:
    return 'Prueba de bandwidth detenida'
      
class PruebaIO(Prueba):
    '''Aqui se haran las pruebas de IO'''
    def ejecutar(self) -> str:
      return f'Ejecutando la prueba de IO.....'
    def pausar(self)->str:
      '''Pausar la ejecucion de la prueba de IO'''
      return f'Se pauso la prueba de IO'
    def detener(self)->str:
      '''Detiene la ejecucion de la prueba de IO'''
      return f'Se detuvo la prueba de IO'

class Concurrency(Prueba):
  '''Se evaluara la capacidad del procesador para paralerizar tareas'''
  def ejecutar(self) -> str:
      '''Inicia la prueba de Concurrencia'''
      return 'Ejecutando la prueba de Concurrencia'

  def pausar(self) ->str:
      '''Pausa la prueba de Concurrencia'''
      return f'Pausando la prueba de Concurrencia'
    
  def detener(self)->str:
      '''Detiene la ejecucion de la prueba de Concurrencia'''
      return f'Se detuvo la prueba de Concurrencia'
    
class PruebaStress(Prueba):
  '''Se ejecutan las prubas de estrés'''
  def ejecutar(self) -> str:
    return f'CPU al 100%'
  def pausar(self) -> str:
    return f'Suspendiendo prueba de estres'
  def detener(self) -> str:
    return f'Terminando prueba de estres'

# Paso 3: Clase creadora
class TestingPlatform:
    ''' Plataforma de pruebas para el cliente '''
    def __init__(self) -> None:
        self.currentTest = None
  
    def crear_prueba(self, tipo_prueba:object) -> Prueba:
        ''' Factory method para distintas pruebas '''
        self.currentTest = tipo_prueba.value
        return self.currentTest

    def ejecutar_prueba(self, tipo_prueba:object) -> str:
        ''' Comienza con la ejecución de la prueba especificada '''
        return self.crear_prueba(tipo_prueba).ejecutar()
    
    def pausar_prueba(self, tipo_prueba:object) -> str:
        ''' Pausa la ejecución de la prueba especificada '''
        if self.currentTest != None:
            return self.currentTest.pausar()

    def detener_prueba(self, tipo_prueba:object) -> str:
        ''' Detiene la ejecución de la prueba especificada '''
        if self.currentTest != None:
            return self.currentTest.detener()

# Paso 4: Creadores concretos
class Apple(TestingPlatform):
  class TipoPrueba(Enum):
    GRAFICA_T =         PruebaGrafica()
    BANDWIDTH_T =       PruebaBandwidth()
    IO_T =                PruebaIO()
    CONCURRENCY_T =     Concurrency()
    STRESS_T =          PruebaStress()
    
class Samsung(TestingPlatform):
  class TipoPrueba(Enum):
    IO            = PruebaIO()
    POWER         = PruebaPower()
    CONCURRENCY   = Concurrency()

class Intel(TestingPlatform):
  class TipoPrueba(Enum):
    #Name            #Value
    IO_TEST          = PruebaIO()
    POWER_TEST       = PruebaPower()
    GRAPHIC_TEST     = PruebaGrafica()
    BANDWIDTH_TEST   = PruebaBandwidth()
    CONCURRENCY_TEST = Concurrency()
    STRESS_TEST      = PruebaStress()

class NVIDIA(TestingPlatform):
  class TipoPrueba(Enum):
    # name        value
    GRAFICA_T        = PruebaGrafica()
    POWER            = PruebaPower()
    STRESS_T         = PruebaStress()

# Funcionamiento
if __name__ == '__main__':
    empresa = Apple()
    print(empresa.crear_prueba(empresa.TipoPrueba.GRAFICA_T))