

def main():
    class Persona():
        nombre = "Yonatha"
        apellido = "Mendoza"
        direccion = "Km 2"
        telefono = "3014032934"

        def mostrarpersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")
    persona1 = Persona() #crear una instancia de la clase
    persona1.nombre = "Jaime"
    #print(persona1.nombre)
    persona1.mostrarpersona()

    persona2 = Persona()
    persona2.nombre = "Thalia"
    persona2.apellido = "Motos"
    persona2.direccion = "Calle nose"
    persona2.telefono = "3020902093"
    persona2.mostrarpersona()

if __name__ == "__main__":
    main()
