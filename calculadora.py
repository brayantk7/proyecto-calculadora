# calculadora.py - VERSIÓN GRÁFICA (GUI)
import tkinter as tk

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

# --- Configuración de la Ventana ---
window = tk.Tk()
window.title("Calculadora")
window.resizable(False, False) # Evita que se cambie el tamaño

# --- Pantalla (Display) ---
# Un campo de texto donde aparecen los números
display = tk.Entry(window, width=20, font=("Arial", 20), justify="right", bd=5)
display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# --- Botones ---
# Definimos los botones en una lista de listas (como una cuadrícula)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

# Creamos los botones numéricos y de operación
for (text, row, col) in buttons:
    btn = tk.Button(window, text=text, font=("Arial", 14), width=5, height=2,
                    command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, padx=2, pady=2)

# Botón de Limpiar (C)
btn_clear = tk.Button(window, text='C', font=("Arial", 14), width=5, height=2, command=clear_display)
btn_clear.grid(row=4, column=3, padx=2, pady=2)

# Botón de Igual (=)
btn_equal = tk.Button(window, text='=', font=("Arial", 14), width=23, height=2, command=calculate_result)
btn_equal.grid(row=5, column=0, columnspan=4, padx=5, pady=5)


# --- Iniciar la App ---
window.mainloop()