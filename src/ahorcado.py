"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Alexis Aparicio Mateos
Fecha: 07-11-2025
"""

def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para que el jugador 2 no vea la palabra
    introducida por el jugador 1.
    """
    print("\n" * 50)


def solicitar_palabra():
    """
    Solicita una palabra al jugador 1.

    La palabra debe tener mínimo 5 caracteres y solo contener letras.
    La entrada se valida y se convierte a mayúsculas antes de devolverla.

    Returns:
        str: La palabra válida introducida por el jugador 1 en mayúsculas.
    """

    palabra_valida = False

    while not palabra_valida:
        palabra = input("Jugador 1: Introduce la palabra a adivinar (mínimo 5 letras): ")

        if len(palabra) < 5:
            print("Error: La palabra debe tener al menos 5 caracteres.")
        elif not palabra.isalpha():
            print("Error: La palabra solo puede contener letras.")
        else:
            palabra_valida = True

    palabra = palabra.upper()
    return palabra


def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2.

    La letra debe ser válida (una sola letra), no estar repetida
    y contener solo caracteres alfabéticos.

    Args:
        letras_usadas (list): Lista de letras ya introducidas.

    Returns:
        str: La letra introducida en mayúsculas.
    """

    letra_valida = False
    while not letra_valida:
        letra = input("Introduce una letra: ")
        letra = letra.upper()
        if len(letra) > 1:
            print("Error: La letra solo puede ser un carácter.")
        elif not letra.isalpha():
            print("Error: No se ha introducido una letra.")
        elif letra in letras_usadas:
            print("Error: La letra ya está usada.")
        else:
            letra_valida = True

    letras_usadas.append(letra)
    return letra


def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego.

    Incluye el número de intentos restantes, la palabra oculta y
    las letras usadas hasta el momento.

    Args:
        palabra_oculta (str): La palabra con guiones bajos y letras adivinadas.
        intentos (int): Número de intentos restantes.
        letras_usadas (list): Lista de letras ya usadas.
    """

    print(f"\nIntentos restantes: {intentos}")
    print(f"Palabra: {palabra_oculta}")
    print(f"Letras usadas: {letras_usadas}\n")


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta mostrando las letras acertadas.

    Args:
        palabra (str): La palabra completa a adivinar.
        palabra_oculta (str): La palabra actual con guiones bajos y letras adivinadas.
        letra (str): La letra recién adivinada.

    Returns:
        str: La palabra oculta actualizada con las letras correctas reveladas.
    """

    palabra_actualizada = ""
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_actualizada += letra
        else:
            palabra_actualizada += palabra_oculta[i]
    return palabra_actualizada


def mostrar_muñeco(intentos):
    """
    Muestra un dibujo del ahorcado según los intentos restantes.

    Args:
        intentos (int): Número de intentos restantes.
    """
    if intentos == 4:
        print("O")
    elif intentos == 3:
        print("O")
        print("|")
    elif intentos == 2:
        print(" O")
        print("/|")
    elif intentos == 1:
        print(" O")
        print("/|\\")
    elif intentos == 0:
        print(" O")
        print("/|\\")
        print("/ \\")


def jugar():
    """
    Ejecuta la lógica principal del juego del ahorcado.
    """

    print("=== JUEGO DEL AHORCADO ===\n")

    INTENTOS_MAXIMOS = 5

    palabra = solicitar_palabra()

    limpiar_pantalla()

    palabra_oculta = "_" * len(palabra)
    intentos = INTENTOS_MAXIMOS
    letras_usadas = []
    juego_terminado = False

    print("Jugador 2: ¡Adivina la palabra!\n")

    while intentos > 0:
        mostrar_estado(palabra_oculta,intentos,letras_usadas)
        letra = solicitar_letra(letras_usadas)

        if letra in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print(f"¡Bien! La letra {letra} está en la palabra.!")
        else:
            print("¡Letra incorrecta!")
            intentos -=1
            mostrar_muñeco(intentos)
        if "_" not in palabra_oculta:
            juego_terminado = True
            break
    mostrar_estado(palabra_oculta,intentos,letras_usadas)

    if palabra_oculta == palabra:
        print(f"¡FELICIDADES! Has adivinado la palabra: {palabra}")
    else:
        print(f"¡GAME OVER! Te has quedado sin intentos.\nLa palabra era: {palabra}")


def main():
    """
    Punto de entrada del programa.
    Inicia el juego del ahorcado y pregunta si el jugador desea volver a jugar.
    """
    jugar()

    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == 's':
        main()

if __name__ == "__main__":
    main()
