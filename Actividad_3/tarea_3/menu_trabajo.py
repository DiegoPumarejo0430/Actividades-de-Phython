import os
def mostrar_lista(lista):
  print(lista)  

def main():
    lista_empleados = [30,2000000, "Ing. Sistemas" ,"Yonatha Mdz", "Estudiante", True, ["Estudiar", "Mas Nada",23]]
    opcion=int(input("digite una opcion: "))

    if opcion==1 :
        print("agregar empleados")
    if opcion==2 :
        print("eliminar empleado")
    if opcion==3 :
        os.system("cls")
        print("MOSTRANDO LISTA DE EMPLEADOS...")
        os.system("timeout /t 1 >null")
        mostrar_lista(lista_empleados)
    if opcion==4 :
        print("salir")





if __name__ == "__main__":
 main()