import random
import pandas as pd
import os

# Archivo donde se almacenarán las estadísticas
ARCHIVO_ESTADISTICAS = "estadisticas_adivina_el_numero.xlsx"

def guardar_estadisticas(nombre, modo, dificultad, intentos, exito):
    """
    Guarda las estadísticas de una partida en un archivo Excel.
    """
    datos = {
        "Jugador": [nombre],
        "Modo": [modo],
        "Dificultad": [dificultad],
        "Intentos Usados": [intentos],
        "Éxito": ["Sí" if exito else "No"]
    }

    try:
        # Carga las estadísticas existentes, si el archivo ya existe
        df_existente = pd.read_excel(ARCHIVO_ESTADISTICAS)
        df_nuevo = pd.DataFrame(datos)
        df_actualizado = pd.concat([df_existente, df_nuevo], ignore_index=True)
    except FileNotFoundError:
        # Si no existe el archivo, crea uno nuevo
        df_actualizado = pd.DataFrame(datos)

    # Guarda los datos en el archivo Excel
    df_actualizado.to_excel(ARCHIVO_ESTADISTICAS, index=False)
    print("\nEstadísticas guardadas correctamente.")

def mostrar_estadisticas():
    """
    Muestra las estadísticas almacenadas en el archivo Excel.
    """
    try:
        df = pd.read_excel(ARCHIVO_ESTADISTICAS)
        print("\n=== Estadísticas de Juego ===")
        print(df)
    except FileNotFoundError:
        print("\nNo hay estadísticas disponibles. Juega una partida primero.")

def secondMenu():
    """
    Menú para elegir la dificultad y retorna el número máximo de intentos.
    """
    while True:
        print("Por favor elige la dificultad:")
        option = input("1. Fácil (20 intentos)\n2. Medio (12 intentos)\n3. Difícil (5 intentos)\n")
        if option == "1":
            return 20
        elif option == "2":
            return 12
        elif option == "3":
            return 5
        else:
            print("Opción no válida. Por favor intenta nuevamente.")

def onePlayer(nombre):
    """
    Modo de juego para 1 jugador.
    """
    dificultad = secondMenu()
    secreto = random.randint(1, 1000)
    intentos = 0

    print(f"\nTienes {dificultad} intentos para adivinar el número entre 1 y 1000.")
    while intentos < dificultad:
        intentos += 1
        try:
            numero = int(input(f"Intento {intentos}/{dificultad}. Dame un número: "))
            if numero < 1 or numero > 1000:
                print("El número debe estar entre 1 y 1000. Intenta nuevamente.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")
            continue

        if numero == secreto:
            print(f"¡Felicidades, {nombre}! Adivinaste el número en {intentos} intentos.")
            guardar_estadisticas(nombre, "1 Jugador", dificultad, intentos, True)
            return
        elif numero < secreto:
            print("Más alto.")
        else:
            print("Más bajo.")
    
    print(f"Lo siento, {nombre}. Se agotaron los intentos. El número era {secreto}.")
    guardar_estadisticas(nombre, "1 Jugador", dificultad, intentos, False)

def twoPlayer(nombre):
    """
    Modo de juego para 2 jugadores.
    """
    dificultad = secondMenu()

    while True:
        try:
            secreto = int(input("\nJugador 1, ingresa el número secreto (entre 1 y 1000): "))
            if 1 <= secreto <= 1000:
                break
            else:
                print("El número debe estar entre 1 y 1000.")
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número válido.")
    
    # Limpia la pantalla (compatibilidad con Windows y Unix)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Jugador 2, es tu turno. ¡Adivina el número!")
    intentos = 0

    while intentos < dificultad:
        intentos += 1
        try:
            numero = int(input(f"Intento {intentos}/{dificultad}. Dame un número: "))
            if numero < 1 or numero > 1000:
                print("El número debe estar entre 1 y 1000. Intenta nuevamente.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")
            continue

        if numero == secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            guardar_estadisticas(nombre, "2 Jugadores", dificultad, intentos, True)
            return
        elif numero < secreto:
            print("Más alto.")
        else:
            print("Más bajo.")

    print(f"Lo siento, no lograste adivinar. El número era {secreto}.")
    guardar_estadisticas(nombre, "2 Jugadores", dificultad, intentos, False)

def mainMenu():
    """
    Menú principal del juego.
    """
    print("=== Bienvenido a Adivina el Número ===")
    nombre = input("Por favor, dime tu nombre: ")

    while True:
        print("\nPor favor elige una opción:")
        option = input("1. Partida modo solitario\n2. Partida 2 jugadores\n3. Estadísticas\n4. Salir\n")
        if option == "1":
            onePlayer(nombre)
        elif option == "2":
            twoPlayer(nombre)
        elif option == "3":
            mostrar_estadisticas()
        elif option == "4":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Inicia el programa
mainMenu()
