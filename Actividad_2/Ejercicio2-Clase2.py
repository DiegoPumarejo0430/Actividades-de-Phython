
def listas():
    listas1 = []
    lista2 = list

listaConElementos = [30,2000000, "Ing. Sistemas" ,"Yonatha Mdz", "Estudiante", True, ["Estudiar", "Mas Nada",23]]

#print(listaConElementos)

#Utilizado el ciclo for
print(" ")
print(" ")
print("CICLO FOR")
for i in range(len(listaConElementos)):
    print(listaConElementos[i])
print(" ")
print(" ")
#Utilizado el ciclo while
print("CICLO WHILE")
j=0
while j < len(listaConElementos):
    print(listaConElementos[j])
    j = j + 1

listaConElementos[1] = listaConElementos[1] + 200000

print(" ")
print(" ")
print(listaConElementos[6][2])
print(listaConElementos[-1][2])
print(listaConElementos[0:3])#Muestra de 0<3
print(listaConElementos[1:7:2])#Muestra posicion par
print(listaConElementos[0:7:2])#Muestra posicion inpar

print(" ")
#agrega elementos en posicion x
listaConElementos.insert(2, (["Sede Riohacha", "Miguel Romero"]))
print(listaConElementos)

print(" ")
#remueve elementos en posicion x
del listaConElementos[2]
print(listaConElementos)
print(" ")
listaConElementos.remove("Estudiante")
print(listaConElementos)

def main():
       listas()

if __name__ == "__main__":
        main()