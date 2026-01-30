def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except:
        return "Error: No se puede dividir por cero"

print("=== CALCULADORA PRO MAX ===")

while True:
    print("\nMenú:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "5":
        print("Saliendo...")
        break

    num1 = float(input("Primero número: "))
    num2 = float(input("Segundo número: "))

    if opcion == "1":
        print("Resultado:", sumar(num1,num2))

    elif opcion == "2":
        print("Resultado:", restar(num1, num2))

    elif opcion == "3":
        print("resultado:", multiplicar(num1,num2))
    
    elif opcion == "4":
        print("Resultado:", dividir(num1,num2))

    else:
        print("Opcion inválida")