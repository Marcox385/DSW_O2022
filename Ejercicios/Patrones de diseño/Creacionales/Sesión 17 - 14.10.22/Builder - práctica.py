# IS727272 - Builder práctica

# Se propone la creación de una pizzería
# Los productos pueden ser distintas formas de pizza
# Los constructores pueden ser pizza o calzones
# Los directores pueden ser distintos estilos de pizza

from enum import Enum
from pydoc import describe

# Paso 1: Interfaz constructora
class Masa:
    ''' Estructura del producto '''
    def __init__(self, descripcion: str) -> None:
        self.__descripcion = descripcion
        self.__ingredientes = []
    
    @property
    def ingredientes(self) -> 'list[str]':
        ''' Retorna los ingredientes del producto '''
        return self.__ingredientes
    
    def agregar_ingrediente(self, ingrediente:str) -> None:
        ''' Agrega un ingrediente a la lista de ingredientes '''
        self.__ingredientes.append(ingrediente)
    
    def __str__(self) -> str:
        ''' Regresa la descripción de la pizza '''
        return self.__descripcion

# Paso 3: Productos
class MasaMagra(Masa):
    def __init__(self, descripcion:str) -> None:
        super().__init__(descripcion)

class MasaLigera(Masa):
    def __init__(self, descripcion:str) -> None:
        super().__init__(descripcion)

# Paso 2: Builders concretos
# Interfase
class Pizzeria:
    def agregar_queso(self, capas:int) -> None:
        ''' Agrega queso al calzone '''
        self.masa.agregar_ingrediente(f'{capas} capas de queso')
    
    def agregar_salsa(self, cantidad:int) -> None:
        ''' Agrega salsa al calzone '''
        self.masa.agregar_ingrediente(f'{cantidad}ml de salsa')
    
    def agregar_ingrediente(self, ingrediente:str) -> None:
        ''' Agrega un ingrediente no especificado '''
        self.masa.agregar_ingrediente(ingrediente)

class Pizza(Pizzeria):
    ''' Builder para pizza '''
    def __init__(self, masa:object) -> None:
        self.masa = masa

    def modificar_orilla(self, tipo:str) -> None:
        self.masa.agregar_ingrediente(f'Orilla tipo {tipo}')

class Calzone(Pizzeria):
    ''' Builder para calzone '''
    def __init__(self, masa:object) -> None:
        self.masa = masa

    def doblar_pizza(self) -> None:
        self.masa.agregar_ingrediente(f'Masa doblada')

# Paso 4: Clase directora
class Directora:
    class TiposPizza(Enum):
        # Tipo          valor
        HAWAIANA    =   'self.cocinar_hawaina()'
    
    def __init__(self, builder:Pizzeria) -> None:
        ''' Asociación de un builder concreto a la clase directora '''
        self.__producto = builder
    
    @property
    def producto(self) -> Pizzeria:
        ''' Asociación de un Builder concreto a la clase directora '''
        return self.__producto

    @producto.setter
    def producto(self, producto: Pizzeria) -> None:
        ''' Asociación de un Builder concreto a la clase directora '''
        self.__producto = producto
    
    def cocinar_hawaiana_ligera(self) -> Pizza:
        ''' Pasos para cocinar una pizza hawaiana '''
        hawaiana = Pizza(self.producto)
        hawaiana.agregar_salsa(250)
        hawaiana.agregar_queso(2)
        hawaiana.agregar_ingrediente('Piña')
        hawaiana.agregar_ingrediente('Jamón')
        return self.producto.masa.ingredientes

# Funcionamiento
if __name__ == '__main__':
    masa = MasaLigera('Masa ligerita')
    # pizza = Pizza(masa)
    # pizza.agregar_salsa(200)
    # pizza.agregar_queso(2)
    # pizza.agregar_ingrediente('Piña')
    # print(pizza.masa.ingredientes)

    print(Directora(Pizza(masa)).cocinar_hawaiana_ligera())