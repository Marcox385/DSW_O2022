# IS727272 - Adapter
# Sesión 20 - 25.10.22
from __future__ import annotations

# Clase existente del cliente
class Entero:
    ''' Librería del cliente que contiene métodos para el
    manejo de operaciones con números decimales, base 10'''

    @classmethod
    def sumar(cls, *numeros:int) -> int:
        ''' Suma n cantidad de números enteros y retorna
        el valor de la suma'''
        return sum(numeros)

# Otra clase para el cliente
class Binario:
    @classmethod
    def adicion(cls, binario_1:str, binario_2:str) -> str:
        ''' Retorna la suma de dos números binarios representados
        como cadena de caracteres'''
        return '{:b}'.format(int(binario_1, 2) + int(binario_2, 2))

# Adapter
class BinarioToEnteroAdapter(Entero, Binario):
    @classmethod
    def sumar(cls, *numeros:str) -> int:
        ''' Suma n cantidad de números BINARIOS (str) y retorna
        el valor de la suma '''
        suma = '0'
        for numero in numeros:
            suma = cls.adicion(suma, numero)
        return int(suma, 2)

# Funcionamiento
if __name__ == '__main__':
    print(BinarioToEnteroAdapter.sumar('1001', '10', '100', '110110'))