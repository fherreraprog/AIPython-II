#Este script será una pequeña aplicación de consola para gestionar una lista de estudiantes,
#permitiendo agregar, eliminar y mostrar información de los estudiantes. Además,
#incluirá la funcionalidad de calcular la edad promedio de los estudiantes.

def agregar_estudiante(estudiantes, nombre, edad, ciudad="Desconocida"):
    """Agrega un estudiante a la lista de estudiantes."""
    estudiantes.append([nombre, edad, ciudad])
    print(f"Estudiante {nombre} agregado exitosamente")


def mostrar_estudiantes(estudiantes):
    """Muestra todos los estudiantes con su información."""
    print(f"Total de estudiantes: {len(estudiantes)}")
    i = 1
    for estudiante in estudiantes:
        print(f"Estudiante {i}: {estudiante[0]}, Edad: {estudiante[1]}, Ciudad: {estudiante[2]}")
        print(f"Tipo de dato: {type(estudiante)}, ID: {id(estudiante)}")
        i += 1

def calcular_edad_promedio(estudiantes):
    """Calcula y muestra la edad promedio de los estudiantes."""
    if not estudiantes:
        print("No hay estudiantes para calcular el promedio.")
        return
    total_edad = sum(estudiante[1] for estudiante in estudiantes)
    promedio = total_edad / len(estudiantes)
    print(f"Edad promedio de los estudiantes: {promedio:.2f}")


def eliminar_estudiante(estudiantes, nombre):
    """Elimina un estudiante de la lista por su nombre."""
    for i in range(len(estudiantes)):
        if estudiantes[i][0].lower() == nombre.lower():
            del estudiantes[i]
            return f"Estudiante {nombre} eliminado exitosamente."
    return f"Estudiante {nombre} no encontrado."


def main():
    """Función principal que maneja la interacción del usuario con el sistema."""
    print("Bienvenido al Sistema de Gestión de Estudiantes")
    print("Para salir del programa, ingresa 'salir' en cualquier momento.\n")

    estudiantes = []  # Lista mutable para almacenar estudiantes

    while True:
        accion = input("¿Quieres agregar, eliminar o mostrar estudiantes? (salir para terminar): ")
        if accion.lower() == "salir":
            break
        elif accion.lower() == "agregar":
            nombre = input("Ingresa el nombre del estudiante: ")
            edad = int(input("Ingresa la edad del estudiante: "))
            ciudad = input("Ingresa la ciudad del estudiante (opcional): ")
            if not ciudad:
                agregar_estudiante(estudiantes, nombre, edad)
            else:
                agregar_estudiante(estudiantes, nombre, edad, ciudad)
            print(f"Estudiante agregado: Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
            if len(estudiantes) > 5:
                print("Ya hay más de 5 estudiantes en la lista.")
        elif accion.lower() == "eliminar":
            nombre = input("Ingresa el nombre del estudiante a eliminar: ")
            print(eliminar_estudiante(estudiantes, nombre))
        elif accion.lower() == "mostrar":
            mostrar_estudiantes(estudiantes)
            calcular_edad_promedio(estudiantes)
        else:
            print("Acción no válida. Por favor, elige entre agregar, eliminar o mostrar.")

    print("Lista de todos los estudiantes:")
    mostrar_estudiantes(estudiantes)
    calcular_edad_promedio(estudiantes)
    if len(estudiantes) > 3:
        print("Primeros tres estudiantes:")
        for estudiante in estudiantes[:3]:
            print(estudiante)

    print("Programa terminado.")


if __name__ == "__main__":
    main()
