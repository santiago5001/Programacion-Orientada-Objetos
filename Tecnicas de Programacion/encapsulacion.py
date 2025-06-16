class CajaFuerte:
    """
    Clase simple para demostrar el encapsulamiento.
    El saldo de la caja fuerte está protegido.
    """
    def __init__(self, saldo_inicial=0):
        # El saldo es un atributo privado (por convención en Python, doble guion bajo)
        self.__saldo = saldo_inicial

    # Método para ver el saldo (getter)
    def ver_saldo(self):
        return self.__saldo

    # Método para ingresar dinero (modifica el saldo de forma controlada)
    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Ingresado: ${cantidad}. Nuevo saldo: ${self.__saldo}")
        else:
            print("No se puede ingresar una cantidad negativa o cero.")

    # Método para sacar dinero (modifica el saldo de forma controlada)
    def sacar_dinero(self, cantidad):
        if cantidad > 0:
            if self.__saldo >= cantidad:
                self.__saldo -= cantidad
                print(f"Retirado: ${cantidad}. Nuevo saldo: ${self.__saldo}")
            else:
                print("No hay suficiente dinero en la caja fuerte.")
        else:
            print("No se puede retirar una cantidad negativa o cero.")

# --- Demostración ---
if __name__ == "__main__":
    print("--- Demostración de Encapsulamiento ---")

    mi_caja = CajaFuerte(100) # Creamos una caja con 100 de saldo inicial

    print(f"Saldo inicial: ${mi_caja.ver_saldo()}")

    # Acciones controladas por métodos
    mi_caja.ingresar_dinero(50)
    mi_caja.sacar_dinero(30)
    mi_caja.sacar_dinero(200) # Intento de sacar más de lo que hay
    mi_caja.ingresar_dinero(-10) # Intento de ingreso inválido

    print(f"Saldo final: ${mi_caja.ver_saldo()}")

    # Intentar acceder al saldo directamente (Python lo dificulta, pero es un ejemplo de por qué es mala práctica)
    # print(mi_caja.__saldo) # Esto daría un error (AttributeError)
    # print(mi_caja._CajaFuerte__saldo) # Esto funcionaría, pero es para fines de demostración, no para uso normal.