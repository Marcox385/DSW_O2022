# IS727272 - Builder
from enum import Enum

# [1] Interfaz constructora
class Estructura:
    ''' Estructura del producto '''

    def __init__(self, descripcion: str) -> None:
        self.__descripcion = descripcion
        self.__partes = []
    
    @property
    def partes(self) -> list:
        ''' Retorna las partes de mi producto '''
        return self.__partes

    def agregar_partes(self, parte: str) -> None:
        ''' Agrega una parte a la lista de partes del producto '''
        self.__partes.append(parte)
    
    def __str__(self) -> str:
        ''' Retorna la descripción del producto '''
        return self.__descripcion

class Honda:
    ''' Clase común para la creación de cualquier producto '''
    def agregar_llantas(self, llantas: int = 2) -> None:
        ''' Agrega llantas al producto '''
        self.estructura.agregar_partes(f'{llantas} llantas')

    def agregar_asientos(self, asientos: int = 1) -> None:
        ''' Agrega llantas al producto '''
        self.estructura.agregar_partes(f'{asientos} asientos')

    def agregar_motor(self, capacidad: str) -> None:
        ''' Agrega motor al producto '''
        self.estructura.agregar_partes(f'Motor {capacidad}')

    def agregar_faros(self, faros: int = 1) -> None:
        ''' Agrega llantas al producto '''
        self.estructura.agregar_partes(f'{faros} faro(s)')

    def contenido(self) -> Estructura:
        return self.estructura

# [3] Productos
class Auto(Estructura):
    ''' Producto 1 '''
    def __init__(self) -> None:
        super().__init__('Automovil')

class SUV(Estructura):
    ''' Producto 2 '''
    def __init__(self) -> None:
        super().__init__('SUV')

class MotoDeportiva(Estructura):
    ''' Producto 3 '''
    def __init__(self) -> None:
        super().__init__('Moto deportiva')

class Cuatrimoto(Estructura):
    ''' Producto 4 '''
    def __init__(self) -> None:
        super().__init__('Cuatrimoto')

# [2] Builder concreto
class HondaAuto(Honda):
    ''' Concrete Builder para los autos Honda '''

    class TipoDeAuto(Enum):
        ''' Estructuras usadas por el builder '''
        # Name        Value
        AUTO        = Auto()
        SUV         = SUV()
    
    def __init__(self, estructura: TipoDeAuto) -> None:
        self.estructura = estructura.value
    
    def agregar_puertas(self, puertas: int = 2) -> None:
        ''' Agrega puertas al producto '''
        self.estructura.agregar_partes(f'{puertas} puertas')
    
    def agregar_sistema_de_audio(self, marca: str) -> None:
        ''' Agrega un sistema de audio al producto '''
        self.estructura.agregar_partes(f'Sistema de audio {marca}')
    
    def agregar_quemacoco(self) -> None:
        ''' Agrega un quemacoco al producto '''
        self.estructura.agregar_partes(f'Quemacocos')

class HondaMoto(Honda):
    ''' Concrete Builder para las motos Honda '''

    class TipoDeAuto(Enum):
        ''' Estructuras usadas por el builder '''
        # Name        Value
        DEPORTIVA     = MotoDeportiva()
        CUATRIMOTO    = Cuatrimoto()
    
    def __init__(self, estructura: TipoDeAuto) -> None:
        self.estructura = estructura.value

# [4] Clase directora
class Directora:
    class Modelos(Enum):
        SUV_ITESO   = 'self.ensamblar_auto_iteso()'
    
    def __init__(self) -> None:
        ''' Asociación de un Builder concreto a la clase directora '''
        self.__producto = None

    @property
    def producto(self) -> Honda:
        ''' Asociación de un Builder concreto a la clase directora '''
        return self.__producto

    @producto.setter
    def producto(self, producto: Honda) -> None:
        ''' Asociación de un Builder concreto a la clase directora '''
        self.__producto = producto
    
    def ensamblar_auto_iteso(self) -> HondaAuto:
        ''' Pasos específicos para ensamblar un auto iteso '''
        auto_iteso = HondaAuto(HondaAuto.TipoDeAuto.SUV)
        auto_iteso.agregar_asientos(7)
        auto_iteso.agregar_faros(4)
        auto_iteso.agregar_llantas(6)
        auto_iteso.agregar_motor('5.1 turbo cargado')
        auto_iteso.agregar_puertas(5)
        auto_iteso.agregar_quemacoco()
        auto_iteso.agregar_sistema_de_audio('Harman Kardon')
        return self.producto.contenido()
        # return auto_iteso

    def iniciar_montaje(self, tipo: Modelos) -> None:
        ''' Inicia el montaje de un nuevo Modelo ya definido en la clase directora '''
        eval(tipo.value)

# Funcionamiento
if __name__ == '__main__':
    directora = Directora()
    directora.producto = HondaAuto(HondaAuto.TipoDeAuto.SUV)
    print(directora.ensamblar_auto_iteso().partes)