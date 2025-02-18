import random
pc_number = random.randint(0, 2)
num = int(input('Guess a number: '))
if num == pc_number:
    print(f'Nice you Win!!! my choise was {pc_number}')
else:
    print(f'You lose! My number is {pc_number}')
