# IS727272 - Cordero Hernández, Marco Ricardo
# Relación de composición

from __future__ import annotations
import random

class Estrella:
    ''' Clase B : Componente '''
    def __init__(self) -> None:
        self.forma = random.choice(['*', '.', '+'])

    def __str__(self) -> str:
        return self.forma

    def __del__(self) -> None:
        print('-I- estrella eliminada')

class Cielo:
    ''' Clase A : Contenedor '''
    def __init__(self, n_estrellas:int) -> None:
        self.estrellas = []     # Se define composición -> asociación

        for _ in range(n_estrellas):
            self.estrellas.append(Estrella())
    
    def mostrar_estrellas(self) -> None:
        for estrella in self.estrellas:
            print(estrella)

if __name__ == '__main__':
    cielo1 = Cielo(5)
    print('-I- Cielo 1')
    cielo1.mostrar_estrellas()
    del cielo1