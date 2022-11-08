# IS727272 - Flyweight
# Sesión 21 - 04.11.22
from random import choice, randint

# Flyweight
class TipoArbol:
    def __init__(self, caracteristicas: str) -> None:
        self.caracteristicas = caracteristicas

# Fábrica Flyweight
class FabricaArboles:
    __tipo_arboles = {}

    def __init__(self, estados_iniciales: list) -> None:
        for estado in estados_iniciales:
            self.__tipo_arboles[self.generar_llave(estado)] = TipoArbol(estado)
    
    def generar_llave(self, estado: list) -> str:
        return "_".join(sorted(estado))
    
    def obtener(self, caracteristicas: list) -> TipoArbol:
        llave = self.generar_llave(caracteristicas)

        if not self.__tipo_arboles.get(llave):
            print('-W- El tipo de árbol no está definido. Ceando uno nuevo...')
            self.__tipo_arboles[llave] = TipoArbol(caracteristicas)
        else:
            print('-E- El tipo de árbol ya existe')
        
        return self.__tipo_arboles[llave]

    def listar_tipos(self) -> None:
        print(f'-I- Lista de tipos de árboles, total: {len(self.__tipo_arboles)}')

        for arbol in self.__tipo_arboles.keys():
            print('\t-', arbol)

class Arbol:
    def __init__(self, x: float, y: float, tipo: TipoArbol) -> None:
        self.x = x
        self.y = y
        self.tipo = tipo # Asociación con la clase tipo árbol

class Bosque:
    def __init__(self, fabrica: FabricaArboles) -> None:
        self.__arboles = []
        self.__fabrica = fabrica
    
    def plantar(self, x: float, y: float, *tipo: list) -> None:
        self.__fabrica.obtener(tipo)
        self.__arboles.append(Arbol(x, y, tipo))
        print(f'-I- Plantando árbol "{self.__fabrica.generar_llave(tipo)}" en x: {x}, y: {y}')

if __name__ == '__main__':
    # Defnir los tipos de árboles disponibles
    tipos_arboles = [
        ['cerezo', 'hoja_caduca'],
        ['nogal' 'hoja_caduca'],
        ['pino', 'hoja_perene'],
        ['olivo', 'hoja_perene'],
        ['mango', 'frutal'],
        ['naranjo', 'frutal']
    ]

    # Árboles a plantar
    arboles_seleccionados = tipos_arboles[::2]

    # Agregar los árboles a la fábrica
    almacen_arboles = FabricaArboles(arboles_seleccionados)

    # Creación del bosque (contexto)
    print('-I- Creando bosque...')
    colomos = Bosque(almacen_arboles)
    colomos.plantar(randint(0, 1000), randint(0, 1000), 'alcanfor', 'totoro', 'gigante')
    for _ in range(1000):
        colomos.plantar(randint(0, 1000), randint(0, 1000), *choice(tipos_arboles))

    # Comprobación de cantidad final de árboles
    almacen_arboles.listar_tipos()