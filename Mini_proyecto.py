# Importamos deque para utilizarla como pila
from collections import deque


# Clase que representa la pila de cartas
class Pila:

    def __init__(self):
        self.cartas = deque()

    # Agregar una carta
    def push(self, carta):
        self.cartas.append(carta)

    # Retirar la carta superior
    def pop(self):
        if not self.cartas:
            print("La pila está vacía.")
            return None
        return self.cartas.pop()

    # Consultar la carta superior
    def cima(self):
        if not self.cartas:
            print("La pila está vacía.")
            return None
        return self.cartas[-1]

    # Cantidad de cartas
    def cantidad(self):
        return len(self.cartas)

    # Verificar si está vacía
    def esta_vacia(self):
        return len(self.cartas) == 0

    # Vaciar la pila
    def vaciar(self):
        self.cartas.clear()

    # Mostrar las cartas
    def mostrar(self):
        if not self.cartas:
            print("\nLa pila está vacía.")
            return

        print("\n--- CARTAS EN LA PILA ---")

        for carta in reversed(self.cartas):
            print("|", carta, "|")

        print("----------------")


# Menú principal
def mostrar_menu():
    print("\n================================")
    print("       🃏 JUEGO DE CARTAS")
    print("================================")
    print("1. Agregar carta")
    print("2. Retirar carta")
    print("3. Ver carta superior")
    print("4. Ver cantidad de cartas")
    print("5. Verificar si la pila está vacía")
    print("6. Vaciar pila")
    print("7. Mostrar cartas")
    print("8. Salir")
    print("================================")


# Agregar una carta
def agregar_carta(pila):

    print("\n--- SELECCIONE EL PALO ---")
    print("1. Corazones ♥")
    print("2. Diamantes ♦")
    print("3. Tréboles ♣")
    print("4. Picas ♠")

    palo = input("Seleccione el palo: ")

    if palo == "1":
        simbolo = "♥"
    elif palo == "2":
        simbolo = "♦"
    elif palo == "3":
        simbolo = "♣"
    elif palo == "4":
        simbolo = "♠"
    else:
        print("Palo no válido.")
        return

    print("\n--- SELECCIONE EL VALOR ---")
    print("A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K")

    valor = input("Ingrese el valor: ").upper()

    valores_validos = [
        "A", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "J", "Q", "K"
    ]

    if valor not in valores_validos:
        print("Valor no válido.")
        return

    carta = simbolo + " " + valor
    pila.push(carta)

    print("\nCarta agregada correctamente:", carta)


# Retirar una carta
def retirar_carta(pila):
    carta = pila.pop()

    if carta is not None:
        print("\nCarta retirada:", carta)


# Ver la carta superior
def ver_carta_superior(pila):
    carta = pila.cima()

    if carta is not None:
        print("\nCarta superior:", carta)


# Mostrar cantidad de cartas
def ver_cantidad(pila):
    print("\nCantidad de cartas:", pila.cantidad())


# Verificar si la pila está vacía
def verificar_pila(pila):
    if pila.esta_vacia():
        print("\nLa pila está vacía.")
    else:
        print("\nLa pila contiene cartas.")


# Vaciar la pila
def vaciar_pila(pila):
    if pila.esta_vacia():
        print("\nLa pila ya está vacía.")
    else:
        pila.vaciar()
        print("\nLa pila ha sido vaciada correctamente.")


# Creamos la pila
pila = Pila()


# Ciclo principal del programa
while True:

    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_carta(pila)

    elif opcion == "2":
        retirar_carta(pila)

    elif opcion == "3":
        ver_carta_superior(pila)

    elif opcion == "4":
        ver_cantidad(pila)

    elif opcion == "5":
        verificar_pila(pila)

    elif opcion == "6":
        vaciar_pila(pila)

    elif opcion == "7":
        pila.mostrar()

    elif opcion == "8":
        print("\nGracias por jugar. ¡Hasta luego! 🃏")
        break

    else:
        print("\nOpción no válida. Intente nuevamente.")
