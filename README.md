# TalentoTech
Bootcamp de Seguridad Informática de TALENTOTECH.


# 🔐 Proyecto de Criptografía en Python

Este repositorio contiene el desarrollo completo de un entrenamiento práctico en criptografía usando Python. A través de diferentes etapas y ejercicios, se abordan conceptos fundamentales como cifrado clásico (César y Vigenère), cifrado simétrico y asimétrico (Fernet, RSA), teoría de grafos aplicada a redes de comunicación, y programación de un sistema final con interfaz gráfica para cifrado y descifrado de documentos.

---

## 🎯 Objetivo General

Desarrollar un sistema completo que permita aplicar distintos algoritmos de cifrado (clásico y moderno), entendiendo su funcionamiento teórico y práctico, e integrando estos conocimientos mediante la programación en Python, el manejo de archivos y la documentación del proceso.

---

## 📁 Estructura del Proyecto

├── 1 - Entrenamiento/ # Introducción a programación y cifrados básicos
├── 2 - Experiencia/ # Aplicación de cifrados simétricos, asimétricos y teoría numérica
├── 3 - Conexion/ # Teoría de grafos aplicada a sistemas seguros
├── 4 - ProyectoFinal/
│ ├── Documentos/ # PDFs explicativos del proyecto
│ ├── SistemaCifrado/ # Código final con interfaz gráfica
│ └── requerimientos.txt # Librerías necesarias

---

## 📚 Contenidos del Proyecto

### 🧠 1. Entrenamiento
- Programas iniciales en Python: calculadoras, análisis de datos, conjuntos.
- Primer acercamiento a la criptografía: Cifrado de César y Vigenère.
- Juegos y lógica: Trivia y Ahorcado con análisis de frecuencia.

### 💻 2. Experiencia
- Implementación de RSA y llaves públicas/privadas.
- Cifrado simétrico y asimétrico.
- Firmas digitales.
- Conversión de texto a binario y decimal.

### 🔗 3. Conexión
- Implementación de grafos: adyacencia, accesibilidad y distancia.
- Aplicaciones en redes y seguridad de datos.

### 🏁 4. Proyecto Final
- Sistema de cifrado completo que incluye:
  - **Cifrado y descifrado Vigenère y Fernet**
  - **Lectura y escritura de archivos PDF, DOCX y TXT**
  - **Interfaz gráfica con Tkinter**
  - **Manejo de errores y logs**
  - **Documentación y modularización profesional**

---

## 🛠️ Tecnologías y Librerías

- `cryptography` (Fernet)
- `PyPDF2`, `reportlab` (PDF)
- `python-docx` (DOCX)
- `tkinter` (Interfaz gráfica)
- `logging`, `os` (manejo de archivos y errores)

Instalación con:

```bash
pip install -r requerimientos.txt
```


## Interfaz Gráfica
- Incluye una interfaz fácil de usar desarrollada en Tkinter, que permite:
- Seleccionar archivos PDF, DOCX o TXT
- Aplicar cifrado Vigenère (requiere clave)
- Aplicar cifrado Fernet (llave automática)
- Visualizar el estado de los archivos

## Autor
- David Ricardo Ordoñez Mora
- Estudiante de Ingeniería de Software y Computación
