# Archivo: Sistema_Vehicular_Compacto.py
# Ubicación: Programacion-Orientada-Objetos/EjemplosMundoReal_POO/Sistema_Vehicular_Compacto.py

# Tarea: Ejemplos del Mundo Real y Características de la Programación Orientada a Objetos
# Este programa simula la interacción entre carros y personas.

class Carro:
    """
    Representa un automóvil.
    Atributos: modelo, anio, conductor (objeto Persona).
    """

    def __init__(self, modelo, anio):
        self.modelo = modelo
        self.anio = anio
        self.conductor = None

    def asignar_conductor(self, persona):
        """
        Asigna un objeto Persona como conductor de este Carro.
        """
        if isinstance(persona, Persona):
            self.conductor = persona
            print(f"'{persona.nombre}' asignado a '{self.modelo}'.")
        else:
            print(f"ERROR: No es una Persona válida: '{persona}'.")

    def __str__(self):
        """
        Devuelve una cadena descriptiva del carro y su conductor.
        """
        conductor_info = self.conductor.nombre if self.conductor else "nadie"
        return f'Carro: {self.modelo} | Año: {self.anio} | Conducido por: {conductor_info}.'


class Persona:
    """
    Representa a un individuo que puede conducir.
    Atributos: nombre, licencia.
    """

    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia

    def __str__(self):
        """
        Devuelve una cadena descriptiva de la persona y su licencia.
        """
        return f'Persona: {self.nombre} | Licencia No.: {self.licencia}.'


if __name__ == "__main__":
    print("--- Simulación de Sistema Vehicular POO ---")

    # Crear objetos
    carro1 = Carro('Corolla', 1998)
    carro2 = Carro('Blazer', 1997)

    # Usando los nombres Carlos y Ana
    persona_carlos = Persona('Carlos', 12345)  # Licencia ficticia para Carlos
    persona_ana = Persona('Ana', 67890)  # Licencia ficticia para Ana

    print("\n--- Estado Inicial ---")
    print(carro1)
    print(carro2)
    print(persona_carlos)
    print(persona_ana)

    # Asignar conductores
    print("\n--- Asignando Conductores ---")
    carro1.asignar_conductor(persona_carlos)  # Carro 1 ahora conducido por Carlos
    carro2.asignar_conductor(persona_ana)  # Carro 2 ahora conducido por Ana
    carro1.asignar_conductor("No es una persona")  # Prueba de error

    # Mostrar estado final
    print("\n--- Estado Final ---")
    print(carro1)
    print(carro2)

    print("--- Fin del ejemplo ---")