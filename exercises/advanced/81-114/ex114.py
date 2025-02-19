import ssl
import certifi
import urllib.request

try:
    context = ssl.create_default_context(cafile=certifi.where())
    resp = urllib.request.urlopen('https://www.pudim.com.br', context=context)

except urllib.error.URLError as e:
    print('Site não acessível no momento.')
    print('Erro:', e.reason)

else:
    print('Site acessível no momento.')