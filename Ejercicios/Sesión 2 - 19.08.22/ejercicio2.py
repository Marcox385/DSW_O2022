# IS727272 - Cordero Hernández, Marco Ricardo

class Animal:

    MULT:float = 0.123

    def __init__(self, nombre:str = 'Animal', edad:int = 0, peso:float = 1.0) -> None:
        ''' Crea un nuevo objeto del tipo animal y le asigna atributos iniciales '''
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def detalles(self) -> str:
        ''' Retorna información de nuestro animal '''

        return f'Tengo un animal llamado {self.nombre}'

    def vacunar(self) -> str:
        ''' Acción de vacunar a mi animal '''

        return f'{self.nombre} vacunad@ con {self.peso * Animal.MULT}ml de medicamento'

    @classmethod
    def mod_mult(cls, valor:float) -> None:
        ''' Colocamos un nuevo valor para nuestar variable de clase '''
        cls.MULT = valor

    @staticmethod
    def hora_de_jugar(hh24:int) -> bool:
        ''' Retorna True si es hora de jugar '''
        return 10 <= hh24 <= 16

class Gato(Animal):
    pass

tom = Gato()
print(tom.hora_de_jugar(14))