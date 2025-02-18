velo_car = int(input('Qual era a velocidade do carro: '))
if velo_car <= 80:
    print('O carro esta dentro do limite da pista')
else:
    multa = (velo_car - 80) * 7
    print('O carro estava {} acima do permitido multa de R$ {}'.format(velo_car, multa))