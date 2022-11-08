# IS727272 - Chain of responsability
# Sesión 22 - 08.11.22
from abc import ABC

# Interface
class Manejador(ABC):
    def siguiente(self, manejador):
        pass

    def manejador(self, peticion):
        pass

# Manejador abstracto base
class ManejadorBase(Manejador):
    siguiente_manejador: Manejador = None

    def siguiente(self, manejador) -> Manejador:
        ''' Define el siguiente manejador '''
        self.siguiente_manejador = manejador
        return manejador
    
    def manejador(self, peticion) -> str:
        ''' Maneja la continuidad de las pruebas '''
        if self.siguiente_manejador:
            return self.siguiente_manejador.manejador(peticion)
        return None

# --
class Tarea1(ManejadorBase):
    def manejador(self, peticion: dict) -> str:
        print('-I- Revisando el tipo de prueba')
        if peticion['tipo'] == 'concurrencia':
            print('-I- Montando ambiente para concurrencia')
        elif peticion['tipo'] == 'stress':
            print('-I- Montando ambiente para stress')
        else:
            print(f'-E- No se ha encontrado un ambiente para {peticion["tipo"]}')
            return None
        return super().manejador(peticion)

class Tarea2(ManejadorBase):
    def manejador(self, peticion: dict) -> str:
        print(f'-I- Iniciando temporizador de {peticion["duracion"]} segundos')
        if peticion['duracion'] > 300:
            print(f'-E- El temporizador supera el tiempo máximo')
            return None
        return super().manejador(peticion)

class Tarea3(ManejadorBase):
    def manejador(self, peticion: dict) -> str:
        print(f'-I- Ejecutando prueba con benchmark {peticion["benchmark"]}')
        return super().manejador(peticion)

# Pruebas
if __name__ == '__main__':
    especificaciones = {
        'tipo': 'concurrencia',
        'duracion': 5,
        'benchmark': 'benchmark1'
    }

    # Definición de los pasos de una prueba en particular
    prueba = Tarea1()
    prueba.siguiente(Tarea2()).siguiente(Tarea3())

    # Ejecución de la prueba
    prueba.manejador(especificaciones)