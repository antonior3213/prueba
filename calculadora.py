"""Calcula la nota según las respuestas del estudiante."""

try:
    correctas = int(input("Número de respuestas correctas: "))
    incorrectas = int(input("Número de respuestas incorrectas: "))
    en_blanco = int(input("Número de respuestas en blanco: "))

    if min(correctas, incorrectas, en_blanco) < 0:
        print("Error: las cantidades no pueden ser negativas.")
    else:
        nota_final = correctas * 5 - incorrectas
        print("La nota final del estudiante es:", nota_final)
except ValueError:
    print("Error: introduce cantidades enteras válidas.")
