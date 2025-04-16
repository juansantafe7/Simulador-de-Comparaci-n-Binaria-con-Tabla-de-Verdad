print("Conversor de numeros base 10 a otro sistemas numérico")
# 1. Ingreso de datos
numero_a_convertir = input("Ingrese un numero entero positivo:\n")

# 2. Validación
while not numero_a_convertir.isdigit():
  numero_a_convertir = input("Error: Por favor, ingresa un numero entero positivo:\n")


# 3. Selector de conversor
print("Ingresa el numero de la opción a la que quieres convertir")
print("1) Base 2")
print("2) Base 8")
print("3) Base 16")
opcion_a_convertir = int(input(""))

while opcion_a_convertir != 1 and opcion_a_convertir != 2 and opcion_a_convertir != 3:
   print("La opción ingresada es incorrecta")
   opcion_a_convertir = int(input("Ingrese 1, 2 o 3:\n"))

# 4. Conversion a bianrio (Fabricio)

# 5. Conversion a hexadecimal (Gabi)

# 6. Conversion a Octal (Juan)

# 7. Mostrar resultado





