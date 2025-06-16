from abc import ABC, abstractmethod

# Clase base abstracta: Define la idea general de un "Trabajador"
class Trabajador(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def trabajar(self):
        """Método abstracto: Cada tipo de trabajador trabaja de una forma distinta."""
        pass

    def presentarse(self):
        """Método concreto: Todos los trabajadores pueden presentarse."""
        print(f"Hola, soy {self.nombre}.")

# Clase concreta que hereda de Trabajador
class Doctor(Trabajador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar(self):
        """El Doctor implementa cómo "trabaja": curando."""
        print(f"{self.nombre} está atendiendo pacientes en el hospital.")

# Clase concreta que hereda de Trabajador
class Constructor(Trabajador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar(self):
        """El Constructor implementa cómo "trabaja": construyendo."""
        print(f"{self.nombre} está construyendo un edificio.")

# --- Demostración ---
if __name__ == "__main__":
    print("--- Demostración de Abstracción ---")

    # Podemos crear objetos de las clases concretas
    mi_doctor = Doctor("María")
    mi_constructor = Constructor("Carlos")

    mi_doctor.presentarse()
    mi_doctor.trabajar()

    print("-" * 20)

    mi_constructor.presentarse()
    mi_constructor.trabajar()

    # Intentar crear un objeto de la clase abstracta directamente (daría error al intentar usar 'trabajar')
    # trabajador_generico = Trabajador("Unknow")
    # trabajador_generico.trabajar()