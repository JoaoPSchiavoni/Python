product_price = float(input('valor do produto: R$ '))
offer = product_price - (product_price * 0.05)
print(f'o produto de R${product_price} com desconto de 5% vai para R${offer:.2f}')