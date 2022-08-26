# IS727272 - Cordero Hernández, Marco Ricardo

from abc import ABC # Para indicar interfaces : class Class(ABC)

class TransporteAereo(ABC):
    def volar(self) -> str:
        return 'El transporte aéreo está volando'

class Avion(TransporteAereo):
    ''' Esta clase permite reservar boletos de avión '''
    def volar(self) -> str:
        ''' Retorna un mensaje cuando el avión está volando '''
        return f'{super().volar()}: avión'

