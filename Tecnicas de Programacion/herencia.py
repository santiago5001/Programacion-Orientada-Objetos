# Clase Padre (Superclase)
class Vehiculo:
    """
    Clase base para cualquier vehículo.
    Define atributos y métodos comunes.
    """
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def encender(self):
        print(f"El {self.marca} {self.color} se ha encendido.")

    def apagar(self):
        print(f"El {self.marca} {self.color} se ha apagado.")

# Clase Hija (Subclase) que hereda de Vehiculo
class Coche(Vehiculo):
    """
    Clase Coche, hereda de Vehiculo.
    Añade un atributo específico y un método propio.
    """
    def __init__(self, marca, color, num_puertas):
        # Llama al constructor de la clase padre
        super().__init__(marca, color)
        self.num_puertas = num_puertas # Atributo específico de Coche

    def tocar_bocina(self):
        print("¡Pip pip! (desde el coche)")

# Clase Hija (Subclase) que hereda de Vehiculo
class Bicicleta(Vehiculo):
    """
    Clase Bicicleta, hereda de Vehiculo.
    Añade un atributo específico y un método propio.
    """
    def __init__(self, marca, color, tipo_bicicleta):
        # Llama al constructor de la clase padre
        super().__init__(marca, color)
        self.tipo_bicicleta = tipo_bicicleta # Atributo específico de Bicicleta

    def pedalear(self):
        print("¡Pedaleando fuerte! (en la bicicleta)")

# --- Demostración ---
if __name__ == "__main__":
    print("--- Demostración de Herencia ---")

    mi_coche = Coche("Toyota", "Rojo", 4)
    mi_bici = Bicicleta("Specialized", "Azul", "Montaña")

    print(f"Mi coche es un {mi_coche.color} {mi_coche.marca} con {mi_coche.num_puertas} puertas.")
    mi_coche.encender()       # Método heredado de Vehiculo
    mi_coche.tocar_bocina()   # Método propio de Coche
    mi_coche.apagar()         # Método heredado de Vehiculo

    print("-" * 20)

    print(f"Mi bici es una {mi_bici.color} {mi_bici.marca} de {mi_bici.tipo_bicicleta}.")
    mi_bici.encender()        # Método heredado (aunque no tenga sentido real, demuestra la herencia)
    mi_bici.pedalear()        # Método propio de Bicicleta
    mi_bici.apagar()          # Método heredado