# calculadora.py - VERSIÓN GRÁFICA (GUI) v2.0
import tkinter as tk

# --- Colores y Fuentes ---
COLOR_FONDO = "#f0f0f0"
COLOR_DISPLAY = "#ffffff"
COLOR_BOTON_NUM = "#e0e0e0"
COLOR_BOTON_OP = "#ff9500" # Naranja para operadores
COLOR_BOTON_ESP = "#d4d4d2" # Gris claro para C y =
FUENTE_DISPLAY = ("Arial", 28)
FUENTE_BOTON = ("Arial", 14)

# --- Lógica ---
def on_button_click(char):
    """Añade el carácter presionado a la pantalla."""
    display.insert(tk.END, char)

def clear_display():
    """Borra la pantalla."""
    display.delete(0, tk.END)

def calculate_result():
    """Calcula la expresión en la pantalla."""
    try:
        # 'eval' toma el texto (ej. "5*2") y lo calcula
        result = eval(display.get())
        clear_display()
        display.insert(0, str(result))
    except Exception:
        clear_display()
        display.insert(0, "Error")

# --- Handlers de Teclado ---
def on_key_press(event):
    """Maneja las pulsaciones de teclado."""
    if event.keysym == "Return": # keysym es el nombre de la tecla
        calculate_result()
    elif event.keysym == "Escape":
        clear_display()

# --- Configuración de la Ventana ---
window = tk.Tk()
window.title("Calculadora")
window.resizable(False, False)
window.configure(bg=COLOR_FONDO)

# --- Pantalla (Display) ---
display = tk.Entry(window, width=16, font=FUENTE_DISPLAY, justify="right", bd=0, 
                   bg=COLOR_DISPLAY, relief="solid", borderwidth=1)
display.grid(row=0, column=0, columnspan=4, pady=20, padx=20, ipady=10) # ipady = alto interno

# --- Botones ---
buttons = [
    ('7', 1, 0, COLOR_BOTON_NUM), ('8', 1, 1, COLOR_BOTON_NUM), ('9', 1, 2, COLOR_BOTON_NUM), ('/', 1, 3, COLOR_BOTON_OP),
    ('4', 2, 0, COLOR_BOTON_NUM), ('5', 2, 1, COLOR_BOTON_NUM), ('6', 2, 2, COLOR_BOTON_NUM), ('*', 2, 3, COLOR_BOTON_OP),
    ('1', 3, 0, COLOR_BOTON_NUM), ('2', 3, 1, COLOR_BOTON_NUM), ('3', 3, 2, COLOR_BOTON_NUM), ('-', 3, 3, COLOR_BOTON_OP),
    ('0', 4, 0, COLOR_BOTON_NUM), ('.', 4, 1, COLOR_BOTON_NUM), ('+', 4, 2, COLOR_BOTON_OP)
]

for (text, row, col, color) in buttons:
    # 'relief="flat"' quita el borde 3D feo
    btn = tk.Button(window, text=text, font=FUENTE_BOTON, width=5, height=2,
                    command=lambda t=text: on_button_click(t), bg=color, relief="flat")
    btn.grid(row=row, column=col, padx=5, pady=5)

# Botón de Limpiar (C)
btn_clear = tk.Button(window, text='C', font=FUENTE_BOTON, width=5, height=2, 
                      command=clear_display, bg=COLOR_BOTON_ESP, relief="flat")
btn_clear.grid(row=4, column=3, padx=5, pady=5)

# Botón de Igual (=)
btn_equal = tk.Button(window, text='=', font=FUENTE_BOTON, width=23, height=2, 
                      command=calculate_result, bg=COLOR_BOTON_OP, relief="flat")
btn_equal.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# --- Binds de Teclado (NUEVO) ---
window.bind("<Key>", on_key_press) # Llama a 'on_key_press' con CUALQUIER tecla

# --- Iniciar la App ---
window.mainloop()