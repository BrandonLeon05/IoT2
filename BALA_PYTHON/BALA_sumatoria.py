### Sumatoria de 10 valores creados en una lista - Brandon Aldahir León Alvarado ###
""" Función que cree 10 valores en una lista y haga la sumatoria        """
""" de la misma y los imprima                                           """

class Lista():
    def sumalista(self):
        suma=0
        lista=[10,20,30,40,55,66,77,89,91,100]

        for i in lista:
            suma = suma + i

        print (suma)
       
lis = Lista()
lis.sumalista()
