"""Este programa utiliza un diccionario para almacenar los productos y sus cantidades en el inventario.
La variable nivel_minimo establece el nivel mínimo de inventario antes de que se emita una alerta.

La función imprimir_inventario() simplemente imprime el inventario actual en la consola.
La función actualizar_inventario() actualiza la cantidad de un producto en el inventario.

La función emitir_alerta() se llama si la cantidad actual es menor que el nivel mínimo establecido.
Esta función imprime una alerta en la consola que indica que el nivel de inventario para un producto determinado es bajo.

En el bucle principal del programa, se le pide al usuario que ingrese una opción (ver el inventario, actualizar el inventario o salir del programa).
 Si el usuario elige la opción de actualizar el inventario y la cantidad actual es menor que el nivel mínimo, se emite una alerta.

Este es solo un ejemplo básico de un programa de inventario en Python,
pero se puede personalizar y ampliar para adaptarlo a tus necesidades específicas."""


# Declaración de variables para los productos y sus cantidades
inventario = {
    "producto1": 10,
    "producto2": 15,
    "producto3": 5,
    "producto4": 20
}

# Establecer el nivel mínimo de inventario
nivel_minimo = 5

# Función para imprimir el inventario actual
def imprimir_inventario():
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

# Función para emitir una alerta si el nivel de inventario es bajo
def emitir_alerta(producto, cantidad):
    print(f"ALERTA: El nivel de inventario para {producto} es bajo. Cantidad actual: {cantidad}")

# Función para actualizar el inventario
def actualizar_inventario(producto, cantidad):
    inventario[producto] = cantidad

# Bucle para ejecutar el programa
while True:
    opcion = input("Ingrese una opción (1 para ver el inventario, 2 para actualizar el inventario, 3 para salir): ")

    # Opción para ver el inventario actual
    if opcion == "1":
        imprimir_inventario()

    # Opción para actualizar el inventario
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        actualizar_inventario(producto, cantidad)

        # Comprobar si la cantidad actual es menor que el nivel mínimo y emitir una alerta si es así
        if cantidad < nivel_minimo:
            emitir_alerta(producto, cantidad)

    # Opción para salir del programa
    elif opcion == "3":
        break

    # Opción inválida
    else:
        print("Opción inválida. Inténtelo de nuevo.")
