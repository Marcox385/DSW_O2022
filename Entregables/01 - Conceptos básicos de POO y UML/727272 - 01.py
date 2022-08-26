# IS727272 - Cordero Hernández, Marco Ricardo

class Vehiculo:
    ''' Superclase base para vehículos abstractos '''

    VELOCIDAD:float = 0
    LIMITE:int = 0
    GASOLINA:float = 0

    def __init__(self, llantas:int = 4, placa:str = 'abc-123', limite:int = 200, kilometraje:float = 0) -> None:
        ''' Inicializa un nuevo vehículo '''
        self.llantas = llantas
        self.placa = placa
        self.LIMITE = limite
        self.kilometraje = kilometraje

    @staticmethod
    def encender() -> None:
        ''' Se enciende el vehículo '''
        return 'Vehículo encendido'
    
    @staticmethod
    def apagar() -> None:
        ''' Se apaga el vehículo '''
        return 'Vehículo apagado'

    @classmethod
    def acelerar(cls, aumento:float = 1) -> None:
        ''' Acelerar vehículo por alguna cantidad '''
        if (cls.VELOCIDAD <= cls.LIMITE and not (cls.VELOCIDAD + aumento) > cls.LIMITE):
            cls.VELOCIDAD += aumento
    
    @classmethod
    def frenar(cls, disminucion:float = 1) -> None:
        ''' Desacelerar vehículo por alguna cantidad '''
        if (cls.VELOCIDAD != 0 and cls.VELOCIDAD - disminucion >= 0):
            cls.VELOCIDAD -= disminucion
    
    @classmethod
    def poner_gasolina(cls, litros:float) -> None:
        ''' Poner gasolina al vehículo '''
        if (litros < 0):
            raise ValueError

        cls.GASOLINA += litros

class Automovil(Vehiculo):
    ''' Subclase heredada de Vehículo '''

    def __init__(self, placa:str = 'abc-123', limite:int = 200, kilometraje:float = 0) -> None:
        super().__init__(4, placa, limite, kilometraje)

    @staticmethod
    def activar_parabrisas(velocidad:int = 1) -> str:
        ''' Se activa el parabrisas en una velocidad determinada '''

        return f'Parabrisas activados en velocidad {velocidad}'

class Motocicleta(Vehiculo):
    ''' Subclase heredada de Vehículo '''

    def __init__(self, placa:str = 'abc-123', limite:int = 200, kilometraje:float = 0) -> None:
        super().__init__(2, placa, limite, kilometraje)

    @staticmethod
    def derrapar(vueltas:int) -> str:
        ''' Derrapar la moto como lo haría Smokey Nagata '''

        return f'¡La mota ha dado {vueltas} vueltas!'

jetta = Vehiculo(placa = '')
print(jetta)