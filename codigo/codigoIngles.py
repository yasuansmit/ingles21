import math

def main():
    opcion = 0
    resultados = {} 

    while opcion != 7:
        print("Selecciona la operación que deseas realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Raíz Cuadrada")
        print("6. Verificar si un número es primo")
        print("7. Salir")
        print("8. Ver resultados anteriores")

        opcion = int(input("Ingresa el número de la operación: "))