# IS727272 - Cordero Hernández, Marco Ricardo
# Nota: método __repr__ para la representación de la clase, usualmente construída para replicar el objeto

from __future__ import annotations
from typing import List  # Para hints relacionados a arrays


class Propietario:
    ''' Clase contenedora (Propietario <>-> Pizzeria)\n
    La existencia de las pizzerías usualmente no dependen de su propietario '''

    def __init__(self, nombre: str = 'Fulanito', apellido: str = 'de Tal', gender: bool = False, is_male: bool = True) -> None:
        ''' Crea propietari@ de sucursal '''
        self.nombre = nombre
        self.apellido = apellido

        # Sin causar polémica, estrictamente visto como ejercicio
        self.__gender = gender
        self.is_male = is_male

    @property
    def gender(self) -> str:
        ''' Propiedad getter de género '''
        return self.__gender

    @gender.setter
    def gender(self, gender: bool) -> None:
        ''' Propiedad setter de género '''
        self.__gender = gender

    def __str__(self) -> str:
        prefix: str = ""

        if (not self.gender):
            prefix = "Sr. " if self.is_male else "Sra. "

        return f'{prefix}{self.nombre} {self.apellido}'


class Pizzeria:
    ''' Clase componente (Propietario <-<> Pizzeria) y contenedora (Pizzeria ++-> Pizza)\n
    La preparación de las pizzas usualmente depende de la sucursal '''

    def __init__(self, nombre: str, direccion: str, propietario: Propietario) -> None:
        ''' Crea una instancia/sucursal con calificación media (máx. 5) '''
        self.NOMBRE: str = nombre
        self.DIRECCION: str = direccion
        self.calificacion: float = 2.5
        self.__propietario: Propietario = propietario
        self.pizzas = []

    @property
    def nombre(self) -> str:
        ''' Retorna el nombre de la sucursal '''
        return f'Pizzería "{self.NOMBRE}"'

    @property
    def direccion(self) -> str:
        ''' Retorna la ubicación de la pizzería '''
        return f'Ubicada en {self.DIRECCION}'

    @property
    def propietario(self) -> str:
        ''' Propiedad getter de propietario '''
        return str(self.__propietario)

    @propietario.setter
    def propietario(self, propietario: Propietario) -> None:
        ''' Propiedad setter de propietario '''
        self.__propietario: str = propietario

    def __str__(self) -> str:
        ''' Información general de la pizzería '''
        return f'{self.nombre} ubicada en {self.DIRECCION}, perteneciente a {self.__propietario}'


class Ingrediente:
    ''' Clase componente '''
    def __init__(self, nombre:str) -> None:
        ''' Crea un nuevo ingrediente '''
        self.nombre = nombre
    
    @property
    def nombre(self) -> str:
        ''' Propiedad getter del nombre '''
        return self.nombre.capitalize()


class Pizza:
    ''' Clase componente (Pizza <-++ Pizzera) y contenedora (Pizza <>-> Ingrediente) '''
    def __init__(self, nombre: str, ingredientes: List[Ingrediente]) -> None:
        ''' Crea una nueva pizza (omitir la palabra "pizza" en instancia) '''
        self.nombre = nombre
        self.ingredientes = ingredientes
    
    def __str__(self) -> str:
        return f'Pizza {self.nombre}\nContiene'


if __name__ == '__main__':
    yo_merengues = Propietario('Marco', 'Cordero')  # Mal nombre de variable
    petra = Pizzeria("Petra Pizzas a la leña",
                     "Av Rafael Sanzio 522", yo_merengues)
    print(f'Información general de sucursal\n└──{petra}')
