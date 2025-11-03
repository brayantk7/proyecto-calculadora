# calculadora.py

def calcular(num1, op, num2):
    """Realiza el cálculo basado en la operación."""
    try:
        n1 = float(num1)
        n2 = float(num2)
    except ValueError:
        return "[Error: Entrada no válida]"

    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            return "[Error: División por cero]"
        return n1 / n2
    else:
        return "[Error: Operador no válido]"

def mostrar_menu():
    """Muestra el menú de la calculadora."""
    print("\n--- Calculadora Simple ---")
    print("Operaciones disponibles:")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("Escribe 'salir' para terminar.")

def main():
    """Función principal de la aplicación."""
    while True:
        mostrar_menu()
        num1_str = input("Ingresa el primer número: ")
        if num1_str == 'salir':
            break

        op = input("Ingresa la operación (+, -, *, /): ")
        if op == 'salir':
            break

        num2_str = input("Ingresa el segundo número: ")
        if num2_str == 'salir':
            break

        resultado = calcular(num1_str, op, num2_str)
        print(f"Resultado: {resultado}")
        print("-----------------------------")

# Iniciar el programa
if __name__ == "__main__":
    main()