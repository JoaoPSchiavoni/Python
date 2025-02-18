salary = float(input('Salario do funcionario: R$ '))
salary_increase = (salary * 0.15) + salary
print('o salario que era de R${:.2f} com aumento de 15% passa a ser de R${:.2f}'.format(salary, salary_increase))