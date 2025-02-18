import random

num = tuple(random.randint(1, 100) for _ in range(5))
print('Numeros gerados: ', num)

print(f"O menor valor é {min(num)}") 
print(f"O maior valor é {max(num)}")
