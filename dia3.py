print("=== CALCULADORA BÁSICA ===")

num1 = float(input("primer número: "))
num2 = float(input("segundo número: "))

print("Operaciones:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicaión")
print("4. Division")

opcion = input("Elige una opción (1/2/3/4): ")

if opcion == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif opcion == "2":
    resultado == num1 - num2
    print("Resultado:", resultado)

elif opcion == "3":
    resultado = num1 * num2
    print("Resultado", resultado)

elif opcion == "4":
    resultado == num1 / num2
    print("Resultado", resultado)

else:
    print("Opción no válida")