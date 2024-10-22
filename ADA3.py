postres = []
postres.append(["Pastel", "harina", "azúcar", "huevos"])
postres.append(["Helado", "leche", "azúcar", "vainilla"])
postres.append(["Galletas", "harina", "mantequilla", "chocolate"])

def existe_postre(postre_nombre):
    for postre in postres:
        if postre[0].lower() == postre_nombre.lower():
            return postre
    return None

def mostrar_menu():
    print("\nOpciones:")
    print("1. Mostrar ingredientes de un postre")
    print("2. Insertar nuevos ingredientes a un postre")
    print("3. Dar de alta un nuevo postre")
    print("4. Dar de baja un postre")
    print("5. Eliminar ingredientes de un postre")
    print("6. Mostrar todos los postres y sus ingredientes")
    print("7. Agregar un ingrediente a otro postre")
    print("8. Salir")

def mostrar_ingredientes():
    postre = input("Ingresa el nombre del postre: ")
    resultado = existe_postre(postre)
    if resultado:
        print(f"Ingredientes de {postre}: {resultado[1:]}")
    else:
        print(f"El postre {postre} no está en la lista.")

def insertar_ingredientes():
    postre = input("Ingresa el nombre del postre: ")
    resultado = existe_postre(postre)
    if resultado:
        nuevo_ingrediente = input("Ingresa el nuevo ingrediente: ")
        resultado.append(nuevo_ingrediente)
        print(f"Ingrediente {nuevo_ingrediente} agregado a {postre}.")
    else:
        print(f"El postre {postre} no está en la lista.")

def alta_postre():
    postre = input("Ingresa el nombre del nuevo postre: ")
    if not existe_postre(postre):
        ingredientes = input(f"Ingresa los ingredientes de {postre} separados por comas: ").split(",")
        postres.append([postre] + [ingrediente.strip() for ingrediente in ingredientes])
        print(f"Postre {postre} añadido con ingredientes {ingredientes}.")
    else:
        print(f"El postre {postre} ya existe.")

def baja_postre():
    postre = input("Ingresa el nombre del postre a eliminar: ")
    resultado = existe_postre(postre)
    if resultado:
        postres.remove(resultado)
        print(f"Postre {postre} eliminado.")
    else:
        print(f"El postre {postre} no está en la lista.")

def eliminar_ingrediente():
    postre = input("Ingresa el nombre del postre: ")
    resultado = existe_postre(postre)
    if resultado:
        ingrediente = input("Ingresa el nombre del ingrediente a eliminar: ")
        if ingrediente in resultado:
            resultado.remove(ingrediente)
            print(f"Ingrediente {ingrediente} eliminado de {postre}.")
        else:
            print(f"El ingrediente {ingrediente} no está en la lista de {postre}.")
    else:
        print(f"El postre {postre} no está en la lista.")

def mostrar_todos_postres():
    print("\nTodos los postres y sus ingredientes:")
    for postre in postres:
        print(f"{postre[0]}: {postre[1:]}")

def agregar_ingrediente_otro_postre():
    postre_origen = input("Ingresa el nombre del postre origen: ")
    resultado_origen = existe_postre(postre_origen)
    if resultado_origen:
        ingrediente = input("Ingresa el nombre del ingrediente a transferir: ")
        if ingrediente in resultado_origen:
            postre_destino = input("Ingresa el nombre del postre destino: ")
            resultado_destino = existe_postre(postre_destino)
            if resultado_destino:
                resultado_destino.append(ingrediente)
                print(f"Ingrediente {ingrediente} transferido de {postre_origen} a {postre_destino}.")
            else:
                print(f"El postre destino {postre_destino} no está en la lista.")
        else:
            print(f"El ingrediente {ingrediente} no está en la lista de {postre_origen}.")
    else:
        print(f"El postre origen {postre_origen} no está en la lista.")

while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ")
    if opcion == "1":
        mostrar_ingredientes()
    elif opcion == "2":
        insertar_ingredientes()
    elif opcion == "3":
        alta_postre()
    elif opcion == "4":
        baja_postre()
    elif opcion == "5":
        eliminar_ingrediente()
    elif opcion == "6":
        mostrar_todos_postres()
    elif opcion == "7":
        agregar_ingrediente_otro_postre()
    elif opcion == "8":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
