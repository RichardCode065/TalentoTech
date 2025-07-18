"""
interfaz.py - Interfaz gráfica del sistema de cifrado de archivos usando Vigenère y Fernet.
Permite al usuario seleccionar un archivo, ingresar una clave (para Vigenère),
y ejecutar operaciones de cifrado y descifrado mediante una GUI amigable.

Autenticado por:
    - main.py           (para cifrado/descifrado Vigenère)
    - mainFernet.py     (para cifrado/descifrado Fernet)

Archivos soportados:
    - .txt (Texto plano)
    - .pdf (Documentos PDF)
    - .docx (Documentos Word)
    - .cif (Solo para descifrado Fernet)
"""

# Importación de librerías
import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox

# Importar funciones de cifrado y descifrado
from main import cifrarVigenere, descifrarVigenere
from mainFernet import cifrarFernet, descifrarFernet

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Configuración del logger
logging.basicConfig(
    filename='logs/error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Colores de la interfaz
COLORFONDO = "#455372"
COLORCONTENEDOR = "#336699"
COLORBOTON = "#FFFFF0"
COLORTEXTO = "#FFFFF0"
COLORALERTA = "#CC3333"

# Variable global para la ruta del archivo
archivoSeleccionado = ""

def seleccionarArchivo():
    """
    Permite al usuario seleccionar un archivo y muestra su nombre.
    """
    global archivoSeleccionado
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=[
            ("Archivos cifrados Fernet", "*.cif"),
            ("Archivos de texto", "*.txt"),
            ("Documentos PDF", "*.pdf"),
            ("Documentos Word", "*.docx"),
            ("Todos los archivos", "*.*")
        ]
    )
    if ruta:
        archivoSeleccionado = ruta
        etiquetaRuta.config(text=f"Archivo: {ruta}")

def cifrarVigenereDesdeGui():
    """
    Ejecuta cifrado Vigenère desde la interfaz.
    """
    if not archivoSeleccionado:
        messagebox.showwarning("Atención", "Debes seleccionar un archivo primero.")
        return
    clave = entradaClave.get()
    if not clave:
        messagebox.showwarning("Atención", "Debes ingresar una clave.")
        return
    resultado = cifrarVigenere(archivoSeleccionado, clave)
    messagebox.showinfo("Resultado", resultado)

def descifrarVigenereDesdeGui():
    """
    Ejecuta descifrado Vigenère desde la interfaz.
    """
    if not archivoSeleccionado:
        messagebox.showwarning("Atención", "Selecciona el archivo cifrado.")
        return
    clave = entradaClave.get()
    if not clave:
        messagebox.showwarning("Atención", "Debes ingresar una clave.")
        return
    resultado = descifrarVigenere(archivoSeleccionado, clave)
    messagebox.showinfo("Resultado", resultado)

def cifrarFernetDesdeGui():
    """
    Ejecuta cifrado Fernet desde la interfaz.
    """
    if not archivoSeleccionado:
        messagebox.showwarning("Atención", "Debes seleccionar un archivo primero.")
        return
    resultado = cifrarFernet(archivoSeleccionado)
    messagebox.showinfo("Resultado", resultado)

def descifrarFernetDesdeGui():
    """
    Ejecuta descifrado Fernet desde la interfaz.
    """
    if not archivoSeleccionado:
        messagebox.showwarning("Atención", "Selecciona un archivo .cif.")
        return
    if not archivoSeleccionado.endswith(".cif"):
        messagebox.showwarning("Atención", "Solo puedes descifrar archivos con extensión .cif.")
        return
    resultado = descifrarFernet(archivoSeleccionado)
    messagebox.showinfo("Resultado", resultado)

def interfazPrincipal():
    """
    Crea la ventana principal con botones y campos necesarios.
    """
    global etiquetaRuta, entradaClave

    ventana = tk.Tk()
    ventana.title("Sistema de Cifrado")
    ventana.geometry("600x550")
    ventana.configure(bg=COLORFONDO)
    ventana.resizable(False, False)

    contenedor = tk.Frame(ventana, bg=COLORCONTENEDOR, padx=30, pady=30)
    contenedor.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Título
    tk.Label(
        contenedor,
        text="Sistema de Cifrado de Archivos",
        font=("Baskerville Old Face", 20, "bold"),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    ).pack(pady=(0, 20))

    # Botón Seleccionar Archivo
    tk.Button(
        contenedor,
        text="Seleccionar archivo",
        font=("Baskerville Old Face", 12),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=seleccionarArchivo,
        relief="flat"
    ).pack(pady=10, fill="x")

    # Mostrar ruta del archivo
    etiquetaRuta = tk.Label(
        contenedor,
        text="Ningún archivo seleccionado",
        font=("Baskerville Old Face", 10),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    )
    etiquetaRuta.pack(pady=(5, 15))

    # Campo clave Vigenère
    tk.Label(
        contenedor,
        text="Clave para Vigenère:",
        font=("Baskerville Old Face", 12, "bold"),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    ).pack()

    entradaClave = tk.Entry(
        contenedor,
        font=("Baskerville Old Face", 12),
        width=30
    )
    entradaClave.pack(pady=(0, 15))

    # Botones Vigenère
    tk.Button(
        contenedor,
        text="Cifrar Vigenère",
        font=("Baskerville Old Face", 14),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=cifrarVigenereDesdeGui,
        relief="flat"
    ).pack(pady=5, fill="x")

    tk.Button(
        contenedor,
        text="Descifrar Vigenère",
        font=("Baskerville Old Face", 14),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=descifrarVigenereDesdeGui,
        relief="flat"
    ).pack(pady=5, fill="x")

    # Botones Fernet
    tk.Button(
        contenedor,
        text="Cifrar Fernet",
        font=("Baskerville Old Face", 14),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=cifrarFernetDesdeGui,
        relief="flat"
    ).pack(pady=10, fill="x")

    tk.Button(
        contenedor,
        text="Descifrar Fernet",
        font=("Baskerville Old Face", 14),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=descifrarFernetDesdeGui,
        relief="flat"
    ).pack(pady=5, fill="x")

    # Botón salir
    tk.Button(
        contenedor,
        text="Salir",
        font=("Baskerville Old Face", 12),
        bg=COLORALERTA,
        fg=COLORTEXTO,
        command=ventana.destroy,
        relief="flat"
    ).pack(pady=15, fill="x")

    ventana.mainloop()

# Ejecución principal
if __name__ == "__main__":
    interfazPrincipal()