# helper
def mostrar_mensaje(a_convertir, opcion, result):
    base = ''
    if opcion == 1:
        base = 'binario'
    if opcion == 2:
        base = 'octal'
    if opcion == 3:
        base = 'hexadecimal'

    print(f"El {a_convertir} en {base} es {result}")


print("Conversor de numeros base 10 a otro sistemas numérico")
# 1. Ingreso de datos
numero_a_convertir = (input("Ingrese un numero entero:\n"))

# 2. Validaciones (validamos que sea un numero)
while not (numero_a_convertir.isdigit() or (numero_a_convertir[0] == "-" and numero_a_convertir[1:].isdigit())):
    numero_a_convertir = input("Error: Por favor, ingresa un número entero válido:\n")

# convertimos el stirng a numero, lo hacemos despues de la validacion de numero entero para que no crashee si es flotante
numero_a_convertir = int(numero_a_convertir)

#  verificamos si el numero es negativo
es_negativo = numero_a_convertir < 0

# guardamos el numero en una variable auxiliar para poder operarla y modificarla
# de esta manera guardamos el original para futuras operaciones
numero_a_convertir_aux = (-numero_a_convertir) if es_negativo else numero_a_convertir

# 3. Selector de conversor
print("Ingresa el numero de la opción a la que quieres convertir")
print("1) Base 2")
print("2) Base 8")
print("3) Base 16")
opcion_a_convertir = int(input(""))

# verificamos que la opcion ingresada sea correcta
while opcion_a_convertir != 1 and opcion_a_convertir != 2 and opcion_a_convertir != 3:
    print("La opción ingresada es incorrecta")
    opcion_a_convertir = int(input("Ingrese 1, 2 o 3:\n"))

# validar si es cero
if numero_a_convertir == 0:
    mostrar_mensaje(numero_a_convertir, opcion_a_convertir, numero_a_convertir)
else:
    # 4. Conversion a bianrio (Fabricio)
    if opcion_a_convertir == 1:
        print("=== Conversión manual de entero a binario ===\n")

        binario = ""
        while numero_a_convertir_aux > 0:
            residuo = numero_a_convertir_aux % 2
            binario = str(residuo) + binario
            numero_a_convertir_aux = numero_a_convertir_aux // 2

        mostrar_mensaje(numero_a_convertir, opcion_a_convertir, f"-{binario}" if es_negativo else binario)

    # 6. Conversion a Octal (Juan)
    elif opcion_a_convertir == 2:
        print("=== Conversión manual de entero a octal ===\n")
        octal = ""

        while numero_a_convertir_aux > 0:
            residuo = numero_a_convertir_aux % 8
            octal = str(residuo) + octal
            numero_a_convertir_aux = numero_a_convertir_aux // 8

        mostrar_mensaje(numero_a_convertir, opcion_a_convertir, f"-{octal}" if es_negativo else octal)

    # 5. Conversion a hexadecimal (Gabi)
    elif opcion_a_convertir == 3:
        print(f"=== Conversión manual de entero {numero_a_convertir} a Hexadecimal  ===\n") 
        
        #Se definen letras para valores especiales 10, 11, 12, 13, 14, 15
        letras =["A", "B", "C", "D", "E", "F"]
        numero_hexadecimal = ""
        #Ciclo While para evaluar cada número positivo
        while numero_a_convertir_aux > 0:
            residuo = numero_a_convertir_aux % 16
            if residuo < 10: 
                digito = str(residuo)
            else:
                digito = letras[residuo-10]

            numero_hexadecimal = digito + numero_hexadecimal
            numero_a_convertir_aux = numero_a_convertir_aux // 16
            
        mostrar_mensaje(numero_a_convertir, opcion_a_convertir, f"-{numero_hexadecimal}" if es_negativo else numero_hexadecimal)
    else:
        print("La opción ingresada no es correcta")


