from web3 import Web3
from chronyk import Chronyk
from bs4 import BeautifulSoup
import requests, re, config, time
from chronyk import Chronyk
from config import *

class Bot:
    def __init__(self):
	self.url = "https://coinmarketcap.com/new"
	self.bsc = config.node
	self.web3 = Web3(Web3.HTTPProvider(self.bsc))
	self.checkConn = self.web3.isConnected()
	#self.latest_token = {}
    def getNewListing(self):
	"""get all the coins and add them to a list
	and then check the time it was added"""
	token = {}
	results = requests.get(self.url)
	doc = BeautifulSoup(results, 'html.parser')
	tbody = doc.find('tbody')
	trs = tbody.contents
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
	
	
	token['name'] = name
	token['price'] = price
	token['timeAdded'] = timeAdded
	token['blockChain'] = blockChain
	token['symbol'] = symbol
	#self.latest_token = token
	return token
    def sendMessage(self, phoneNumber, token, endPrice)
	"""code for sending text message"""
	message = f"Token {token} was launched on the Binance Smart Chain\n. Token {token} was bought.\nIt had a starting price of {price} and sold for {endPrice}\nProfit of {profit} was made."
    def calculateProfit(self, starting_price, ending_price):
	pass
    
    def tokenIsLocked(self, coin):
	pass
    def buyToken(self, tokenAddress):
	pass
    def sellToken(self, tokenAddress):
	pass
   

if __name__ = '__main__':
    bot = Bot()
    if bot.isConnected:
	token = bot.getNewListing()
	if tokenIsLocked(token):
	    while True:
		if bot.latest_token['name'] != token['name']:
		    bot.buyToken(tokenAddress)
		    if bot.calculateProfit(startingPrice, price) >= 40:
		        bot.sellToken(tokenAddress)

