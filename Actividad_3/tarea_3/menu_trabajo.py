import os, time
import collections
def mostrar_lista(lista):
    if len(lista) == 0 :
        print ("**  lista vacia  **")
    else:
        for i in range(len(lista)):
            print(f"{i+1} {lista[i]}")


def Agregar_final(lista):
    print("Agregar Empleados...")
    nombre=input("Nombre(s) : ")
    apellidos=input("Apellidos :")
    telefono=int(input("Telefono: "))
    edad=int(input("Edad: "))
    direccion=input("Direccion:")

    lista.append([nombre,apellidos,telefono,edad,direccion])

    
def Agregar_posicion(pos,lista):
    print("...Agregar Empleados...")
    nombre=input("Nombre(s): ")
    apellidos=input("apellidos:")
    telefono=int(input("telefono: "))
    edad=int(input("Edad: "))
    direccion=input("Direccion:")

    lista.insert(pos, ([nombre,apellidos,telefono,edad,direccion]))



def main():
    os.system("clear")
    opcion = "0"
    lista_empleados = []
    while opcion != "4":
        os.system("clear")
        print("\n ----------------------------------------------------------------------------")
        print("                         LISTA DE EMPLEADOS                                    ")
        print("\n ----------------------------------------------------------------------------")
        print(f" 1. AGREGAR EMPLEADO A LA LISTA \n 2. ELIMINAR EMPLEADO DE LA LISTA \n 3. MOSTRAR LISTA DE EMPLEADOS \n 4. SALIR")
        print("\n ----------------------------------------------------------------------------")
        opcion=input("digite una opcion: ")
        
        if opcion=="1":
            if len(lista_empleados) == 0:
                Agregar_final(lista_empleados)
            else: 
                pos=int(input("posicion: "))
                pos_h=pos-1
                if pos>len(lista_empleados):
                    Agregar_final(lista_empleados)
                else :
                    Agregar_posicion(pos_h,lista_empleados)
                    # Agregar_final(lista_empleados)
         

        if opcion=="2" :
            print("eliminar empleado")
            if len(lista_empleados) == 0:
               print("Lista Vacia")
            else:
                posicion = int(input("Digite Posicion a Buscar: "))
                lista_empleados.pop(posicion)
                print(lista_empleados)				




        if opcion=="3" :
            os.system("clear")
            print("MOSTRANDO LISTA DE EMPLEADOS...")
            mostrar_lista(lista_empleados)
        input()


        if opcion=="4" :
            print("cerrando...")
        
