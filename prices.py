import requests, logging
from bs4 import BeautifulSoup
from chronyk import Chronyk
import config

logging.basicConfig(filename='log.txt',
	filemode='a',
	format='%(asctime)s %(levelname)s-%(message)s',
	datefmt='%Y-%m-%d %H:%M:%S')


url = 'https://coinmarketcap.com/new'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

tbody = doc.find('tbody')
trs = tbody.contents

prices = {}
token = {}
tr1 = trs[0]


name, price = tr1.contents[2:4]
n = name.find_all('p')
timeAdded = tr1.contents[-2]
blockchain = tr1.contents[-3]

name = name.p.string
price = price.span.string
timeAdded = timeAdded.string
blockChain = blockchain.div.img.next_sibling
symbol = n[1].string

print(f'{name}\n\n{price}\n\n{timeAdded}\n\n{blockChain}')
print(f'\n\n{symbol}\n\n')
#for td in tr1.contents:
 #   print(td)
  #  print('\n\n\n')

#percent = tr1.contents[4]
#print(percent.span)

token = dict(name=name, price=price, timeAdded=timeAdded, blockChain=blockChain, symbol=symbol)
