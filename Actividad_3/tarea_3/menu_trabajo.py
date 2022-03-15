import os
def mostrar_lista(lista):
  print(lista)  

def main():
    opcion = 0
    lista_empleados = [30,2000000, "Ing. Sistemas" ,"Yonatha Mdz", "Estudiante", True, ["Estudiar", "Mas Nada",23]]
    while opcion != 4 :
        os.system("cls")
        print("\n")
        print(f" 1. AGREGAR EMPLEADO A LA LISTA \n 2. ELIMINAR EMPLEADO DE LA LISTA \n 3.MOSTRAR LISTA DE EMPLEADOS \n 4. SALIR\n ")
        opcion=int(input("digite una opcion: "))

        if opcion==1 :
            print("Agregar Empleados")
        if opcion==2 :
            print("eliminar empleado")
        if opcion==3 :
            os.system("cls")
            print("MOSTRANDO LISTA DE EMPLEADOS...")
            mostrar_lista(lista_empleados)
            os.system("timeout /t 3 >null")
        if opcion==4 :
            print("salir")





if __name__ == "__main__":
 main()