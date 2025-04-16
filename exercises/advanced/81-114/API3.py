import requests, json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-USD')
cotacoes = cotacoes.json()
dolar = cotacoes['USDBRL']['bid']
euro = cotacoes['EURBRL']['bid']
btc = cotacoes['BTCUSD']['bid']
print(f'A cotação do Dólar é: {dolar}')
print(f'A cotação do Euro é: {euro}')
print(f'A cotação do Bitcoin é: {btc}')