# IS727272 - Cordero Hernández, Marco Ricardo
# Nota: método __repr__ para la representación de la clase, usualmente construída para replicar el objeto

from __future__ import annotations

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
        prefix: str = ''

        if (not self.gender):
            prefix = 'Sr. ' if self.is_male else 'Sra. '

        return f'{prefix}{self.nombre} {self.apellido}'


class Pizzeria:
    ''' Clase componente (Propietario <-<> Pizzeria) y contenedora (Pizzeria ++-> Pizza) '''

    def __init__(self, nombre: str, direccion: str, propietario: Propietario, pizzas:list[Pizza] = []) -> None:
        ''' Crea una instancia/sucursal con calificación media (máx. 5) '''
        self.NOMBRE: str = nombre
        self.DIRECCION: str = direccion
        self.calificacion: float = 2.5
        self.__propietario: Propietario = propietario

        if (type(pizzas) != list or len(pizzas) == 0): # Aunque sea una pizza, debe estar dentro de una lista
            self.pizzas = []
        else:
            self.pizzas = pizzas

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

    def agregar_pizza(self, pizza:Pizza) -> None:
        ''' Añade una pizza al menú de la sucursal '''
        self.pizzas.append(pizza)

    def agregar_pizzas(self, pizzas:list[Pizza]) -> None:
        ''' Añade varias pizzas al menú de la sucursal '''
        self.pizzas += pizzas

    def __str__(self) -> str:
        ''' Retorna información general de la pizzería '''
        info = f'{self.nombre} ubicada en {self.DIRECCION}, perteneciente a {self.__propietario}'

        if (len(self.pizzas) > 0):
            info += '\n\n------ MENÚ ------\n'
            for pizza in self.pizzas:
                info += str(pizza)

        return info


class Ingrediente:
    ''' Clase componente '''
    def __init__(self, nombre:str) -> None:
        ''' Crea un nuevo ingrediente '''
        self.nombre = nombre
    
    def __str__(self):
        ''' Retorna el nombre del ingrediente formateado '''
        return self.nombre.capitalize()

class Pizza:
    ''' Clase componente (Pizza <-++ Pizzera) y contenedora (Pizza <>-> Ingrediente)\n
    La preparación de las pizzas usualmente depende de la sucursal '''
    def __init__(self, nombre: str, ingredientes: list[Ingrediente]) -> None:
        ''' Crea una nueva pizza (omitir la palabra "pizza" en instancia) '''
        self.nombre = nombre
        self.ingredientes = ingredientes
    
    def __str__(self) -> str:
        ''' Retorna la descripción de la pizza según sus ingredientes '''
        if (len(self.ingredientes) > 1):
            ingredientes = f"{', '.join([str(i) for i in self.ingredientes[:-1]])} y {self.ingredientes[-1]}"
        else:
            ingredientes = str(self.ingredientes[0])

        return f'Pizza "{self.nombre.capitalize()}"\n└──Contiene {ingredientes}\n'
    
    def __del__(self) -> None:
        ''' Indica la eliminación de la pizza '''
        print(f'La receta de la pizza "{self.nombre}" ha sido quemada\nSe extrañará su grasoso sabor\n')


if __name__ == '__main__':
    queso = Ingrediente('queso')
    pepperoni = Ingrediente('PePPeroni')
    salsa = Ingrediente('SALSA')
    pinia = Ingrediente('pIña')
    jamon = Ingrediente('jAMON')
    chorizo = Ingrediente('chorizo')
    cebolla = Ingrediente('cebollA')
    jalap = Ingrediente('jalapeÑos')

    hawaiiana = Pizza('hawaiana', [queso, salsa, pinia, jamon])
    pizza_queso = Pizza('queso', [queso])
    clasica = Pizza('clásica', [queso, salsa, pepperoni])
    mexicana = Pizza('mexicana', [queso, salsa, chorizo, cebolla, jalap])

    yo = Propietario('Marco', 'Cordero')  # Mal nombre de variable
    petra = Pizzeria('Petra Pizzas a la leña', 'Av Rafael Sanzio 522', yo)
    petra.agregar_pizzas([clasica, mexicana])
    
    tu = Propietario(gender=True, is_male=False)
    donimos = Pizzeria('Donimo\'s', 'Av. Guadalupe 1626', tu, [hawaiiana])
    donimos.agregar_pizza(pizza_queso)

    print(petra, donimos, sep='\n\n')

    print("Se eliminará la primera y segunda sucursal")
    del petra
    del donimos