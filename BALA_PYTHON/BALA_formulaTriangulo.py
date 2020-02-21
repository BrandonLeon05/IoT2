### Formula del triangulo - Brandon Aldahir León Alvarado ###
""" Crear una funcion que calcule el area del triangulo """

class Triangulo():
    def calcular(self):
        numbera = int(input("Cual es la base del triangulo: "))
        numberb = int(input("Cual es la altura del triangulo: "))
        area = (numbera)*(numberb)/2   
        print ("El area del triangulo es de: "+ str(area))

tri = Triangulo()
tri.calcular()

