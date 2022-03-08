





def main():

    #app de diccionarios
#    persona = {
 #   "nombre": "diego",
 #   "apellido": "pumarejo",
#  "edad" : 23
#   }

    persona = {

    "datospersonales":{
    "nombre" : "diego" ,
    "apellido": "pumarejo",
       "edad" : 23
    },


    "salarial" : {
     "salario" : 2000000 ,
      "subtransporte" : 50000 ,
      "subalimentacon" : 60000


    }

    }

   # print(persona["nombre"])
   # print(f"{persona['nombre']} {persona['apellido']}    ")
    print(f"Nombre: {persona['datospersonales']['nombre']} Apellido: {persona['datospersonales']['nombre']}  ")




if __name__=="__main__":
    main()