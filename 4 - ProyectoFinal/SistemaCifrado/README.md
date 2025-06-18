# Sistema de Cifrado de Archivos (Fernet & Vigenère)

Este proyecto implementa un sistema completo para el cifrado y descifrado de archivos .txt, .pdf y .docx usando dos algoritmos:

    - Fernet (moderno, seguro y simétrico, basado en AES)
    - Vigenère (clásico, educativo, basado en sustitución polialfabética)

Incluye interfaz gráfica (interfaz.py), manejo de errores (logs/error.log), estructura modular y soporte completo para documentos.


# Estructura del Proyecto

    .
    ├── __pycache__/
    ├── claves/
    │   └── clave.key                  # Clave Fernet generada
    ├── funciones/
    │   ├── fernet.py                 # Lógica Fernet
    │   ├── vigenere.py               # Lógica Vigenère
    │   └── __pycache__/
    ├── logs/
    │   └── error.log                 # Registro de errores
    ├── interfaz.py                   # Interfaz gráfica con Tkinter
    ├── main.py                       # Ejecución con Vigenère
    ├── mainFernet.py                 # Ejecución con Fernet
    ├── prueba_gui.py                 # Archivo de prueba de GUI
    ├── requerimientos.txt            # Dependencias
    └── readme.md                     # Este documento


# Requisitos

    Instala las dependencias:

    pip install -r requerimientos.txt

    Contenido de requerimientos.txt:
        - cryptography
        - python-docx
        - PyPDF2
        - reportlab


# Uso de Algoritmos


# Fernet (Archivos .txt, .pdf, .docx)
    from funciones import fernet
        clave = fernet.generarClave("claves/clave.key")

    #cargar clave existente
        clave = fernet.cargarClave("claves/clave.key")

    #Cifrar
        ruta_cifrado = fernet.cifrarArchivo("documento.pdf", clave)

    #Descifrar
        ruta_descifrado = fernet.descifrarArchivo(ruta_cifrado, clave)


# Vigenère (educativo, solo letras A-Z en clave)
    from funciones import vigenere
        texto = vigenere.leerArchivo("documento.docx")
        cifrado = vigenere.cifrarVigenere(texto, "CLAVE")
        vigenere.guardarArchivo(cifrado, "doc_cifrado.txt")

    #Descifrar
        texto_descifrado = vigenere.descifrarVigenere(cifrado, "CLAVE")
        vigenere.guardarArchivo(texto_descifrado, "doc_descifrado.txt")

    #Ejecutar desde main
        python main.py        # Para Vigenère
        python mainFernet.py  # Para Fernet


# Funciones Clave

    leerArchivo(ruta) - Lee documentos .txt, .pdf, .docx
    guardarArchivo(texto, ruta) - Guarda en el mismo formato
    cifrarArchivo() / descifrarArchivo() - Fernet seguro
    cifrarVigenere() / descifrarVigenere() - educacional


# Interfaz Gráfica

    interfaz.py permite usar el sistema desde una ventana visual. Puedes seleccionar el archivo, tipo de cifrado y clave.


# Ejemplo de Ejecución Visual
    python interfaz.py

    Puedes compilar a .exe usando PyInstaller:
        pyinstaller --onefile interfaz.py


# Autor

    David Ricardo Ordoñez Mora
    Estudiante de Ingeniería de Software
    Proyecto de seguridad informática (Bootcamp / TalentoTech)


# Licencia

MIT License. Puedes modificar, compartir y usar libremente, dándole crédito al autor original.

