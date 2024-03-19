from menu import menu
from os import system


def set_terminal_title(title):
    # Definir la secuencia de escape para establecer el título
    escape_sequence = f"\033]0;{title}\007"
    # Imprimir la secuencia de escape
    system(f"echo -ne '{escape_sequence}'")


if __name__ == "__main__":
    set_terminal_title("Transcript v1.0.0")
    menu()
