import requests
import json

requisicao = requests.get('https://api.hgbrasil.com/finance?key=2ebfe9dd')
cotacao = json.loads(requisicao.text)
'''print(valor) '''
dolar = cotacao['results']['currencies']['USD']['buy']
euro = cotacao['results']['currencies']['EUR']['buy']
real = float(input('Informe um valor desejado em R$: '))
dolarConvertido = real*dolar
euroConvertido = real*euro
print(f'Valor em dolar: {dolarConvertido}')
print(f'Valor em euro: {euroConvertido}')
