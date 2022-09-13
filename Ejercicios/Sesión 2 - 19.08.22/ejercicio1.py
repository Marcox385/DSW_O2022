# IS727272 - Cordero Hernández, Marco Ricardo

class Gato:

    MULT:float = 0.123

    def __init__(self, nombre:str = 'Gatit@', edad:int = 0, peso:float = 1.0) -> None:
        # Buena práctica: incluir doc string
        ''' Crea un nuevo objeto del tipo gato y le asigna atributos iniciales '''
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def detalles(self) -> str:
        # Buena práctica: nunca imprimir dentro de la función, idealmente, retornar un valor
        ''' Retorna información de nuestr@ gatit@ '''

        # Buena práctica: formate mediante f"String" (introducido en Python3)
        # return f'Tengo un gatit@ llamad@ {self.nombre}'

        return 'Tengo un gatit@ llamad@ ' + self.nombre

    def vacunar(self) -> str:
        ''' Acción de vacunar a mi gato '''

        # Buena práctica: atributos de clase referidos directamente hacia la misma clase
        return f'{self.nombre} vacunad@ con {self.peso * Gato.MULT}ml de medicamento'

    # Buena práctica: método de clase mediante decoradores; omitir self, intercambiar por cls
    @classmethod
    def mod_mult(cls, valor:float) -> None:
        ''' Colocamos un nuevo valor para nuestar variable de clase '''
        Gato.MULT = valor # equivalente a /cls.Mult = valor/

    # Buena práctica: método estático; omitir self si no se accede a atributo
    @staticmethod
    def hora_de_jugar(hh24:int) -> bool:
        ''' Retorna True si es hora de jugar '''
        return 10 <= hh24 <= 16

tom = Gato('Tomás', 5, 8)
luna = Gato('Luna', 'Error')

# Mala práctica: definir atributos fuera de la definición de la clase
# tom.nombre = 'Tomás'
# luna.nombre = 'Luna'

print(tom)
print(luna)

print(luna.detalles())

print(tom.vacunar())

Gato.mod_mult(10)

print(tom.hora_de_jugar(13))