# IS727272 - Proxy
# Sesión 21 - 04.11.22
from abc import ABC, abstractmethod

# Interface de servicio
class Operaciones(ABC):
    @abstractmethod
    def obtener_usuarios(self, role:str) -> list:
        pass

# Servicio
@singleton
class MongoMejorado(Operaciones):
    def __init__(self) -> None:
        self.__table_users = {}
        self.__table_roles = {}
    
    def llenar_datos(self) -> None:
        # Tabla usuarios, nivel de acceso: privado
        self.__table_users = {
            '112233': {
                'nombre': 'MRCH',
                'nivel': 3
            }
        }

        # Tabla roles, nivel de acceso: privado
        self.__table_roles = {
            'profesor': ['112233', '334455'],
            'investigador': ['112233', '223235']
        }
    
    def obtener_usuarios(self, role: str) -> list:
        ''' Imprime la lsita de usuarios asignados a un role '''
        for user_id in self.__table_users[role]:
            print('\t-', self.__table_users[user_id]['nombre'])
    
    def obtener_nivel_acceso(self, id: str) -> int:
        pass

    def insertar_usuario(self, id: str, **datos) -> None:
        self.__table_users[id] = {
            'nivel_acceso': datos['nivel_acceso'],
            'nombre': datos['nombre']
        }
        self.__table_roles[datos['role']].append(id)

# Proxy
class Proxy(Operaciones):
    def __init__(self, db: MongoMejorado) -> None:
        self.__db = db
    
    def obtener_usuarios(self, role: str, id_solicitante: str) -> object:
        pass #if self.check_acces
    
    def check_access() -> None:
        pass

    def log_access() -> None:
        print('-I- Insetando una entrada en el archivo de acceso...')

if __name__ == '__main__':
    print('-I- Ejecución de la consulta adirectamente usando el proxy')
    db = MongoMejorado()
    db.llenar_datos()
    # db.insertar_usuario('99887766', nombre = 'Ivan Villalon', role)
    db.obtener_usuarios('profesor')
    print('-' * 80)

    print('-I- Ejecución d ela consulta usando un proxy a un nu')
    db2 = MongoMejorado()
    db2.llenar_datos()
    proxy = Proxy(db2)
    proxy.obtener_usuarios('profesor', '11223344')
    print('-' * 80)

    print('-I- Ejecución de la consulta usando un proxy a un o')
