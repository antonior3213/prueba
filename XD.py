"""Calcula la nota media de un estudiante."""

try:
    cantidad = int(input("¿Cuántas notas quieres promediar? "))

    if cantidad <= 0:
        print("Debes introducir al menos una nota.")
    else:
        suma = 0.0

        for numero in range(1, cantidad + 1):
            nota = float(input(f"Introduce la nota {numero}: "))
            suma += nota

        media = suma / cantidad
        print(f"La nota media es: {media:.2f}")
except ValueError:
    print("Error: introduce números válidos.")
