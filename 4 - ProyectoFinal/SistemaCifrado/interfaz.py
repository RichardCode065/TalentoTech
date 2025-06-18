import tkinter as tk
from tkinter import filedialog, messagebox
from main import ejecutarVigenere
from mainFernet import ejecutarFernet

# Paleta de colores
COLORFONDO = "#455372"
COLORCONTENEDOR = "#336699"
COLORBOTON = "#FFFFF0"
COLORTEXTO = "#FFFFF0"
COLORALERTA = "#CC3333"

archivoSeleccionado = ""

def seleccionarArchivo():
    global archivoSeleccionado
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Documentos PDF", "*.pdf"), ("Documentos Word", "*.docx")]
    )
    if ruta:
        archivoSeleccionado = ruta
        etiquetaRuta.config(text=f"Archivo: {ruta}")

def ejecutarVigenereDesdeGui():
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
    if archivoSeleccionado:
        ejecutarFernet(archivoSeleccionado)
        messagebox.showinfo("Éxito", "Cifrado y Descifrado Fernet completado.")
    else:
        messagebox.showwarning("Atención", "Debes seleccionar un archivo primero.")

def interfazPrincipal():
    global etiquetaRuta, entradaClave
    ventana = tk.Tk()
    ventana.title("Sistema de Cifrado")
    ventana.geometry("550x500")
    ventana.configure(bg=COLORFONDO)
    ventana.resizable(False, False)

    contenedor = tk.Frame(ventana, bg=COLORCONTENEDOR, padx=30, pady=30)
    contenedor.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Título
    titulo = tk.Label(
        contenedor,
        text="Sistema de Cifrado",
        font=("Baskerville Old Face", 20, "bold"),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    )
    titulo.pack(pady=(0, 20))

    # Botón para seleccionar archivo
    botonSeleccionar = tk.Button(
        contenedor,
        text="Seleccionar archivo",
        font=("Baskerville Old Face", 12),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=seleccionarArchivo,
        relief="flat"
    )
    botonSeleccionar.pack(pady=10, fill="x")

    etiquetaRuta = tk.Label(
        contenedor,
        text="Ningún archivo seleccionado",
        font=("Baskerville Old Face", 10),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    )
    etiquetaRuta.pack(pady=(5, 15))

    # Entrada para clave Vigenère
    etiquetaClave = tk.Label(
        contenedor,
        text="Clave Vigenère:",
        font=("Baskerville Old Face", 12, "bold"),
        bg=COLORCONTENEDOR,
        fg=COLORTEXTO
    )
    etiquetaClave.pack()

    entradaClave = tk.Entry(
        contenedor,
        font=("Baskerville Old Face", 12),
        width=30
    )
    entradaClave.pack(pady=(0, 15))

    # Botón cifrado Vigenère
    botonVigenere = tk.Button(
        contenedor,
        text="Cifrado Vigenère",
        font=("Baskerville Old Face", 14),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=ejecutarVigenereDesdeGui,
        relief="flat"
    )
    botonVigenere.pack(pady=10, fill="x")

    # Botón cifrado Fernet
    botonFernet = tk.Button(
        contenedor,
        text="Cifrado Fernet",
        font=("Baskerville Old Face", 14),
        bg=COLORBOTON,
        fg=COLORFONDO,
        command=ejecutarFernetDesdeGui,
        relief="flat"
    )
    botonFernet.pack(pady=10, fill="x")

    # Botón salir
    botonSalir = tk.Button(
        contenedor,
        text="Salir",
        font=("Baskerville Old Face", 12),
        bg=COLORALERTA,
        fg=COLORTEXTO,
        command=ventana.destroy,
        relief="flat"
    )
    botonSalir.pack(pady=10, fill="x")

    ventana.mainloop()

if __name__ == "__main__":
    interfazPrincipal()
