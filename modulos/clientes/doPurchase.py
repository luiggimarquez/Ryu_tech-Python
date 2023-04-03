from .clientes import *
from os import system
import pickle
from pathlib import Path
import random

path = Path('clients.pickle')

def doPurchase():
    
    if(path.is_file()):
        
        system('cls')
        print("\n******* Ejemplo de Factura ******")

        with open('clients.pickle', 'rb') as clients:
            clientes = pickle.load(clients)
            clients.close()

        for i in range(len(clientes)):

            products=["Laptop", "Celular", "Televisor", "Auriculares", "Tablet", "SmartWatch", "GPS", "Disco Duro Externo"]
            prices =[120,150,1000,1500,10,25,333, 1589,666]
            quantity = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  

            clientes[i].doPurchase(random.choice(products),random.choice(prices),random.choice(quantity))   

        return input("\n\nPresiona cualquier tecla para continuar")
    else:
        system('cls')
        print("\n\nNo hay información de cliente almacenada, debes agregar primero un cliente\n\n")
        return input("\n\n      Presiona cualquier tecla para continuar")