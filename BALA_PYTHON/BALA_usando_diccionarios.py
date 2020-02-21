### Diccionario datos básicos - Brandon Aldahir León Alvarado ###
""" Imprimir en un programa los datos de un diccionario con los """
""" datos basicos de 5 de tus compañeros                        """

class Diccionarios():
    def imprimir(self):
        diccionario = {'nombre' : ['Miriam', 'Dani', 'Fabian', 'Alan', 'Banda'], 'edad': [19, 23, 24, 19, 19], 'hobbies': ['Cine','Tomar','Conducir','Musica','Tomarx2']}

        for key in diccionario:
            print (key, ":", diccionario[key])

dic = Diccionarios()
dic.imprimir()

