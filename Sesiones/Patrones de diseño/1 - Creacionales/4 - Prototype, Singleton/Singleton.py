# IS727272 - Singleton
# Sesión 18 - 18.10.22
from __future__ import annotations

class Sesion:
    ''' Clase del singleton '''
    _INSTANCIA:Sesion = None

    def __init__(self, usuario:str) -> None:
        if (Sesion._INSTANCIA == None):
            self.usuario = usuario
            Sesion._INSTANCIA = self # Implementación del singleton
        else:
            print(f'El usuario {Sesion._INSTANCIA.usuario} está loggeado y no es posible hacer login con el usuario')

    def logout(self) -> None:
        ''' Eliminar al usuario del singleton '''
        Sesion._INSTANCIA = None

# Funcionamiento
if __name__ == '__main__':
    s1 = Sesion('Hugo')
    s1.logout()
    s2 = Sesion('Paco')
    s3 = Sesion('Luis')