# IS727272 - Cordero Hernández, Marco Ricardo

# Dato: al definir un atributo privado (__attr) dentro de una clase, usualmente
# no se podría acceder a él desde una instancia, sin embargo, en python, esto
# es posible mediante instance_name._ClassName__attr; riesgo potencial

from abc import ABC, abstractmethod

# Interface
class VehiculoGasolina(ABC):
    def poner_gasolina(self, litros:float) -> None:
        ''' Función para cargar combustible a vehículo '''
        if (hasattr(self, 'gasolina')):
            self.gasolina += litros
        else:
            self.gasolina = litros

        return f'Se ha(n) puesto {litros} litro(s) de gasolina'

# Clase abstracta
class TransporteTerrestre(ABC):
    def __init__(self, llantas:int) -> None:
        self.llantas = llantas

    @abstractmethod
    def derrapar() -> str:
        ''' Sonido de derrape '''
        pass  

class Automovil(TransporteTerrestre, VehiculoGasolina):
    __chocado = None

    def __init__(self, chocado:bool = False) -> None:
        super().__init__(llantas=4)
        self.__chocado = chocado
    
    def derrapar() -> str:
        return 'SKREEEEEEEEEE'

class Bicicleta(TransporteTerrestre):
    def __init__(self, diablitos:bool = False) -> None:
        super().__init__(2)
        self.diablitos = diablitos

    def derrapar() -> str:
        return 'BRRRRRRREEEEE'


jetta_2006 = Automovil(chocado=True) # Mi carcachita
benotto = Bicicleta() # Mi otra carcachita

try:
    print(jetta_2006.__chocado)
except AttributeError as e:
    print(f'{e} (at least not publicly)\n'
    f'Valor de atributo: {jetta_2006._Automovil__chocado}')