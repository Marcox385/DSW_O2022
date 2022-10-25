# IS727272 - Cordero Hernández, Marco Ricardo
# Relación de agregación

from __future__ import annotations

class Superheroe:
    ''' Clase A : Contenedor '''
    def __init__(self, nombre:str, ataque:int, armas:list) -> None:
        self.nombre:str = nombre
        self.ataque:int = ataque
        self.armas:list = armas     # Se define relación de agregación
        self.salud:int = 100

    def atacar(self, oponente:Superheroe) -> str:
        ''' Ataca a un superhéroe oponente '''
        death = f'¡El oponente ya está muerto!'

        if (oponente.salud > 0):
            ataque_final = self.ataque * sum([arma.ataque for arma in self.armas])
            oponente.salud -= ataque_final

            if (oponente.salud <= 0):
                return death

            return f'¡La salud del oponente quedó en {oponente.salud}!'
        
        return death

    def __str__(self) -> str:
        ''' Retorna los detalles del superhéroe '''
        return f'{self.nombre} tiene una saluda de {self.salud}, y estas armas: {[arma.nombre for arma in self.armas]}'

    def __del__(self) -> None:
        print(f'¡{self.nombre} murió!')

class Arma:
    ''' Clase B : Componente '''
    def __init__(self, nombre:str, ataque:int) -> None:
        self.nombre:str = nombre
        self.ataque:int = ataque

    def __str__(self) -> str:
        ''' Retorna el nombre del arma '''
        return self.nombre

if __name__ == '__main__':
    armas_thor = [Arma('Martillo', 6), Arma('Rayo', 10)]
    armas_ojo = [Arma('Arco', 4)]

    thor = Superheroe('Thor', 2, armas_thor)
    ojo_de_halcon = Superheroe('Ojo de Halcón', 1, armas_ojo)

    print(thor.atacar(ojo_de_halcon))

    del thor
    ojo_de_halcon.armas.append(armas_thor)

    print(ojo_de_halcon)
    # No funcionaría, ya que el append anterior modifica la estructura del atributo
    # de la forma [arma, [arma, arma]]