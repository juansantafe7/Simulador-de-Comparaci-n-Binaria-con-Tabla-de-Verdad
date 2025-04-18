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
   #Evaluamos si el número ingresado es menor a 10 y asignamos su valor Hexadecimal sin hacer conversión.
   if numero_a_convertir < 10:
      print(f"El número decimal {numero_a_convertir}, es igual en hexadecimal")
   if numero_a_convertir == 15:
      print(f"El número decimal {numero_a_convertir}, es la letra F en Haxadecimal")
   if numero_a_convertir == 14:
      print(f"El número decimal {numero_a_convertir}, es la letra E n Haxadecimal")
   if numero_a_convertir == 13:
      print(f"El número decimal {numero_a_convertir}, es la letra D en Hexadecimal")
   if numero_a_convertir == 12:
      print(f"El número decimal {numero_a_convertir}, es la letra C en Hexadecimal")
   if numero_a_convertir == 11:
      print(f"El número decimal {numero_a_convertir}, es la letra B en Hexadecimal")
   if numero_a_convertir == 10:
      print(f"El número decimal {numero_a_convertir}, es la letra A en Hexadecimal")
   if numero_a_convertir < 10:
      print(f" El número decimal {numero_a_convertir} es igual en el sistema Hexadecimal")
   #En el caso que el número ingresado sea mayor a 10, dividimos entre 16 para hacer la conversión
   else:
        #Armamos una lista para ingresar las letras que corresponden a los número decimales desde el 10 al 15
        letras =["A", "B", "C", "D", "E", "F"]
        #Creamos una lista para ir guardando el resultado de la divsión del número decimal a hexadecimal. 
        numero_hexadecimal = []
        #Mientrás el número sea mayor a 15 evaluamos dividimos entre 16.
        while numero_a_convertir > 0:
              #Se almacena el residuo de la división
            residuo = numero_a_convertir % 16
            #Evaluamos si el residuo es menor a 10 y lo convertimos en string para almecenarlo en la lista de numero_hexadecimal.
            if residuo < 10: 
                 digito = str(residuo)
            #Cuando el residuo sea entre 10 y 15, le restaremos 10 a la lista de letras y nos dará el indice de la letra que corresponda. 
            else:
                 digito = letras[residuo-10]
            #Una vez evaluadas todas las condiciones insertamos el valor del dígito en la variable numero_hexadecimal como lista. 
            numero_hexadecimal.insert(0, digito)
            # Dividimos el número decimal entre 16, y e2025l resultado lo asigamos a la variable numero_a_convertir para evaluar nuevamente la condición While. 
            numero_a_convertir = numero_a_convertir // 16
        #Finalmente unimos todos los valores de residuos guardados en la varible mientras se ejecutó el bucle While
        print("El número en hexadecimal es:", "".join(numero_hexadecimal))
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



