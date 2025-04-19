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
if opcion_a_convertir == 3:
   print(f"=== Conversión manual de entero {numero_a_convertir} a Hexadecimal  ===\n")
   if numero_a_convertir == 0:
      print(f"El número Hexadecimal equivalente es: 0")
   else:
        numero_negativo = False
        #Se evalua si el número ingresado es negativo, en caso de ser cierto se pasa a positivo para hacer la conversión.
        if numero_a_convertir < 0:
            numero_negativo = True
            numero_a_convertir = numero_a_convertir * -1
        #Se definen letras para valores especiales 10, 11, 12, 13, 14, 15
        letras =["A", "B", "C", "D", "E", "F"]
        numero_hexadecimal = ""
        #Ciclo While para evaluar cada número positivo
        while numero_a_convertir > 0:
            residuo = numero_a_convertir % 16
            if residuo < 10: 
                 digito = str(residuo)
            else:
                 digito = letras[residuo-10]
            numero_hexadecimal = digito + numero_hexadecimal
            numero_a_convertir = numero_a_convertir // 16
        if numero_negativo:
            numero_hexadecimal = "-" + numero_hexadecimal
        print(f"El número en hexadecimal equivalente es: {numero_hexadecimal}")

# 6. Conversion a Octal (Juan)

elif opcion_a_convertir == 2:
    print("=== Conversión manual de entero a octal ===\n")
    if numero_a_convertir == 0:
        print("El número octal de 0 es: 0")
    elif numero_a_convertir < 0:
        octal = ""
        numero_a_convertir = -numero_a_convertir

        while numero_a_convertir > 0:
            residuo = numero_a_convertir % 8
            octal = str(residuo) + octal
            numero_a_convertir = numero_a_convertir // 8

        octal = "-" + octal
        print("El número octal equivalente es:", octal)
    else:
        octal = ""
        while numero_a_convertir > 0:
            residuo = numero_a_convertir % 8
            octal = str(residuo) + octal
            numero_a_convertir = numero_a_convertir // 8

        print("El número octal equivalente es:", octal)


# 7. Mostrar resultado



