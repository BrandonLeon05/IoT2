### Operaciones - Brandon Aldahir León Alvarado ###
""" Crear una funcion que calcule el resultado de la operacion  """
""" solicitada entre dos numeros (sumar, restar, multiplicar y dividir) """


class Operaciones():
    def menu(self):
        print("")
        print("**********************")
        print("* Operaciones        *")
        print("*                    *")
        print("* 1.- Sumar          *")
        print("* 2.- Restar         *")
        print("* 3.- Multiplicar    *")
        print("* 4.- Dividir        *")
        print("**********************")
        print("")
        
    def resultado(self):
        ope = int(input("Inserta el numero de la operación a realizar:"))
        
        n1 = int(input("Inserta el primer numero: "))
        n2 = int(input("Inserta el segundo numero: "))
        
        if (ope==1):
            print ("El resultado de la suma es: ", n1+n2)
            
        else:
            if (ope==2):
                print ("El resultado de la resta es: ", n1-n2)
                
            else:
                if (ope==3):
                    print ("El resultado de la multiplicación es: ", n1*n2)
                    
                else:
                    print ("El resultado de la división es: ", n1/n2)
                    
ope = Operaciones()
ope.menu()
ope.resultado()

