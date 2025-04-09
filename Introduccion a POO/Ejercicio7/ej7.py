class Celular:
    def __init__(self):
        self.__apps = [""]*21
        self.__espacio = 1024
        self.__bateria = int(input("Ingrese el porcentaje de la bateria actual:")) 
        self.__esError = False
    def instalarApp(self):
        if self.__bateria > 0 and self.__bateria <= 100:
            tope = 1
            self.__apps[0] = "------"
            self.__apps[tope] = input("Aplicacion a instalar:")
            tope += 1
            peso_app = float(input("Ingrese cuanto pesa la app:"))
            if peso_app <= 0:
                print("Error, entrada invalida")
            elif peso_app >= 1024:
                print("Espacio lleno")
            else:
                self.__espacio -= peso_app
        else:
            print("ERROR, FUERA DE RANGO")
            self.__esError = True
    def usarApp(self):
        if self.__esError == False: 
            print(
                f''' -------APPS INSTALADAS--------
                1. {self.__apps[1]}
                2. {self.__apps[2]}
                3. {self.__apps[3]}
                4. {self.__apps[4]}
                5. {self.__apps[5]}
                6. {self.__apps[6]}
                7. {self.__apps[7]}
                8. {self.__apps[8]}
                9. {self.__apps[9]}
                10. {self.__apps[10]}
                11. {self.__apps[11]}
                12. {self.__apps[12]}
                13. {self.__apps[13]}
                14. {self.__apps[14]}
                15. {self.__apps[15]}
                16. {self.__apps[16]}
                17. {self.__apps[17]}
                18. {self.__apps[18]}
                19. {self.__apps[19]}
                20. {self.__apps[20]}
                '''
            )
            entrada = int(input("Ingresa en numero de app que deseas abrir:"))
            for i in range(len(self.__apps)):
                if i == entrada:
                    print(f"Ejecutando la app de {self.__apps[entrada]}")
                    if self.__espacio > 1000:
                        
        else:
            print("ERROR NO SE PUDO EJECUTAR LA APP")

#Main
celular = Celular()
celular.instalarApp()
celular.usarApp()
    