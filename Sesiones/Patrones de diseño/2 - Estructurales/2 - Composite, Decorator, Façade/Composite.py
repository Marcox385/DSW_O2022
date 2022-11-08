# IS727272 - Composite
# Sesión 20 - 01.11.22
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange

# Componente
class Elemento(ABC):
    @abstractmethod
    def mostrar(self, indent: int = 0) -> str:
        pass

    @abstractmethod
    def costo(self) -> str:
        pass

# Hoja
class Persona(Elemento):
    COSTO_MIN = 500
    COSTO_MAX = 1000

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._costo = randrange(self.COSTO_MIN, self.COSTO_MAX)
    
    def costo(self) -> int:
        return self._costo
    
    def mostrar(self, indent: int = 0) -> str:
        return ' ' * indent + '- ' + self.nombre + ' $' + str(self.costo())

# Composite
class Departamento(Elemento):
    def __init__(self, nombre: str) -> None:
        self.hijos = []
        self.nombre = nombre
    
    def agregar(self, elemento: Elemento) -> None:
        self.hijos.append(elemento)

    def eliminar(self, elemento: Elemento) -> None:
        self.hijos.remove(elemento)

    def costo(self) -> int:
        costo_total = 0
        for hijo in self.hijos:
            costo_total += hijo.costo()
        return costo_total
    
    def mostrar(self, indent: int = 0) -> str:
        detalle_hijos = ' ' * indent + '+ ' + self.nombre + '\n'
        for hijo in self.hijos:
            detalle_hijos += ' ' * indent + hijo.mostrar(indent + 2)
        return detalle_hijos

if __name__ == '__main__':
    victor = Persona('Victor')
    print('-I- ¿Cuál sería el costo de contratar a Victor?')
    print(victor.mostrar())