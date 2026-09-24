# Proyecto Calculadora - Módulo de funciones principales
def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def main():
    try:
        try:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
        except ValueError:
            raise ValueError("Debe ingresar solamente valores numericos.")

        print("\nSeleccione una operacion:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            resultado = suma(a, b)
        elif opcion == "2":
            resultado = resta(a, b)
        elif opcion == "3":
            resultado = multiplicacion(a, b)
        elif opcion == "4":
            resultado = division(a, b)
        else:
            raise ValueError("La operacion seleccionada no existe.")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    except ValueError as error:
        print("Error:", error)
    else:
        print("El resultado es:", resultado)
    finally:
        print("Ejecucion finalizada.")


if __name__ == "__main__":
    main()