import modulos.coreFiles as c
import modulos.productos as prod
import modulos.validation as v
from tabulate import tabulate
import os

def main_menu(srcData:dict):
    def wrapper(func):
        func
        input()
        main_menu(srcData)
    
    titulo='''
        ++++++++++++++++++++++++++++++++++++
        +    Administrador de inventario   +
        ++++++++++++++++++++++++++++++++++++
    '''
    
    menu=[['1. Administrar Productos'],['2. Administrar Proveedores'],['3. Salir']]

    isOption=True

    
    while isOption:
        try:
            os.system('cls')
            print(titulo)
            print(tabulate(menu,tablefmt='grid'))
            op=int(input('ingrese una opcion --> '))
            if op==1:
                wrapper(menuProductos(srcData))
            elif op==2:
                wrapper(menuProveedores(srcData))
            elif op==3:
                isOption= v.exit()
        except ValueError:
            print('El valor ingresado no es valido')
            input()


def menuProductos(srcData:dict):
    
    titulo='''
        +++++++++++++++++++++++++++++++++++
        +    Administrador de productos   +
        +++++++++++++++++++++++++++++++++++
    '''
    
    menu=[['1. Agregar Productos'],['2. Editar Productos'],['3. Eliminar Productos'],['4. Buscar Productos'],['5. Salir']]

    isOption=True

    while isOption:
        os.system('cls')
        print(titulo)
        print(tabulate(menu,tablefmt='grid'))
        op=int(input('ingrese una opcion --> '))
        if op==1:
            prod.AgregarProductos(srcData)
        elif op==2:
            prod.editProductos(srcData)
        elif op==3:
            prod.deleteProductos(srcData)
        elif op==4:
            prod.searchProductos(srcData)
        elif op==5:
            isOption= v.exit()
    