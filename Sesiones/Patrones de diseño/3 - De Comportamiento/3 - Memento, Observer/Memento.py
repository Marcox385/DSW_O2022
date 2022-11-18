# IS727272 - Memento
# Sesión 25 - 18.11.22
from __future__ import annotations

# Clase originadora
class CuentaBanco:
    def __init__(self, balance:float = 0):
        self._balance = balance # Este es el estado que se quiere preservar

    def depositar(self, origen:str, cantidad:float): # Se guarda el estado en un objeto Memento
        self._balance += cantidad
        print(f'-I- Cliente {origen} ha depositado ${cantidad} pesos en la cuenta. \tBalance: ${self._balance}')
        return Memento(origen, self._balance)

    def restaurar(self, memento): # Restauramos el estado desde un memento
        self._balance = memento.obtener_estado()
        origen = memento.obtener_origen()
        print(f'-I- Se ha cancelado la ultima transaccion. Último cliente {origen}. Balance: ${self._balance}')

    def __str__(self):
        return f'Balance = {self._balance}'

# Memento
class Memento:
    def __init__(self, origen:str, balance:int):
        self._origen = origen
        self._balance = balance
    
    def obtener_origen(self):
        return self._origen
    
    def obtener_estado(self):
        return self._balance

# Clase cuidadora
class TiendaVirtual:
    def __init__(self, cuenta:CuentaBanco):
        self._cuenta = cuenta # Cuenta de banco del negocio
        self._historial = []  # Lista de mementos
    
    def cobrar(self, cliente:str, cantidad:int): # Un cliente necesita pagar un producto
        memento = self._cuenta.depositar(cliente, cantidad)
        self._historial.append(memento)
    
    def cancelar(self):
        if (not len(self._historial)): return
        self._historial.pop()
        memento = self._historial[-1]
        self._cuenta.restaurar(memento)

if __name__ == '__main__':

    cuenta_bbva = CuentaBanco()
    tienda = TiendaVirtual(cuenta_bbva)
    tienda.cobrar('Pedro', 220.99)
    tienda.cobrar('Gaby', 122.14)
    tienda.cobrar('Andrea', 198.00)
    tienda.cancelar()