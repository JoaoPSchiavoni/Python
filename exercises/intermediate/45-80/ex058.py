import random
pc_number = random.randint(0, 10)
count = 0
num = 0
while num != pc_number:
    num = int(input('Guess a number: '))
    count += 1
print(f'Nice you Win!!! my choise was {pc_number} but you needed {count} times')
