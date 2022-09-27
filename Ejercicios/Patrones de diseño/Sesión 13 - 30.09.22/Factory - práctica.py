# IS727272 - Factory Method práctica

# Se propone un ejercicio acerca de pruebas unitarias para microprocesadores
# en donde se deben automatizar las pruebas de estrés, concurrencia, memoria, etc.
# utilizando una interfaz común, sin embargo, no todos los clientas usan las mismas pruebas
# Resolver la problemática utilizando Factory Method

from abc import ABC, abstractmethod
from enum import Enum

# Paso 1: Interface o clase abstracta para los productos
class Producto(ABC):
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
class Prue

# Paso 3: Clase creadora


# Paso 4: Creadores concretos


# Funcionamiento
if __name__ == '__main__':
    pass