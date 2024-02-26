import menu as m

if (__name__=='__main__'):
    inventario={
        'productos':{},
        'proveedores':{}
    }
    m.c.checkFile('inventario.json',inventario)
    m.main_menu(inventario)