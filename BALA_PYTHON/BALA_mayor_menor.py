### Mayor o Menos - Brandon Aldahir León Alvarado ###
""" Programa con 2 funciones que permita saber cual de estos numero """
""" es mayor o saber cual es menor de dichos numeros                """
from comparar_numeros import comparar

class mayor_menor:
    def __init__(self):
        self.com = comparar()
        n1 = int(input("Ingresa el primer número: "))
        self.n1 = int()
        print("")
        n2 = int(input("Ingresa el segundo número: "))
        self.n2 = int()
        print("")
        opcion = int(input("Selecciona una opcion:" + '\n' + "1. Mayor" + '\n' +  "2. Menor" + '\n'))
        print("")
        
        if opcion==1:
            self.com.mayor(n1, n2)
            print("El mayor es ", self.com.resultado)
        elif opcion ==2:
            self.com.menor(n1, n2)
            print("El menor es ", self.com.resultado)
        else:
            print("Seleccion una opcion válida, solo números 1 o 2")
            
a = mayor_menor()

