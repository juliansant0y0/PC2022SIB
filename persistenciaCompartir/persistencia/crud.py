import core as cr
import os
import time

def AddItemDicc():
            dicc={}
            dicDir={}
            os.system('cls')
            print("****************************************") 
            print("*                                      *")
            print("*¡   Registro de Contactos           ! *")
            print("*                                      *")
            print("****************************************")
            isAddItem=True
            while isAddItem==True:

                nombre=input("Nombre del contacto   : ")
                email=input("Email del contacto     : ")
                movil=input("Movil del contacto     : ")
                fechac=input("Fecha de cumpleaños   : ")
                os.system("pause")
                os.system('cls')
                print("****************************************") 
                print("*        ¡Registro de Direcciones!     *")
                print("****************************************")
                isAddDir=True
                while isAddDir==True:
                    valor=len(dicDir)
                    ciudad=input("Ingrese la Ciudad : ")
                    direccion=input("Ingrese la Direccion : ")
                    dicDir.update({valor:{"ciudad":ciudad,"direccion":direccion}})
                    rta=input("Desea ingresar otra Direccion S o N")
                    if rta.upper()=="S":
                        isAddDir=True
                    elif rta.upper()=="N":
                        isAddDir=False
                os.system("pause")
                os.system('cls')
                print("****************************************") 
                print("*        ¡Registro de Hobbies!         *")
                print("****************************************")
                isAddHob=True
                dicHob={}
                dicHob.clear()
                while isAddHob==True:
                    valor=len(dicHob)
                    hob=input("Ingrese el Hobbie : ")
                    dicHob.update({valor:{"hobbie":hob}})
                    rta=input("Desea ingresar otro Hobbie S o N")
                    if rta.upper()=="S":
                        isAddHob=True
                    elif rta.upper()=="N":
                        isAddHob=False   
                contacto={
                        "nombre":nombre,
                        "email":email,
                        "movil":movil,
                        "direcciones":dicDir,
                        "hobbies":dicHob
                    }
                cr.crearInfo("contacto.json", contacto)
                rta=input("Desea ingresar otro contacto S o N")
                if rta.upper()=="S":
                    isAddItem=True
                elif rta.upper()=="N":
                    isAddItem=False
def RecargarData(diccionario):
    cr.RefrescarData("contacto.json",diccionario)
def VerData(data):
    os.system('cls')
    for item in data['data']:
        print(f"{item['nombre']}\t{item['email']}".expandtabs())
    v=input("Presione enter para continuar....")

def BuscarData(data):
    pass
def BorrarData(data):
    pass

    

    

