"""Convierte una temperatura de grados Celsius a Fahrenheit."""

try:
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F.")
except ValueError:
    print("Error: introduce un número válido.")
