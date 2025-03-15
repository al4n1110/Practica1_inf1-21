#Clase(s)
class Persona:
    def __init__(self, nombre , edad , ciudad ):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        
    def saludo(self):
        print(f"Hola, soy {self.nombre} de {self.ciudad}")
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")
#Main
persona_1 = Persona("Juan", 20 , "La paz")
persona_2 = Persona("Fernando" , 14 , "Tarija")
persona_3 = Persona("Maria" , 18, "Oruro")

#Mostrando saludos
persona_1.saludo()
persona_2.saludo()
persona_3.saludo()