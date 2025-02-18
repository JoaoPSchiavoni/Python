#joken po
import random

print("""      [1] Stone
      [2] paper
      [3]scissors""")
user_value = int(input('Escolha as uma das opcoes: '))
pc_value = random.randint(1, 3)

if user_value == 1 and pc_value == 2:
    print('O computador Ganhou! computador escolheu Paper')
elif user_value == 3 and pc_value == 1:
    print('O computador Ganhou! computador escolheu Stone')
elif user_value == 2 and pc_value == 3:
    print('O computador Ganhou! computador escolheu Scissors')
elif user_value == 1 and pc_value == 3:
    print('Parabens voce Ganhou do computador! Computador escolheu Scissors')
elif user_value == 2 and pc_value == 1:
    print('Parabens voce Ganhou do computador! Computador escolheu Stone')
elif user_value == 3 and pc_value == 2:
    print('Parabens voce Ganhou do computador! Computador escolheu Paper')
else:
    print(f'Empate! Ambos escolheram {["Stone", "Paper", "Scissors"][user_value - 1]}')
