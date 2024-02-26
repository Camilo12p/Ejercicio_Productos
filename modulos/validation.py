

def valiateInt(nameVar:str,subject:str, action:str=''):
    try:
        number=int(input(f'Ingrese el {nameVar} del {subject} {action} --> '))
        if number>=0:
            return number
        else:
            return valiateInt(nameVar,subject,action)
    except ValueError:
        return valiateInt(nameVar,subject,action)
    

def valiateStr(nameVar:str,subject:str,action:str=''):
    string=input(f'Ingrese el {nameVar} del {subject} {action} --> ')
    if string.isalpha():
        return string
    else:
        return valiateStr(nameVar,subject,action)

def productRegister(srcData:dict,id:int):
    if str(id) in srcData.get('productos'):
        return True
    else:
        return False


def exit():
    e=str(input('Desea Salir?\nN. Para no \n Enter. Para Salir\n--> ')).lower()
    if e=='n' or e=='no':
        return True
    elif e=='':
        return False
    else:
        return exit()

def estado(srcData:dict):
    print('entra')
    input()
    for key, value in srcData.get('productos').items():
        if int(value['stock']) >= int(value['stockMax']):
            value.update({'estado':'max-critico'})
        elif int(value['stock']) <= int(value['stockMin']):
            value.update({'estado':'min-critico'})
        elif int(value['stock'])==0:
            value.update({'estado': 'agotado'})
        else:
            value.update({'estado':'disponible'})