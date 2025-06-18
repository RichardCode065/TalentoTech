import tkinter as tk

ventana = tk.Tk()
ventana.title("Prueba Tkinter")
ventana.geometry("300x200")
tk.Label(ventana, text="¡Hola, interfaz!").pack(pady=40)
ventana.mainloop()
