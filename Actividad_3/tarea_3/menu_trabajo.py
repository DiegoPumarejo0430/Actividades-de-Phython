import os, time
def mostrar_lista(lista):
    if len(lista) == 0 :
        print ("**  lista vacia  **")
    else:
        for i in range(len(lista)):
            print(lista[i])

def main():
    opcion = 0
    lista_empleados = []
    while opcion != 4 :
        os.system("clear")
        print("\n ----------------------------------------------------------------------------")
        print("                         LISTA DE EMPLEADOS                                    ")
        print("\n ----------------------------------------------------------------------------")
        print(f" 1. AGREGAR EMPLEADO A LA LISTA \n 2. ELIMINAR EMPLEADO DE LA LISTA \n 3. MOSTRAR LISTA DE EMPLEADOS \n 4. SALIR")
        print("\n ----------------------------------------------------------------------------")
        opcion=int(input("digite una opcion: "))
        
        if opcion==1 :
            print("Agregar Empleados")

            
        if opcion==2 :
            
            print("eliminar empleado")




        if opcion==3 :
            os.system("clear")
            print("MOSTRANDO LISTA DE EMPLEADOS...")
            mostrar_lista(lista_empleados)
            time.sleep(3)


        if opcion==4 :
            print("cerrando...")
            





if __name__ == "__main__":
 main()