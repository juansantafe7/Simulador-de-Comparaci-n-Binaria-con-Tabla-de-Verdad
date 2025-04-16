# 1. Ingreso de datos
print("Simulador de Comparación Binaria con Operaciones Lógicas")
num1 = int(input("Ingrese el primer número decimal: "))
num2 = int(input("Ingrese el segundo número decimal: "))

# 2. Conversión a binario
bin1 = bin(num1)[2:]  # [2:] para quitar el '0b' del inicio
bin2 = bin(num2)[2:]

# 3. Normalización de longitud (rellenamos con ceros a la izquierda)
max_len = max(len(bin1), len(bin2))
bin1 = bin1.zfill(max_len)
bin2 = bin2.zfill(max_len)

# 4. Operaciones bit a bit
and_result = []
or_result = []
xor_result = []

for bit1, bit2 in zip(bin1, bin2):
    b1 = int(bit1)
    b2 = int(bit2)
    and_result.append(str(b1 & b2))
    or_result.append(str(b1 | b2))
    xor_result.append(str(b1 ^ b2))

# 5. Mostrar tabla
print("\nResultado de las operaciones bit a bit:\n")
print("Bit A | Bit B | AND | OR  | XOR")
print("-------------------------------")
for i in range(max_len):
    print(f"  {bin1[i]}   |   {bin2[i]}   |  {and_result[i]}   |  {or_result[i]}   |  {xor_result[i]}")
