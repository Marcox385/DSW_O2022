# IS727272 - Cordero Hernández, Marco Ricardo
# Encapsulamiento a nivel del método

from __future__ import annotations
from enum import Enum, unique

class Producto:
    def __init__(self, nombre:str, precio:float) -> None:
        ''' Inicializa un nuevo producto '''
        self.nombre:str = nombre
        self.precio:float = precio


class Orden:
    # Encapsulamiento
    @unique # Se usa para asegurar valores únicos (sería un error en este caso)
    class Pais(Enum):
        MEXICO = 0.20
        USA    = 0.07
        CHINA  = 0.14

    def __init__(self, productos:list[Producto]) -> None:
        ''' Inicializa una nueva orden '''
        self.productos:list[Producto] = productos

    def agregar_productos(self, productos:list[Producto]) -> None:
        ''' Agrega una lista de productos a la orden '''
        self.productos + productos

    def total_orden(self, pais:Orden.Pais) -> float:
        ''' Retorna el total calculado de la orden (con impuestos incluídos)\n
        MX = 0.20
        US = 0.07'''

        return sum([product.precio for product in self.productos]) * (pais.value + 1)


if __name__ == '__main__':
    carrito = [Producto('reloj', 5800), Producto('pantalón', 680)]
    tienda = Orden(carrito)
    print(f'Total de orden: ${tienda.total_orden(Orden.Pais.MEXICO)}')