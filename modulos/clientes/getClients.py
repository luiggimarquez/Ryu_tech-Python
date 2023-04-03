from .clientes import *
from os import system
from pathlib import Path
import pickle

path = Path('clients.pickle') #Ruta de archivado de los clientes para verificar si existe
def getClients():

    system("cls")
    print("\n****** Menu - Mostrar clientes Registrados y su método __STR__ *******")

    if(path.is_file()):
        
        with open('clients.pickle', 'rb') as clients:
            clientes = pickle.load(clients)
            clients.close()

        for i in range(len(clientes)):

            print(f"\n\nCliente {i}: {clientes[i].name}, datos registrados: \n", )
            print(clientes[i])
            clientes[i].userData()

        return input("\nPresione cualquier tecla para continuar")
    
    else:
        system("cls")
        print("\n\nNo hay clientes registrados, no hay nada para mostrar\n\n")
        return input("\nPresione cualquier tecla para continuar")