product_price = float(input('Digite o valor do produto: '))
#Mostrar as opcoes de pagamento ao usuario
print("[1]2x no Cartao: preco normal")
print("[2]A vista Cartao: Desconto de 5%")
print("[3]A vista Dinheiro/Cheque: Desconto de 10%")
print("[4]3x ou mais no Cartao: Juros de 20%")

payment = int(input('Qual A sua escolha: '))

if payment == 1:
    print(f'O valor do Produto sera de {product_price:.2f}')
elif payment == 2:
    product_price = product_price - (product_price * 0.05)
    print(f'O valor do Produto sera de {product_price:.2f} com 5% de desconto')
elif payment == 3:
    product_price = product_price - (product_price * 0.1)
    print(f'O valor do Produto sera de {product_price:.2f} com 10% de desconto')
elif payment == 4:
    product_price = product_price + (product_price * 0.2)
    print(f'O valor do Produto sera de {product_price:.2f} com 20% de Juros')
else:
    print('A opcao escolhida nao foi encontrada')