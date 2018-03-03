from random import randint
import config
import sys

class Deck:
	def __init__(self):
			self.cards = config.cards
			return
	
	def drawCard(self):
		return self.cards[randint(0, len(self.cards)-1)]

class Bet:
	def __init__(self, player, amount):
		self.player = player
		self.amount = amount
		return

class Box:
	def __init__(self):
		self.player = 0
		self.hands = []
		self.avail = True
	def openBox(self, player):
		self.player = player
		self.avail = False
	def addHand(self, hand):
		self.hands.append(hand)

class Hand:
	def __init__(self):
		self.cards = []
		self.bets = []
		return
	def addBet(self, player, amount):
		self.bets.append(Bet(player, amount))
		return
	def toString(self):
		ret = ""
		for x in range(0, len(self.cards)):
			ret = ret + self.cards[x] + " "
		return ret
	def hitCard(self, deck):
		self.cards.append(deck.drawCard())

class Table:
	def __init__(self):
		self.players = []
		self.dealerCards = Hand()
		self.deck = Deck()
		self.boxes = []
		for x in range(0,8):
			self.boxes.append(Box())
		return
	
	def addPlayer(self, newPl):
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
		#print boxes with their hand, players and bets
		print("--------------------------")
		print("Box" + '\t' + "Hand" + '\t\t' + "Player" + '\t' + "Bet")
		print("--------------------------")
		for x in range(0, len(self.boxes)):
			sys.stdout.write(str(x+1) + "\t")
			if (self.boxes[x].avail == True):
				print("closed")
			else:
				for y in range(0, len(self.boxes[x].hands)):
					sys.stdout.write(self.boxes[x].hands[y].toString() + "\t\t")
					for z in range(0, len(self.boxes[x].hands[y].bets)):
						sys.stdout.write(self.boxes[x].hands[y].bets[z].player.name + "\t")
						sys.stdout.write(str(self.boxes[x].hands[y].bets[z].amount) + "\n")
						if (z+1 < len(self.boxes[x].hands[y].bets)):
							sys.stdout.write("\t\t\t")
					if (y+1 < len(self.boxes[x].hands)):
						sys.stdout.write("\t")
		print
		print("Dealer: " + self.dealerCards.toString())
	
	def startRound(self):
		for x in range(0, len(self.boxes)):
			if (self.boxes[x].avail == False):
				self.boxes[x].addHand(Hand())
	
	def bettingRound(self):
		for x in range(0, len(self.boxes)):
			if (self.boxes[x].avail == False):
				sys.stdout.write("Box " + str(x+1) + " - " + self.boxes[x].player.name + "  to bet amount: ")
				(self.boxes[x].hands[0].addBet(self.boxes[x].player, self.boxes[x].player.getBet()))
	
	def dealRound(self):
		for x in range(0, len(self.boxes)):
			if (self.boxes[x].avail == False):
				self.boxes[x].hands[0].hitCard(self.deck)
				self.boxes[x].hands[0].hitCard(self.deck)
		self.dealerCards.hitCard(self.deck)

class Player:
	def __init__(self, name, bankroll):
		self.name = name
		self.bankroll = bankroll
		self.table = 0
	
	def joinTable(self, table):
		self.table = table
		self.table.addPlayer(self)
	
	def openBox(self, num):
		if (self.table.boxes[num-1].avail == False):
			print("Box not available")
		else:
			self.table.boxes[num-1].openBox(self)
	
	def getBet(self):
		return raw_input()

class Bot(Player):
	def __init__(self, name, bankroll):
		Player.__init__(self, name, bankroll)
		self.bet = 0
	
	def setBet(self, num):
		self.bet = num
	
	def getBet(self):
		print(self.bet)
		return self.bet
		

#userName = raw_input("Give me player 2's name: ")
#table.addPlayer(str(userName), 50)

table1 = Table()

p1 = Player("sewis", 400)
p2 = Player("magnus", 400)
p3 = Player("roan", 400)
b1 = Bot("bot1", 400)
m1 = Player ("mathilda", 800)
b1.setBet(120)

p1.joinTable(table1)
p2.joinTable(table1)
p3.joinTable(table1)
b1.joinTable(table1)
m1.joinTable(table1)

table1.printPlayers()

p1.openBox(8)
p2.openBox(6)
p3.openBox(6)
b1.openBox(1)
m1.openBox(7)

table1.startRound()
table1.bettingRound()
table1.dealRound()

table1.printTableStatus()





















