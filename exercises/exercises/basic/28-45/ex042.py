# CODIGO A SEGUIR FOI COPIA DO CODIGO FEITO POR UMA IA, POR PREGUICA MINHA

import math

# Solicita ao usuário os comprimentos dos lados
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 == lado2 == lado3:
    # Triângulo Equilátero
    area = (math.sqrt(3) / 4) * (lado1 ** 2)
    perimetro = 3 * lado1
    print(f"Triângulo Equilátero: Área = {area:.2f}, Perímetro = {perimetro}")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    # Triângulo Isósceles
    if lado1 == lado2:
        base = lado3
        lado = lado1
    elif lado1 == lado3:
        base = lado2
        lado = lado1
    else:
        base = lado1
        lado = lado2
    
    altura = math.sqrt(lado**2 - (base**2 / 4))
    area = (base * altura) / 2
    perimetro = 2 * lado + base
    print(f"Triângulo Isósceles: Área = {area:.2f}, Perímetro = {perimetro}")
else:
    # Triângulo Escaleno
    s = (lado1 + lado2 + lado3) / 2
    area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    perimetro = lado1 + lado2 + lado3
    print(f"Triângulo Escaleno: Área = {area:.2f}, Perímetro = {perimetro}")
