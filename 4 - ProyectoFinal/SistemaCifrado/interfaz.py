#Importacion de libererias
import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox
from main import ejecutarVigenere
from mainFernet import ejecutarFernet

# Asegurar que la carpeta de logs exista
os.makedirs("logs", exist_ok=True)

# Configurar el logger para registrar errores
logging.basicConfig(
    filename='logs/error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Paleta de colores personalizada para la interfaz
COLORFONDO = "#455372"
COLORCONTENEDOR = "#336699"
COLORBOTON = "#FFFFF0"
COLORTEXTO = "#FFFFF0"
COLORALERTA = "#CC3333"

# Variable global para almacenar la ruta del archivo seleccionado
archivoSeleccionado = ""

def seleccionarArchivo():
    "Abre una ventana de diálogo para que el usuario seleccione un archivo."
    "Actualiza la etiqueta de ruta con la ubicación del archivo."
    
    global archivoSeleccionado
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=[
            ("Archivos de texto", "*.txt"),
            ("Documentos PDF", "*.pdf"),
            ("Documentos Word", "*.docx")
        ]
    )
    if ruta:
        archivoSeleccionado = ruta
        etiquetaRuta.config(text=f"Archivo: {ruta}")

def ejecutarVigenereDesdeGui():
    "Ejecuta el cifrado y descifrado usando el algoritmo Vigenère con la clave proporcionada por el usuario."

    if not archivoSeleccionado:
        messagebox.showwarning("Atención", "Debes seleccionar un archivo primero.")
        return

    clave = entradaClave.get()
    if not clave:
        messagebox.showwarning("Atención", "Debes ingresar una clave para Vigenère.")
        return

    resultado = ejecutarVigenere(archivoSeleccionado, clave)
    messagebox.showinfo("Resultado", resultado)

def ejecutarFernetDesdeGui():
    " Ejecuta el cifrado y descifrado usando el algoritmo Fernet sin necesidad de clave proporcionada por el usuario."
    
    if archivoSeleccionado:
        resultado = ejecutarFernet(archivoSeleccionado)
        messagebox.showinfo("Resultado", resultado)
    else:
        messagebox.showwarning("Atención", "Debes seleccionar un archivo primero.")

def interfazPrincipal():
    " Crea e inicia la interfaz gráfica del sistema de cifrado. Permite al usuario seleccionar archivos y aplicar los algoritmos de cifrado."
    
    global etiquetaRuta, entradaClave

    # Configuración general de la ventana
    ventana = tk.Tk()
    ventana.title("Sistema de Cifrado")
    ventana.geometry("550x500")
    ventana.configure(bg=COLORFONDO)
    ventana.resizable(False, False)

    # Contenedor principal para los elementos
    contenedor = tk.Frame(ventana, bg=COLORCONTENEDOR, padx=30, pady=30)
    contenedor.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Título del sistema
    tk.Label(
        contenedor,
        text="Sistema de Cifrado",
        font=("Baskerville Old Face", 20, "bold"),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    ).pack(pady=(0, 20))

    # Botón para seleccionar un archivo
    tk.Button(
        contenedor,
        text="Seleccionar archivo",
        font=("Baskerville Old Face", 12),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=seleccionarArchivo,
        relief="flat"
    ).pack(pady=10, fill="x")

    # Etiqueta que muestra la ruta del archivo seleccionado
    etiquetaRuta = tk.Label(
        contenedor,
        text="Ningún archivo seleccionado",
        font=("Baskerville Old Face", 10),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    )
    etiquetaRuta.pack(pady=(5, 15))

    # Etiqueta para la entrada de clave Vigenère
    tk.Label(
        contenedor,
        text="Clave Vigenère:",
        font=("Baskerville Old Face", 12, "bold"),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    ).pack()

    # Campo de entrada para la clave Vigenère
    entradaClave = tk.Entry(
        contenedor,
        font=("Baskerville Old Face", 12),
        width=30
    )
    entradaClave.pack(pady=(0, 15))

    # Botón para ejecutar Vigenère
    tk.Button(
        contenedor,
        text="Cifrado Vigenère",
        font=("Baskerville Old Face", 14),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=ejecutarVigenereDesdeGui,
        relief="flat"
    ).pack(pady=10, fill="x")

    # Botón para ejecutar Fernet
    tk.Button(
        contenedor,
        text="Cifrado Fernet",
        font=("Baskerville Old Face", 14),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=ejecutarFernetDesdeGui,
        relief="flat"
    ).pack(pady=10, fill="x")

    # Botón para cerrar la aplicación
    tk.Button(
        contenedor,
        text="Salir",
        font=("Baskerville Old Face", 12),
        bg=COLORALERTA,
        fg=COLORTEXTO,
        command=ventana.destroy,
        relief="flat"
    ).pack(pady=10, fill="x")

    # Inicia el bucle de eventos
    ventana.mainloop()

# Punto de entrada de la aplicación
if __name__ == "__main__":
    interfazPrincipal()