# ---------------------------------------------------------------------------------------------
# * Equipo: -1
# Nombre de los integrantes del equipo
# - IS727272; Cordero Hernández, Marco Ricardo
# ---------------------------------------------------------------------------------------------

from __future__ import annotations
from abc import ABC
from multiprocessing.sharedctypes import Value
from time import sleep

class Personaje:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.mochilas = None
        self.vida = 100
    
    def comer(self, alimento:Alimento):
        '''
        El personaje consume los alimentos para ganar vida
        '''
        self.vida += alimento.aporte_vida

class Objeto:
    def __init__(self, nombre:str) -> None:
        ''' Nuevo objeto '''
        self.nombre = nombre
    
    def __str__(self) -> str:
        ''' Nombre del objeto '''
        return self.nombre

class Mochila:
    '''
    La mochila tiene la capacidad de guardar un número limitado de artículos
    '''

    SPACER:int = 50 # Parte de reto

    def __init__(self, nombre, max_items:int=5):
        self.nombre = nombre
        self._max_items = max_items
        self.items:list[Objeto] = []
    
    # ---------------------------------------------------------------------------------------------
    # * RETO --- REALIZADO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: recoger colecciones de objetos a la mochila. Los objetos se pueden agrupar. No hace
    # falta conocer el numero de objetos. Actualmente solo es posible incluir los nombres de los
    # articulos.
    # 
    # Por ejemplo:
    #  - palitos x 5 recoger
    #  - rocas x 4
    #

    def capacidad_maxima(self) -> bool:
        ''' Revisar si la capacidad máxima ha sido alcanzada '''
        return len(self.items) < self._max_items
    
    def recoger(self, objetos:list[Objeto]) -> None:
        '''
        Ingresa articulos en la mochila
        '''
        if self.capacidad_maxima():
            for objeto in objetos:
                self.items.append(objeto)

                if not self.capacidad_maxima():
                    print(f'Capacidad máxima alcanzada, los demás objetos no serán recogidos')
                    break
            else:
                print('Objetos agregados exitósamente')
        else:
            raise ValueError(f'Se alcanzo la capacidad máxima de tu mochila, {self._max_items} en total')

    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Poder guardar herramientas dentro de la mochila, pero una version de la herramienta
    # a la vez. Por ejemplo, no se puede tener un Hacha normal y un Hacha de lujo en la misma mochila.
    #
    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Consolidar las expresiones en las condicionales
    #
    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # La lógica de las condicionales parece algo compleja 
    # Objetivo: Crear métodos para el manejo de las expresiones en las condicionales
    #
    # ---------------------------------------------------------------------------------------------
    # * RETO
    # ---------------------------------------------------------------------------------------------
    # Existe código que se repite constantemente
    # Objetivo: Evitar duplicidad de código en cada una de las ramas de las condicionales
    #
    def fabricar(self, herramienta) -> bool:
        '''
        Fabricar herramientas a través de los artículos en tu inventario. Regresa True si se pudo
        fabricar la herramienta
        '''
        if herramienta == 'martillo' and self.items.count('ramita') >= 3 and self.items.count('roca') >= 3 and self.items.count('cuerda') >= 2:
            herramienta = Martillo()
            self.recoger(str(herramienta))
            self.items.remove('ramita')
            self.items.remove('ramita')
            self.items.remove('ramita')
            self.items.remove('roca')
            self.items.remove('roca')
            self.items.remove('roca')
            self.items.remove('cuerda')
            self.items.remove('cuerda')
            return True
        else:
            return False

        if herramienta == 'hacha' and self.items.count('ramita') >= 1 and self.items.count('pedernal') >= 1:
            herramienta = Hacha()
            self.recoger(str(herramienta))
            self.items.remove('ramita')
            self.items.remove('pedernal')
            return True
        else:
            return False

        if herramienta == 'hacha_lujo' and self.items.count('ramita') >= 4 and self.items.count('pepita oro') >= 2:
            herramienta = HachaLujo()
            self.recoger(str(herramienta))
            self.items.remove('ramita')
            self.items.remove('ramita')
            self.items.remove('ramita')
            self.items.remove('ramita')
            self.items.remove('pepita oro')
            self.items.remove('pepita oro')
            return True
        else:
            return False
    
    # ---------------------------------------------------------------------------------------------
    # * RETO --- REALIZADO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Reemplazar los números con variables de clase.
    # Se puede aplicar a todo el código, no solamente a este dunder method.
    #
    def __str__(self) -> str:
        list_items = '\n'.join(self.items)
        return f'''{self.nombre:^{self.SPACER}}\n{"="*self.SPACER}\n{list_items}'''

# ---------------------------------------------------------------------------------------------
# * RETO --- REALIZADO
# ---------------------------------------------------------------------------------------------
# Objetivo: Agrega el metodo "demoler" con un "assert" el cual suponga que se tiene al menos
# 1 de durabilidad antes de ejecutar la acción.
#

class Demoler(ABC):
    def demoler(self) -> None:
        ''' Acción de demoler '''
        assert self.durabilidad >= 1, f'¡{str(self)} ya no soporta demoliciones!'
        self.durabilidad -= 1

class Martillo(Demoler):
    '''
    El martillo es una herramienta que se puede utilizar para demoler estructuras.
    El martillo requiere 3 rocas, 3 ramitas y 2 cuerdas para que se pueda fabricar.
    La durabilidad es el número de usos.
    '''
    def __init__(self, durabilidad:int=75, daño=17):
        self.durabilidad = durabilidad
        self.daño = daño

    def __str__(self) -> str:
        return 'Martillo'

class Hacha(Demoler):
    '''
    El hacha es una herramienta que se puede utilizar para talar árboles. Se puede crear
    al comienzo del juego con 1 ramita y 1 pedernal.
    '''
    def __init__(self, durabilidad:int=100, daño=27):
        self.durabilidad = durabilidad
        self.daño = daño
    
    def __str__(self) -> str:
        return 'Hacha normal'

class HachaLujo(Demoler):
    '''
    El Hacha de lujo es una versión del Hacha normal que tiene cuatro veces más durabilidad
    y requiere pepitas de oro en lugar de pedernal. Se necesitan 4 ramitas y 2 pepitas de oro
    para fabricar.
    '''
    def __init__(self, durabilidad:int=400, daño=27):
        self.durabilidad = durabilidad
        self.daño = daño
        
    def __str__(self) -> str:
        return 'Hacha de Lujo'

class Alimento:
    def __init__(self, nombre:str, tiempo_coccion:int=5) -> None:
        self.nombre = nombre
        self.tiempo_coccion = tiempo_coccion
        self.cocido = False
    
    def __str__(self) -> str:
        ''' Nombre del alimento '''
        return self.nombre

class Fogata:
    '''
    Una fogata es la clave para la supervivencia básica en el mundo. Aporta luz, calor y permite
    cocinar los alimentos. Requiere 3 césped y 2 troncos para que se pueda fabricar.
    Los personajes no pueden consumir alimentos crudos.
    '''

    CESPED_REQUERIDO = 3
    TRONCOS_REQUERIDOS = 2

    def __init__(self, materiales:list[Objeto]):
        cesped = 0
        troncos = 0

        for material in materiales:
            match str(material):
                case 'césped':
                    cesped += 1
                case 'tronco':
                    troncos += 1
        
        if not (cesped == self.CESPED_REQUERIDO and troncos == self.TRONCOS_REQUERIDOS):
            raise ValueError('No hay materiales suficientes para hacer la fogata')

    # ---------------------------------------------------------------------------------------------
    # * RETO --- REALIZADO
    # ---------------------------------------------------------------------------------------------
    # Los alimentos tienen diferentes tiempos de cocción. No queremos tener condicionales, entonces
    # usamos refactorización. Se ha comentado parte del código original.
    # Objetivo: Usar polimorfismo para obtener el tiempo de cocción y simplificar el método. Trata de
    # usar una interface con al menos los atributos: nombre, tiempo_coccion, cocido
    def cocinar(self, alimento:Alimento) -> None:
        '''
        Permite cocinar un alimento crudo en la fogata. Regresa el mismo alimento pero cocinado.
        '''
        if alimento.cocido == False:
            sleep(alimento.tiempo_coccion)
            alimento.cocido = True
            print(f'{str(alimento)} ha sido cocido')
        else:
            print('El alimento ya está cocido')

if __name__ == '__main__':
    # Personajes
    wilson = Personaje('Wilson')

    # Items
    backpack = Mochila('Morral chico', 10)
    backpack.recoger([Objeto('ramita'),Objeto('ramita'),Objeto('ramita'),Objeto('roca'),Objeto('roca'),Objeto('roca'),Objeto('cuerda'),Objeto('cuerda'),Objeto('cuerda')])

    # Fabrica
    # backpack.fabricar('martillo')
    # backpack.fabricar('hacha')
    # backpack.fabricar('hacha_lujo')

    # ---------------------------------------------------------------------------------------------
    # * RETO --- REALIZADO
    # ---------------------------------------------------------------------------------------------
    # Objetivo: Agregar al menos dos alimentos que se puedan cocinar en la fogata. Crear una fogata,
    # Cocinar los alimentos en la fogata y comer los alimentos.
    # 

    fogata = Fogata(['césped', 'césped', 'césped', 'tronco', 'tronco'])

    cordero = Alimento('cordero', 3)
    bistec = Alimento('bistec', 1)

    fogata.cocinar(cordero)
    fogata.cocinar(bistec)

    # Listamos los articulos en nuestra mochila
    print(backpack)