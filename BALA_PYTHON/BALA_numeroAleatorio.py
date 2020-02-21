### Numero Aleatorio - Brandon Aldahir León Alvarado ###
""" Generar un programa que dado un número generado aleatoriamente """
""" y permita compararlo con otro tecleado por el usuario y que    """
""" diga si este es mayor o menor                                  """

import random 

class Aleatorio():
    def calculaMenMay(self):
        numbera = random.randint(0,100)
        numberb = int(input("Teclea un numero entre el 0 y el 100: "))

        if numberb>numbera:
            print("El numero es mayor: " + str(numberb))
        else:
            print("El numero es menor: " + str(numberb) + " y el mayor es: " + str(numbera))

alea = Aleatorio()
alea.calculaMenMay()
