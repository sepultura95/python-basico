print("=== CALCULADORA PRO ===")

while True:
    print("\nMenú:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("saliendo del programa...")
        break

    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    if opcion == "1":
        print("Resultado:", num1 + num2)

    elif opcion == "2":
        print("Resultado", num1 - num2)

    elif opcion == "3":
        print("Resultado", num1 * num2)

    elif opcion == "4":
        print("Resultado", num1 / num2)

    else:
        print("Opción inválida")