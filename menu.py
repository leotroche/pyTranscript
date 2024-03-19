from colors import COLORS
from os import system
import transcribe


# ----------------------------------------------------------------


def menu_header():
    print(
        COLORS.CYAN
        + "╔═════════════════════════════╗\n"
        + "║     pyTranscript v1.0.0     ║\n"
        + "╚═════════════════════════════╝\n"
        + COLORS.RESET
    )


def main_menu():
    print(COLORS.CYAN + COLORS.UNDERLINE + "Seleccione una opción:" + COLORS.RESET)
    print("1. Transcribir desde micrófono")
    print("2. Transcribir desde archivo de audio")
    print("3. Salir\n")


def menu():
    while True:
        system("cls")

        menu_header()
        main_menu()

        option = input("Ingrese el número de la opción deseada: ")

        if option == "1":
            transcribe_from_microphone_option()
        elif option == "2":
            transcribe_from_file_option()
        elif option == "3":
            transcribe._
            exit()


# ----------------------------------------------------------------


def transcribe_from_microphone_option():
    system("cls")

    print(COLORS.YELLOW + "Por favor, habla ahora..." + COLORS.RESET, "\n")
    text = transcribe.from_microphone()

    if text is not None:
        transcribe.save_text(text)

        print(COLORS.GREEN + "Transcripción exitosa:" + COLORS.RESET, "\n")
        print(text, "\n")
        print(COLORS.GREEN + "Archivo guardado como: 'output.txt'" + COLORS.RESET)

        input("Presione una tecla para volver al menú principal.")


# ----------------------------------------------------------------


def transcribe_from_file_option():
    system("cls")

    audio_file = input(
        "Ingrese el nombre del archivo de audio "
        + COLORS.YELLOW
        + "(.wav)"
        + COLORS.RESET
        + ": "
    )

    print(COLORS.YELLOW + "Procesando, espere..." + COLORS.RESET, "\n")

    text = transcribe.from_file(audio_file)

    if text is not None:
        transcribe.save_text(text)

        print(COLORS.GREEN + "Transcripción exitosa:" + COLORS.RESET, "\n")
        print(text, "\n")
        print(COLORS.GREEN + "Archivo guardado como: 'output.txt'" + COLORS.RESET)

        input("Presione una tecla para volver al menú principal.")
