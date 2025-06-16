# Reutilizamos la base de clases de animales para mostrar polimorfismo.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        """Método común, con una implementación básica."""
        print(f"{self.nombre} hace un sonido (genérico).")

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        """Implementación específica para Perro."""
        print(f"{self.nombre} ladra: ¡Guau guau!")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        """Implementación específica para Gato."""
        print(f"{self.nombre} maúlla: ¡Miau miau!")

class Vaca(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        """Implementación específica para Vaca."""
        print(f"{self.nombre} muge: ¡Muuuuuu!")

# --- Demostración ---
def pedir_sonido(animal):
    """
    Esta función no sabe qué tipo de animal es, pero puede pedirle que haga su sonido.
    Aquí se ve el polimorfismo en acción.
    """
    animal.hacer_sonido()

if __name__ == "__main__":
    print("--- Demostración de Polimorfismo ---")

    mi_perro = Perro("Toby")
    mi_gato = Gato("Luna")
    mi_vaca = Vaca("Manchas")
    animal_generico = Animal("Desconocido")

    # Creamos una lista de diferentes animales
    animales_en_granja = [mi_perro, mi_gato, mi_vaca, animal_generico]

    # Iteramos sobre la lista y pedimos a cada uno que haga un sonido
    for animal in animales_en_granja:
        pedir_sonido(animal) # La misma llamada de función, pero diferentes resultados

    print("\nEl polimorfismo nos permite tratar diferentes tipos de objetos (Perro, Gato, Vaca)")
    print("de manera uniforme (como si fueran Animales) y aún así obtener comportamientos específicos para cada uno.")