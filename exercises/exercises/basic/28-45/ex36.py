house_value = float(input('Digite o Valor da casa: R$ '))
payslip = float(input('Digite o salario: R$ '))
years = int(input('Quantos anos deseja pagar: '))

# variaveis para armazenar o valores da casa e payslip
monthly_amount = (years * 12) / house_value
payslip_value = payslip * 0.3

# Verificacao para autorizar o emprestimo
if monthly_amount <= payslip_value:
    print('O emprestimo esta APROVADO!')
else:
    print('O emprestimo esta NEGADO!')