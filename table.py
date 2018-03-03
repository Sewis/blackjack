from random import randint
import config

class Deck:
	cards = 0
	def __init__(self):
			self.cards = config.cards
	
	def drawCard(self):
		return self.cards[randint(0, len(self.cards)-1)]

class Table:
	def __init__(self):
		self.players = [];
		self.dealerCards = [];
		self.deck = Deck()
		return
	
	def addPlayer(self, name, bankroll):
		newPl = Player(name, bankroll)
		self.players.append(newPl)
		return
	
	def printDealerCards(self):
		res = ""
		for x in range(0, len(self.dealerCards)):
			res = res + self.dealerCards[x] + " "
		return res
	
	def printPlayers(self):
		print("--------------------------")
		print("Players at Table")
		print("--------------------------")
		print("Name" + '\t' + "Bankroll")
		print("-----" + '\t' + "----------")
		for x in range(0, len(self.players)):
			print(self.players[x].name + '\t' + str(self.players[x].bankroll))
		print("--------------------------")
	
	def printTableStatus(self):
		print("--------------------------")
		print("Dealer Cards:" + "\t" + self.printDealerCards())
		print("--------------------------")
		print("Name" + '\t' + "Cards")
		print("-----" + '\t' + "----------")
		for x in range(0, len(self.players)):
			print(self.players[x].name + '\t' + self.players[x].printHand())
		print("--------------------------")
	
	def dealRound(self):
		self.dealerCards.append(self.deck.drawDealerCard())
		for x in range(0, len(self.players)):
			self.players[x].getCard(self.deck.drawPlayerCard1())
		for x in range(0, len(self.players)):
			self.players[x].getCard(self.deck.drawPlayerCard2())

class Box:
	cft = 0


class Hand:
	def __init__(self):
		self.cards = []
		self.bets = []

class Player:
	def __init__(self, name, bankroll):
		self.name = name
		self.bankroll = bankroll
		self.hand = []
		#self.hands = []
	
	def printHand(self):
		res = ""
		for x in range(0, len(self.hand)):
			res = res + str(self.hand[x]) + " "
		return res
	
	def getCard(self, card):
		self.hand.append(card)

userName = input("Give me player 2's name: ")

deck1 = Deck()
deck2 = Deck()

table = Table()
table.addPlayer('john', 30)
table.addPlayer(userName, 50)
table.addPlayer('sewis', 400)

table.printPlayers()

table.dealRound()

table.printTableStatus()
