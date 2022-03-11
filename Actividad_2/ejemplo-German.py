from api.Library import *

def main():
    SALARIO_MIN = 2000000
    SUB_ALIM = 150000
    SUB_TRANSP = 50000
    BONO = 80000
    nombre = input("Digite su nombre: ")
    salario = int(input("Digite su salario mensual: "))
    diastrabajados = int(input("digite los dias trabajados: "))
    sueldopagar = calcularsueldo(salario, diastrabajados)

    if salario < (SALARIO_MIN * 2):
        sueldopagar = sueldopagar + SUB_ALIM + SUB_TRANSP
    else:
        sueldopagar = sueldopagar + BONO

    print(f"mi nombre es: {nombre} y mi sueldo es {sueldopagar:.0f}")



if __name__ == "__main__":
    main()