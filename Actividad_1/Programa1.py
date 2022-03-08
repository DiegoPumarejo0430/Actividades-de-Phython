
print ("CALCULAR EL AREA DE UN TRIANGULO")

def calculo(base,altura):
    area =  base *  altura / 2.0
    return area

def main():
    base = int(input("CUAL ES LA BASE: "))
    altura = int(input("CUAL ES LA ALTURA: "))
    area = calculo(base,altura)
    print (f"el resultado es:  {area}")

if __name__ == "__main__":
    main()

