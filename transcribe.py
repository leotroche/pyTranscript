from colors import COLORS
from os import path
from speech_recognition import Microphone, AudioFile, Recognizer
from time import sleep


# Definir el reconocedor de voz
r = Recognizer()


def __transcribe_audio(audio_data):
    try:
        # Utilizar Google Speech Recognition para transcribir el audio
        text = r.recognize_google(audio_data, language="es-LA")
        return text

    except Exception as e:
        print(COLORS.RED + "Error:" + COLORS.RESET, e)
        return None


def from_microphone():
    with Microphone() as source:
        # Escuchar el audio del microfono
        audio_data = r.listen(source)
        return __transcribe_audio(audio_data)


def from_file(file_name):
    if not path.exists(file_name + ".wav"):
        print(COLORS.RED + "Archivo no encontrado" + COLORS.RESET)
        sleep(2)
        return None

    with AudioFile(file_name + ".wav") as source:
        # Escuchar el audio del archivo
        audio_data = r.record(source)
        return __transcribe_audio(audio_data)


def save_text(text):
    # Guardar el texto en un archivo
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text)
