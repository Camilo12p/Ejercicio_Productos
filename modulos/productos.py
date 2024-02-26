import modulos.validation as v
import modulos.coreFiles as c

def AgregarProductos(srcData:dict):
    id=v.valiateInt('id','producto')
    if v.productRegister(srcData,id):
        print('El id ya se encuentra registrado')
        input()
        return
    namePro=v.valiateStr('nombre','producto')
    stock=v.valiateInt('stock','producto')
    stockMax=v.valiateInt('stock maximos','producto')
    stockMin=v.valiateInt('stock minimo','producto')
    proveedor=v.valiateStr('proveedor','producto')

    producto={
        'id':id,
        'nameProducto':namePro,
        'stock':stock,
        'stockMax':stockMax,
        'stockMin':stockMin,
        'proveedor':proveedor
    }

    srcData.get('productos').update({id:producto})
    v.estado(srcData)
    c.updateFile('inventario.json',srcData)

def editProductos(srcData:dict):
    menu=[]
    id=str(v.valiateInt('id','producto','a editar'))
    data=srcData.get('productos').get(id)

    try:
        for key in data:
            menu.append(key)
        
        for i in range(len(menu)):
            if not(menu[i] == 'id'):
                print(f'{i}.{menu[i]}')

        op=int(input('Ingresa un valor --> '))

        for i in range(len(menu)):
            if op==i:
                if str(data[menu[op]]).isalpha():
                    data[menu[op]]=v.valiateStr(menu[op],'producto','a editar')
                else:
                    data[menu[op]]= v.valiateInt(menu[op],'producto','a editar')
    
    except TypeError:
        print('El id no se encuentra en el sistema')
        input()
        return

    srcData.get('productos').update({id:data})
    v.estado(srcData)
    c.updateFile('inventario.json',srcData)

def deleteProductos(srcData:dict):
    id=str(v.valiateInt('id','producto','a editar'))
    try:
        srcData.get('productos').pop(id)
        input()
    except KeyError:
        print('El id no se encuentra en el sistema:')
        input()
        return
    c.updateFile('inventario.json',srcData)


def searchProductos(srcData):
    id=str(v.valiateInt('id','producto','a editar'))
    try:
        for key,value in srcData.get('productos').get(id).items():
            print(f'{key} : {value}')
        input()
    except AttributeError:
        print('El id no se encuentra en el sistema:')
        input()
        return
