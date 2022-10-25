# IS727272 - Cordero Hernández, Marco Ricardo

class Menu:
    def __init__(self,  productos:'list[Producto]', categoria:str = 'Normal') -> None:
        ''' Retorna una nueva instancia de menú '''  
        self.categoria:str = categoria
        self.produtos:list[Producto] = productos
    
    def desplegar_menu(self):
        ''' Desplegar menú con sus productos correspondientes '''
        print(f'Menú', f'de {self.categoria}' if (self.categoria != 'Normal') else '')
        for p in range(len(self.productos)):
            print(f'{p + 1} - {self.productos[p].nombre} - ${self.productos[p].precio}')