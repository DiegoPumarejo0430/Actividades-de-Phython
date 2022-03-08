
import math
print ("CALCULAR LA RAIZ DE UN NUMERO")

def calculo(base):
    res =  math.sqrt(base) 
    return res

def main():
    num = int(input("numero a calcular: "))
    if num < 0 :
        print (f"Error, no existe raiz para un numero negativo ")

    else :
        if num == 0 :
              print (f"la raiz de 0 es 0")
        else:
            res = calculo(num)
            print (f"el resultado es:  {res}")


if __name__ == "__main__":
    main()