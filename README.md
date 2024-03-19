# 🎙️ pyTranscript v1.0.0

pyTranscript es una aplicación de línea de comandos que permite transcribir audio a texto, ya sea desde el micrófono de la computadora o desde un archivo .wav.

## 🎚️ Funcionalidades:

🎤 Transcribe a texto el audio proveniente del micrófono.  
💿 Transcribe a texto el audio proveniente de un archivo .wav.

## 📦 Dependencias:

Esta aplicación utiliza las siguientes dependencias:

- 🔊 [pyaudio](https://pypi.org/project/pyaudio/): Para acceder al micrófono de la computadora.
- 🗣️ [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Para transcribir el audio a texto.

Puedes instalar las dependencias utilizando pip:

```bash
pip install pyaudio
pip install SpeechRecognition
```

## 🚀 Ejecutable:

Puedes descargar el archivo ejecutable desde el siguiente enlace _(No firmado digitalmente)_: ⬇️ [Descargar](release/pyTranscript_1.0.0.exe)

## 🛠️ Compilar tu Propio Ejecutable

Si prefieres compilar tu propio ejecutable, sigue estos pasos:

1. Clona este repositorio

```bash
git clone https://github.com/leotroche/pyTranscript.git
```

2. Instala pyinstaller

```bash
pip install pyinstaller
```

3. Compila el codigo

```bash
pyinstaller -F main.py
```

El ejecutable estará disponible en _dist/main.exe_ -->

## 📝 Licencia:

Este proyecto se distribuye bajo la licencia MIT. Puedes encontrar los términos completos de la licencia en el archivo LICENSE del repositorio.
