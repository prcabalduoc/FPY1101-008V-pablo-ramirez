def menuPrincipal():
    print("\n===[ MENÚ PRINCIPAL ]===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

maxLibros = 120
stockLibros = 120
historialPrestamos = 0

#Verificar que el usuario ingrese una opción válida del menú principal
while True:
    menuPrincipal()
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
        if opcion < 1 or opcion > 5:
            print("¡Opción inválida! Por favor, seleccione una opción entre 1 y 5.")
        else:
            
            #Opciones del menú principal
            if opcion == 1:
                print("\n===[ Libros Disponibles ]===")
                # Aquí se mostrarían los libros disponibles en la biblioteca
                print(f"Actualmente, hay {stockLibros} libros disponibles en la biblioteca.")
                
            elif opcion == 2:
                print("\n===[ Realizar Préstamo ]===")
                # Aquí se implementaría la lógica para realizar un préstamo de libro

                try:
                    numPrestamo = int(input("Ingrese el número de libros a prestar: "))
                except ValueError:
                    print("Error: Por favor, ingrese un número entero válido.")

                if numPrestamo < 1:
                    print("¡Número de libros inválido! Por favor, ingrese un número entero positivo.")
                elif numPrestamo > stockLibros:
                    print(f"¡No hay suficientes libros disponibles! Solo hay {stockLibros} libros en stock.")
                else:
                    stockLibros -= numPrestamo
                    historialPrestamos += 1
                    print(f"¡Préstamo realizado con éxito! Quedan {stockLibros} libros disponibles en la biblioteca.")

            elif opcion == 3:
                print("\n===[ Devolver Préstamo ]===")
                # Aquí se implementaría la lógica para devolver un libro prestado

                try:
                    numDevolucion = int(input("Ingrese el número de libros a devolver: "))
                except ValueError:
                    print("Error: Por favor, ingrese un número entero válido.")

                if numDevolucion < 1:
                    print("No puede devolver menos de 1 libro.")
                elif stockLibros + numDevolucion > maxLibros:
                    print(f"¡Error! No se pueden devolver más de {maxLibros - stockLibros} libros, ya que el stock máximo es de {maxLibros}.")
                else:
                    stockLibros += numDevolucion
                    historialPrestamos -= 1
                    print(f"¡Devolución realizada con éxito! Ahora hay {stockLibros} libros disponibles en la biblioteca.")

            elif opcion == 4:
                print("\n===[ Historial de Préstamos ]===")
                # Aquí se mostraría el historial de préstamos realizados por el usuario
                print(f"Total de préstamos realizados: {historialPrestamos}")

            elif opcion == 5:
                print("\n¡Gracias por usar el sistema de biblioteca! ¡Hasta luego!\n")
                break
            
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido para seleccionar una opción.")