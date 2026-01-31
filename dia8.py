while True:
    print("\nMENÚ contactos")
    print("1. Agregar contactos")
    print("2. ver contactos")
    print("3. Buscar contactos")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1": 
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        contactos = {}
        contactos[nombre] = telefono
        print("Contactos guardado")

    elif opcion == "2":
        if len(contactos) == 0:
            print("No hay contacto")
        else:
            for nombre, telefono in contactos.items():
                print(nombre, "->", telefono)

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        if nombre in contactos:
            print("Teléfono:", contactos[nombre])
        else:
            print("Contacto no encontrado")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")    