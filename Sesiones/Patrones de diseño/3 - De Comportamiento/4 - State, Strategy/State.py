# IS727272 - State
# Sesión 26 - 22.11.22
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep

# Context
class Semaforo:
    class TipoSecuencia:
        NORMAL = 'self._estado.secuencia_normal()'
        PRECAUCION = 'self._estado.secuencia_precaucion()'
    
    _estado = None
    
    def __init__(self, estado:Estado, tipo:TipoSecuencia) -> None:
        self.tipo = tipo
        self._estado = estado

    def cambiar_estado(self, estado:Estado) -> None:
        print(f'-I- El semáforo ha cambiado a {type(estado).__name__}')
        self._estado = estado # Nuevo estado
        self._estado.contexto = self # Referencia al estado concreto
        eval(self.tipo)

    def iniciar(self):
        self.cambiar_estado(self._estado)

# Interface de estado
class Estado(ABC):
    @property
    def contexto(self) -> Semaforo:
        return self._contexto

    @contexto.setter
    def contexto(self, contexto: Semaforo) -> None:
        self._contexto = contexto

    @abstractmethod
    def secuencia_normal(self) -> None:
        pass

    @abstractmethod
    def secuencia_precaucion(self) -> None:
        pass

# Estado concreto
class Rojo(Estado):
    def secuencia_normal(self) -> None:
        sleep(2)
        self.contexto.cambiar_estado(Verde())
    
    def secuencia_precaucion(self):
        sleep(1)
        self.contexto.cambiar_estado(Amarillo())

class Amarillo(Estado):
    def secuencia_normal(self) -> None:
        sleep(1)
        self.contexto.cambiar_estado(Rojo())
    
    def secuencia_precaucion(self) -> None:
        sleep(1)
        self.contexto.cambiar_estado(Rojo())

class Verde(Estado):
    def secuencia_normal(self) -> None:
        sleep(2)
        self.contexto.cambiar_estado(Amarillo())

    def secuencia_precaucion(self) -> None:
        # sleep(1)
        # self.contexto.cambiar_estado(Amarillo())
        raise NotImplemented

if __name__ == '__main__':
    # Código cliente

    contexto = Semaforo(Rojo(), Semaforo.TipoSecuencia.PRECAUCION)
    contexto.iniciar()
