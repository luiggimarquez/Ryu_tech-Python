

class Cliente:
    
    def __init__ (self, name, lastName, DNI, email, phone):

        self.name = name
        self.lastName = lastName
        self.DNI = DNI
        self.email = email
        self.phone = phone
    

    def __str__(self):

        return (f"\n Ejemplo de __STR__ -- Cliente registrado: {self.name} {self.lastName} -- , Clase: {type(self).__name__}")

    def userData (self):

        print(f"\nUsuario registrado: {self.name} {self.lastName}\nDNI: {self.DNI} \nEmail: { self.email} \nTelefono: {self.phone}\n")
    
    def doPurchase(self, item1, price, quantity):

        result = quantity*price
        print(f"\n\nEl usuario {self.name} {self.lastName} ha comprado el producto {item1} por un monto de {result}\n. Un correo a {self.email} será enviado con los dato de la compra.\nSe ha enviado tambien a su celular { self.phone}")






