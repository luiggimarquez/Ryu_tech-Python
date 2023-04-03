from modulos.clientes.addClients import *
from modulos.clientes.getClients import *
from modulos.clientes.doPurchase import *
from os import system

option=0
while(option != 4):

    while (True):

        system("cls")
        print("\n****** Menu ****** \n\n1. Cargar cliente \n2. Imprimir Clientes \n3. Ejemplo de factura \n4. Salir")
        try:
            option = int(input("\n            Ingresa opción: "))
            if(option == 1):
                addClients()
                break
            elif(option == 2):
                getClients()
                break
            elif(option == 3):
                doPurchase()
                break
            elif(option == 4):
                break

        except ValueError:

            print("\nError: Solo puedes ingresar la opción en número (1,2,3 o 4)")

        input("\n\nOpción errónea, presiona cualquier tecla para continuar")
         
system("cls")
print("\n\n\n********** Programa Finalizado **********\n\n\n\n")