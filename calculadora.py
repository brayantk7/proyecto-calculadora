# calculadora.py

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

        print(f"Procesando: {num1_str} {op} {num2_str}...")
        # La lógica de cálculo vendrá después
        print("Resultado: [CÁLCULO PENDIENTE]")
        print("-----------------------------")

# Iniciar el programa
if __name__ == "__main__":
    main()