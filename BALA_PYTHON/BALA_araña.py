### Cancion un elefante - Brandon Aldahir León Alvarado ###
""" Imprimir con una función la canción de los elefantes que se """
""" columpian en la tela de un araña                            """


class Elefante():
    def imprimir(self):
        i=1
        for i in range(1,101):
            if(i==1):
                print(i , "elefante se columpiaba sobre la tela de una araña y como veia que resistia fueron a llamar a otro elefante")
            else:
                print(i, "elefantes se columpiaban sobre la tela de una araña y como veia que resistia fueron a llamar a otro elefante")

                
elefante = Elefante()
elefante.imprimir()

