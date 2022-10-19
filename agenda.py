import crud
import core
import os


agenda=[]
dircontacto={"data":[]}
isMenuActivate=True

if __name__ == "__main__":
    print("****************************************") 
    print("*                                      *")
    print("*¡Bienvenidos a Gestor de Contactos !  *")
    print("*                                      *")
    print("****************************************")
    os.system("pause")
    os.system('cls')
    if(core.checkFile('contacto.json')):
        dircontacto=core.LoadInfo('contacto.json')
    else:
        core.crearInfo('contacto.json',dircontacto)    
    while isMenuActivate==True:
        os.system('cls')
        print("****************************************") 
        print("*        ¡Menu Principal Agenda        *")
        print("****************************************")
        print("1.Agregar contacto\n2.Listar Contactos\n3.Buscar y editar\n4.Eliminar registro\n5.Salir")
        op=int(input())
        print(op)
        if op==1:
            crud.AddItemDicc()
            dircontacto=core.LoadInfo('contacto.json')
        elif op==2:
            crud.VerData(dircontacto)
        elif op==3:
            pass
        elif op==4:
            pass
        elif op==5:
                rta=input("Desea Terminar el programa S o N")
                if rta.upper()=="S":
                    isMenuActivate=False
                elif rta.upper()=="N":
                    isMenuActivate=True
