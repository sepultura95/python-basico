contactos = {}

def mostrar_menu():
    print("\nMENÚ contactos")
    print("1. Agregar contactos")
    print("2. Ver contactos")
    print("3. Buscar contactos")
    print("4. Salir")

def agregar_contactos():
    nombre = input("Nombre: ")
    telefono = input("Telefono")
    contactos[nombre] = telefono
    print("contactos guardado")

def ver_contactos():
    for nombre, telefono in contactos.items():
        print(nombre, ":", telefono)

def buscar_contactos():
    buscar = input("Nombre a buscar: ")
    if buscar in contactos:
        print("telefono:", contactos[buscar])
    else:
        print("contactos no encontrado")

while True:
    mostrar_menu()
    opcion = input("elige una opcion: ")

    if opcion == "1":
        agregar_contactos()
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        buscar_contactos()
    elif opcion == "4":
        print("saliendo...")
        break
    else:
        print("opcion no valida")