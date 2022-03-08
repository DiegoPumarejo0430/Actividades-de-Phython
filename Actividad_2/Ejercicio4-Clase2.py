# **********************
# manejo de listas 
#********************


"""

lo mismo

"""

def listas():
 lista=[1,2]
 lista2 = list()

listaconelementos = [30,2000000, "jaider quintero",True,"fin",["magister",24,"especializado"]] 
#print(listaconelementos[3])
print("*************ciclo for*****************")
for i in range(len(listaconelementos)):
    print(listaconelementos[i])

print("***********ciclo while*************")

j=0
while j < len(listaconelementos):
    print(listaconelementos[j])
    j=j+1

listaconelementos[1]=listaconelementos[1]+200
print("****************** listas - posicion **********************")
print(listaconelementos[5][2])
print(listaconelementos[-1][2])
print(listaconelementos[3:5])
print(listaconelementos[1:6:2])
print(listaconelementos[0:6:2])

print(listaconelementos[1]+200)

print("****************** add final **********************")
listaconelementos.append("sede riohacha")
print(listaconelementos)

print("****************** add- posicion **********************")

listaconelementos.insert(2,["pais","colombia"])

print(listaconelementos)

print("****************** del- posicion **********************")

del listaconelementos[2]

print(listaconelementos)


print("****************** add- posicion **********************")

listaconelementos.remove("jaider quintero")

print(listaconelementos)

def main ():


    listas()

if __name__ == "__main__" :

    main()
