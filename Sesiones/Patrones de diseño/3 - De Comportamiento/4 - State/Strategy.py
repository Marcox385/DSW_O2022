# IS727272 - Strategy
# Sesión 26 - 22.11.22

from __future__ import annotations
from abc import ABC, abstractmethod

# Context
class TerminalBancaria:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def realizar_cargo(self, monto: float) -> None:
        print('Terminal bancaria: Ingrese SuS')
        self._strategy.cobrar(monto)

# Strategy
class Strategy(ABC):
    @abstractmethod
    def cobrar(self, monto: float):
        pass

# Concrete Strategies
class Contado(Strategy):
    def cobrar(self, monto:float) -> None:
        print(f'-I- Cobrando ${monto} pesos en un solo pago')

class Meses(Strategy):
    def cobrar(self, monto:float, meses:int=3) -> None:
        print(f'-I- Cobrando ${monto} pesos a meses. ${round(monto/meses, 2)} cada mes')

class Puntos(Strategy):
    def cobrar(self, monto:float) -> None:
        print(f'-I- Cobrando ${monto} pesos en puntos. {monto*10} gastados')

if __name__ == '__main__':
    print('-I- Terminal BBVA')
    monto = float(input('Monto: $'))
    print('''-I- Opciones de pago:
        1.- Contado
        2.- 3 meses sin intereses
        3.- Puntos BBVA''')

    opcion = int(input('Opción: '))
    match opcion:
        case 1: strategy = Contado()
        case 2: strategy = Meses()
        case 3: strategy = Puntos()
        case _: raise NotImplementedError('Opción no definida')

    TerminalBancaria(strategy).realizar_cargo(monto)