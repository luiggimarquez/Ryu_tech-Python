from .clientes import *
from os import system
import pickle
from pathlib import Path

path = Path('clients.pickle')
def addClients():

    while(True):
        cliente=[]
        clientes=[]
        flag="a"
        validate=True

        if(path.is_file()):
            with open('clients.pickle', 'rb') as clients:
                clientes = pickle.load(clients)
                clients.close()
       
        system("cls")
        print("\n******* Menú Agregar Usuario ******\n\n")
        while(True):
            try:
                DNI = int(input("Ingresa el DNI del cliente: "))
                break
            except ValueError:
                print("Error: Un DNI solo está formado por números, por favor ingresa DNI válido\n")

        #Validacion que los clientes sean únicos, filtramos por DNI
        if(clientes != []):
            for i in range(len(clientes)):
                if(clientes[i].DNI == DNI):
                    validate = False

        if(validate == True):

            name = input("Ingresa el nombre del cliente: ")
            lastName = input("Ingresa el apellido del cliente: ")
            email = input("Ingresa el email del cliente: ")

            while(True):
                try:
                    phone = int(input("Ingresa el celular del cliente: "))
                    break
                except ValueError:
                    print("Error: por favor ingresa número de celular válido (solo números)\n")
            
            cliente= Cliente(name, lastName, DNI, email, phone) #Se instancia la clase
            clientes.append(cliente) #Si el archivo clients existe, carga en "clientes" todas las instancia de clase
            
            with open('clients.pickle', 'wb') as clients:
                pickle.dump(clientes, clients)
                clients.close()
        else:
            print("Cliente ya está registrado\n")   
        
        while(True ):

            flag = input("\nDeseas agregar otro cliente? (Y/N)  ").lower()
            if(flag == 'y' or flag == 'n'):
                break
            else:
                system("cls")
                print("Por favor introduce una respuesta válida\n")
        
        if(flag == "n"):
            system("cls")
            break
        
    return input("****** DB de Clientes Actualizada - Presione alguna tecla para continuar ******")