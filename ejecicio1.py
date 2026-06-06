print("\n===[Bienvenidos al Sistema Médico]===")

#Ingresar total de médicos
while True:
    try:
        totalMedicos = int(input("\nIngrese el total de médicos: "))
        if totalMedicos < 0:
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
        else:
            break
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

#Inicializar contadores
medResidentes = 0
medEspecialistas = 0

for i in range(totalMedicos):

    # Solicitar nombre del médico
    while True:
        nombreMedico = input(f"\nIngrese el nombre del médico {i + 1}: (6 caracteres o más, No debe incluir espacios): ")
        if (len(nombreMedico) < 6) or (" " in nombreMedico):
            print("¡Registro médico inválido! El nombre del médico debe tener 6 caracteres o más y no contener espacios.")
        else:
            break
    
    # Solicitar años de experiencia del médico
    while True:
        try:
            anosExperiencia = int(input(f"Ingrese los años de experiencia del médico {i + 1}: "))
            if anosExperiencia < 0:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
            else:
                if anosExperiencia <= 5:
                    medResidentes += 1
                else:
                    medEspecialistas += 1
                break
        except ValueError:
            print("Error: Por favor, ingrese un número mayor a 0.")

print("\n===[Resultados del Registro Médico]===")
print("¡El hospital cuenta con:")
print(f"Residentes Junior: {medResidentes}")
print(f"Especialistas Senior: {medEspecialistas}")
print("¡Sistema listo para operar!\n")