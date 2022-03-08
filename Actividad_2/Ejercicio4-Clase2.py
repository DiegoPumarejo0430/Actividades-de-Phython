from Library import *

def main():
    # Aplicacion de los Diccionarios
    #  persona = {
    #  "Nombre": "Yonatha"
    #   "Apellido": "Mendoza"
    #    "Edad": 23
    #}

 persona = {
     "datospersonales":{
        "Nombre": "Yonatha",
        "Apellido": "Mendoza",
        "Edad": 23
     },
     "salarial": {
         "salario": 2000000,
         "subtransporte": 50000,
         "subalimentacion": 60000
     }
    }

#print(persona["Nombre"]+ " " + persona["Apellido"])
#persona["Nombre"] = "Molina"
#print(f"{persona['Nombre']}{persona['Apellido']})
#print(f"Nombre: {persona["datospersonales"]['nombre']}")
print(f"Nombre: {persona['datospersonales']['nombre']} Apellido: {persona['datospersonales']['nombre']}  ")


if __name__ == "__main__":
    main()