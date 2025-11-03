import tkinter as tk

COLOR_FONDO = "#f0f0f0"
COLOR_DISPLAY = "#ffffff"
COLOR_BOTON_NUM = "#e0e0e0"
COLOR_BOTON_OP = "#ff9500"
COLOR_BOTON_ESP = "#d4d4d2"
FUENTE_DISPLAY = ("Arial", 28)
FUENTE_BOTON = ("Arial", 14)

def on_button_click(char):
    display.insert(tk.END, char)

def clear_display():
    display.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(display.get())
        clear_display()
        display.insert(0, str(result))
    except Exception:
        clear_display()
        display.insert(0, "Error")

def on_key_press(event):
    key = event.keysym
    char = event.char

    if key == "Return":
        calculate_result()
    elif key == "Escape":
        clear_display()
    elif char in "0123456789+-*/.":
        on_button_click(char)
    else:
        pass
    
    return "break"

window = tk.Tk()
window.title("Calculadora")
window.resizable(False, False)
window.configure(bg=COLOR_FONDO)

display = tk.Entry(window, width=16, font=FUENTE_DISPLAY, justify="right", bd=0, 
                   bg=COLOR_DISPLAY, relief="solid", borderwidth=1)
display.grid(row=0, column=0, columnspan=4, pady=20, padx=20, ipady=10, sticky="ew")

buttons = [
    ('7', 1, 0, COLOR_BOTON_NUM), ('8', 1, 1, COLOR_BOTON_NUM), ('9', 1, 2, COLOR_BOTON_NUM), ('/', 1, 3, COLOR_BOTON_OP),
    ('4', 2, 0, COLOR_BOTON_NUM), ('5', 2, 1, COLOR_BOTON_NUM), ('6', 2, 2, COLOR_BOTON_NUM), ('*', 2, 3, COLOR_BOTON_OP),
    ('1', 3, 0, COLOR_BOTON_NUM), ('2', 3, 1, COLOR_BOTON_NUM), ('3', 3, 2, COLOR_BOTON_NUM), ('-', 3, 3, COLOR_BOTON_OP),
    ('0', 4, 0, COLOR_BOTON_NUM), ('.', 4, 1, COLOR_BOTON_NUM), ('+', 4, 2, COLOR_BOTON_OP)
]

for (text, row, col, color) in buttons:
    btn = tk.Button(window, text=text, font=FUENTE_BOTON, width=5, height=2,
                    command=lambda t=text: on_button_click(t), bg=color, relief="flat")
    btn.grid(row=row, column=col, padx=5, pady=5)

btn_clear = tk.Button(window, text='C', font=FUENTE_BOTON, width=5, height=2, 
                      command=clear_display, bg=COLOR_BOTON_ESP, relief="flat")
btn_clear.grid(row=4, column=3, padx=5, pady=5)

btn_equal = tk.Button(window, text='=', font=FUENTE_BOTON, width=23, height=2, 
                      command=calculate_result, bg=COLOR_BOTON_OP, relief="flat")
btn_equal.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

window.bind_all("<Key>", on_key_press)

window.mainloop()