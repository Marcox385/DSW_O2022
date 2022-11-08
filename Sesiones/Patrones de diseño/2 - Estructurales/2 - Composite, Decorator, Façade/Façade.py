# IS727272 - Façade
# Sesión 20 - 01.11.22
from abc import ABC, abstractmethod
from enum import Enum

class Bateria:
    def __init__(self, modelo: str, capacidad: int) -> None:
        self.__modelo = modelo
        self.__capacidad = capacidad
        self.__disponible = False

    def encender(self) -> str:
        self.__disponible = True
        print(f'-I- Bateria {self.__modelo} de {self.__capacidad}Gb está disponible')

class CPU:
    class Estados(Enum):
        ENCENDIDA = 0
        APAGADO   = 1
        BOOT      = 2
    
    def __init__(self, modelo: str) -> None:
        self.__modelo = modelo
        self.__estado = self.Estados.APAGADO
    
    def boot(self) -> None:
        self.__estado = self.Estados.BOOT
        print(f'-I- CPU ')

# Para façade se realizaría un import de todo el código anterior
# y se crearía una clase que contenga todo lo necesario