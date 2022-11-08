# IS727272 - Decorator
# Sesión 20 - 01.11.22
from __future__ import annotations
from abc import abstractmethod

class Enmascarado:
    @abstractmethod
    def usar(self) -> str:
        pass

class Link(Enmascarado):
    pass

class Decorator(Enmascarado):
    def __init__(self, mascara: Enmascarado) -> None:
        self._mascara = mascara
    
    @property
    def mascara(self) -> str:
        return self._mascara

class Something:
    ''' Código incompleto, revisar repositorio fuente '''