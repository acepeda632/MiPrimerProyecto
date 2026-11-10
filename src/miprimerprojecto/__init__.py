def main() -> None:
    try:
        limite = int(input("Introduce un número entre 0 y 100: "))
    except ValueError:
        print("Por favor, introduce un número entero.")
        return

    if not 0 <= limite <= 100:
        print("El número debe estar entre 0 y 100.")
        return

    cantidad = sum(1 for numero in range(limite + 1) if numero % 2 == 0)
    sustantivo = "número par" if cantidad == 1 else "números pares"
    print(f"Hay {cantidad} {sustantivo} entre 0 y {limite}, inclusive.")
