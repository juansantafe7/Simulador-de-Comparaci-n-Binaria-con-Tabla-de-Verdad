print("Conversor de numeros base 10 a otro sistemas numérico")
# 1. Ingreso de datos
numero_a_convertir = (input("Ingrese un numero entero:\n"))

# 2. Validación
while not (numero_a_convertir.isdigit() or (numero_a_convertir[0] == "-" and numero_a_convertir[1:].isdigit())):
    numero_a_convertir = input("Error: Por favor, ingresa un número entero válido:\n")


# 3. Selector de conversor
print("Ingresa el numero de la opción a la que quieres convertir")
print("1) Base 2")
print("2) Base 8")
print("3) Base 16")
opcion_a_convertir = int(input(""))

while opcion_a_convertir != 1 and opcion_a_convertir != 2 and opcion_a_convertir != 3:
   print("La opción ingresada es incorrecta")
   opcion_a_convertir = int(input("Ingrese 1, 2 o 3:\n"))
   
numero_a_convertir = int(numero_a_convertir) 

# 4. Conversion a bianrio (Fabricio)
if opcion_a_convertir == 1:
    print("=== Conversión manual de entero a binario ===\n")
    if numero_a_convertir == 0:
        print("El binario de 0 es: 0")
    elif numero_a_convertir < 0:
        binario = ""
        numero_a_convertir = -numero_a_convertir  # lo pasamos a positivo para operar

        while numero_a_convertir > 0:
            residuo = numero_a_convertir % 2
            binario = str(residuo) + binario
            numero_a_convertir = numero_a_convertir // 2

        binario = "-" + binario  # Agregamos el signo negativo al resultado
        print("El número binario equivalente es:", binario)
    else:
        binario = ""
        while numero_a_convertir > 0:
            residuo = numero_a_convertir % 2
            binario = str(residuo) + binario
            numero_a_convertir = numero_a_convertir // 2
        print("El número binario equivalente es:", binario)
        
# 5. Conversion a hexadecimal (Gabi)

# 6. Conversion a Octal (Juan)

# 7. Mostrar resultado



