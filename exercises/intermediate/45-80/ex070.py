buy_list_value = []
product_1000 = 0
cheap_product_price = None
cheap_product = None
while True:
    
    item = input('Nome do Item: ')
    
    try:
        item_price = float(input('Preco do Produto: '))   
    except ValueError:
        print('Digite um valor valido! ')
        continue
    
    buy_list_value.append(item_price)
    
    if item_price >= 1000:
        product_1000 += 1
    
    if cheap_product_price is None or item_price < cheap_product_price:
        cheap_product_price = item_price
        cheap_product = item
    
    continue1 = input('Deseja continuar? [S/N]: ').lower()
    while continue1 not in ['s', 'n']:
        continue1 = input('Deseja continuar? [S/N]: ').lower()
    if continue1 == 'n':
        break

print(f'O Total Gasto foi {sum(buy_list_value):.2f}')
print(f'{product_1000} Foi iseridos com o valor maior ou igual a 1000')
print(f'O produto mais barato foi {cheap_product} custando apenas {cheap_product_price:.2f}')

    
    