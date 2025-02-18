from math import hypot, sqrt
x = float(input('Digite o cateto oposto: '))
y = float(input('Digite o cateto adjacente: '))
hyp = sqrt(x*x + y*y)
print(f'A hypotenusa é {hyp:.2f}')