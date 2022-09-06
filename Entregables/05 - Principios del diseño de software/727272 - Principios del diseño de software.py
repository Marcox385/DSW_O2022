# Composición sobre la herencia

from abc import ABC
from enum import Enum, unique

''' ------------------------ INTERFACES ------------------------ '''
# IS727272 - Cordero Hernández, Marco Ricardo
class Motor(ABC):
    ''' La implementarán MotorCombustion y MotorElectrico '''
    def mover(self) -> str:
        ''' El transporte comenzará a moverse '''
        pass

class Chofer(ABC):
    ''' La implementarán Robot y Humano '''
    def manejar(self) -> str:
        ''' Se indica quién estaría manejando el transporte '''
        pass
''' ------------------------------------------------------------ '''


''' --------------------- CLASES CONCRETAS --------------------- '''
# IS721210 - Hidalgo Ureña, Miguel Abraham
class MotorCombustion(Motor):
    def __init__(self, cilindros: int, combustible: str, marca: str) -> None:
        self.cilindros = cilindros
        self.combustible = combustible
        self.marca = marca

class MotorElectrico(Motor):
    def __init__(self, voltaje: str) -> None:
        self.voltaje = voltaje

class Robot(Chofer):
    def __init__(self, nombre: str, sistema_operativo: str, marca: str) -> None:
        self.sistema_operativo = sistema_operativo
        self.nombre = nombre
        self.marca = marca

class Humano(Chofer):
    def __init__(self, nombre: str, nacionalidad: str, edad: int) -> None:
        self.nacionalidad = nacionalidad
        self.nombre = nombre
        self.edad = edad
''' ------------------------------------------------------------ '''


''' ------------------------ INTEGRACIÓN ----------------------- '''
# IE726173 - Montes Ramírez, Jose Aurelio
class Transporte:
    @unique
    class Motor_enum(Enum):
        COMBUSTION = 1
        ELECTRICO = 2

    def __init__(self, chofer:list, motor:Motor_enum) -> None:
        self.chofer = chofer
        self.motor = []
        if motor == Transporte.Motor_enum.COMBUSTION:
            self.motor.append(MotorCombustion(10, 'diesel', 'volvo'))
        else:
            self.motor.append(MotorElectrico(120))
    
    def Entregar(self, destino:str, carga:str) -> str:
        ''' Se lleva una carga a un destino'''
        return f'Se llevo {carga} a {destino}'

if __name__ == '__main__':
    robot = [Robot('Robotina', 'Windows', 'Volvo')]

    transporte = Transporte(robot, Transporte.Motor_enum.COMBUSTION)

    print(transporte.Entregar('Muelle', 'cajas'))
''' ------------------------------------------------------------ '''