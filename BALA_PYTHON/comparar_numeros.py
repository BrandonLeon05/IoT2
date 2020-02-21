### Clase comparar - Brandon Aldahir León Alvarado ###
""" Funciones para saber el numero mayor y numero menor entre 2 numeros """

class comparar:
    def __init__(self):
        self.resultado = 0
        
    def mayor(self, n1, n2):
        if n1>n2:
            self.resultado = n1
        else:
            self.resultado = n2
            
    def menor(self, n1, n2):
        if n1<n2:
            self.resultado = n1
        else:
            self.resultado = n2
            
