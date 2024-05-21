import math

def main():
    opcion = 0
    resultados = {}  # Diccionario para almacenar resultados de operaciones

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

        if opcion in [1, 2, 3, 4, 5, 6]:
            resultado = realizar_operacion(opcion)
            resultados[opcion] = resultado
        elif opcion == 7:
            print("Saliendo del programa...")
        elif opcion == 8:
            ver_resultados(resultados)
        else:
            print("Opción no válida. Por favor selecciona una opción válida.")

def realizar_operacion(opcion):
    if opcion == 1:
        return realizar_suma()
    elif opcion == 2:
        return realizar_resta()
    elif opcion == 3:
        return realizar_multiplicacion()
    elif opcion == 4:
        return realizar_division()
    elif opcion == 5:
        return calcular_raiz_cuadrada()
    elif opcion == 6:
        return verificar_primo()

def realizar_suma():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
    return resultado

def realizar_resta():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
    return resultado

def realizar_multiplicacion():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
    return resultado

def realizar_division():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
        return resultado
    else:
        print("No es posible dividir por cero.")
        return None

def calcular_raiz_cuadrada():
    num = int(input("Ingresa el número para calcular su raíz cuadrada: "))
    if num >= 0:
        resultado = math.sqrt(num)
        print("La raíz cuadrada de", num, "es:", resultado)
        return resultado
    else:
        print("No es posible calcular la raíz cuadrada de un número negativo.")
        return None

def verificar_primo():
    num = int(input("Ingresa un número para verificar si es primo: "))
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print(num, "no es primo.")
                return False
        else:
            print(num, "es primo.")
            return True
    else:
        print(num, "no es primo.")
        return False

def ver_resultados(resultados):
    if resultados:
        print("Resultados anteriores:")
        for operacion, resultado in resultados.items():
            print(f"Operación {operacion}: {resultado}")
    else:
        print("No hay resultados anteriores.")

if  "_main_":
    main()