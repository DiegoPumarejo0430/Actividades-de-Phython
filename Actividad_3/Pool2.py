

def main():
    class Persona():
        def __init__(self):
            self.nombre = input("Ingrese el Nombre: ")
            self.apellido = input("Ingrese el apellido: ")
            self.direccion = input("Ingrese la direccion: ")
            self.telefono = input("Ingrese el telfono: ")
        
        def mostrarpersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")
    
    #persona1 = Persona()
    #persona1.mostrarpersona()
    #persona2 = Persona()
    #persona2.mostrarpersona()

    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            self.__sueldo = float (input("Ingrese el sueldo: "))
            #self.transporte = 0
            #self.alimentacion = 0
            self.pension = 0
            self.salud = 0
            
            if self.__sueldo < 2000000 :
                self.alimentacion = 80000
                self.transporte = 60000
            else: 
                    self.transporte = 0
                    self.alimentacion = 0
            self.pension  = self.__sueldo + 0.04
            self.salud = self.__sueldo + 0.0375

            
            self.dev = self.alimentacion + self.transporte   
            self.ded = self.pension + self.salud
          
            #self.transporte = 0
            #self.alimentacion = 0
            #self.pension = 0
            #self.salud = 0
        def mostrarempleado(self):
            super().mostrarpersona()
            print(f"Sueldo: {self.__sueldo}")
            print(f"Devengado: {self.dev}")
            print(f"Deduciones: {self.ded}")
            print(f"Total a pagar: {self.dev + self.ded}")
            #print(f"Transporte: {self.transporte}")
            #print(f"Alimentacion: {self.alimentacion}")
            #print(f"Pension: {self.pension}")
        
            

    empleado1 = Empleado()
    #empleado1.__sueldo = 4000000
    empleado1.mostrarpersona()
         
if __name__ == "__main__":
    main()

