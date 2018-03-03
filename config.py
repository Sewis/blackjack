#####################################################
#					Table							#
#####################################################

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
boxesPerTable = 8
dealerRule = 0		# 0- Dealer draws to 16 and stands on 17
					# 1- Dealer must hit soft 17

#####################################################
#					Deck  		   					#
#####################################################

deckCards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

#####################################################
#					Insurance						#
#####################################################

toggleInsurance = 0		# 0-Off
						# 1-On
						
insurance_Pays = 0		# 0- 2 to 1
						# 1- 3 to 2
						# 2- 6 to 5

#####################################################
#					Betting							#
#####################################################

startAmount = 500
tableMinimum = 50
tableMaximum = 20000

blackjack_Pays = 1		# 0- 2 to 1
						# 1- 3 to 2
						# 2- 6 to 5

#####################################################
#					Modes							#
#####################################################

mode = 0		# 0- Normal Play
				# 1- Automatic Simulation

advice = 0		# 0-Off		(Only for normal play)
				# 1-On

rounds = 1000			#only for Automatic Simulation
betting_amount = 50		#only for Automatic Simulation

#####################################################
#					Strategy						#
#####################################################

#		Dealer:	 2	 3	 4	 5	 6	 7 	 8	 9	 10	 A	   Player:
strategy = [[	'H','H','H','H','H','H','H','H','H','H'	],#	5		Hard Hands
			[	'H','H','H','H','H','H','H','H','H','H'	],#	6
			[	'H','H','H','H','H','H','H','H','H','H'	],#	7
			[	'H','H','H','H','H','H','H','H','H','H'	],#	8
			[	'H','D','D','D','D','H','H','H','H','H'	],#	9
			[	'D','D','D','D','D','D','D','D','H','H'	],#	10
			[	'D','D','D','D','D','D','D','D','D','H'	],#	11
			[	'H','H','S','S','S','H','H','H','H','H'	],#	12
			[	'S','S','S','S','S','H','H','H','H','H'	],#	13
			[	'S','S','S','S','S','H','H','H','H','H'	],#	14
			[	'S','S','S','S','S','H','H','H','H','H'	],#	15
			[	'S','S','S','S','S','H','H','H','H','H'	],#	16
			[	'S','S','S','S','S','S','S','S','S','S'	],#	17
			[	'S','S','S','S','S','S','S','S','S','S'	],#	18
			[	'S','S','S','S','S','S','S','S','S','S'	],#	19
			[	'S','S','S','S','S','S','S','S','S','S'	],#	20
			
			[	'H','H','H','D','D','H','H','H','H','H'	],#	A,2		Soft Hands
			[	'H','H','H','D','D','H','H','H','H','H'	],#	A,3
			[	'H','H','H','D','D','H','H','H','H','H'	],#	A,4
			[	'H','H','H','D','D','H','H','H','H','H'	],#	A,5
			[	'H','H','H','H','H','H','H','H','H','H'	],#	A,6
			[	'H','H','H','H','H','H','H','H','H','H'	],#	A,7
			[	'H','H','H','H','H','H','H','H','H','H'	],#	A,8
			[	'H','H','H','H','H','H','H','H','H','H'	],#	A,9
			
			[	'H','H','H','H','H','H','H','H','H','H'	],#	2,2		Doubles
			[	'H','H','H','H','H','H','H','H','H','H'	],#	3,3
			[	'H','H','H','H','H','H','H','H','H','H'	],#	4,4
			[	'H','H','H','H','H','H','H','H','H','H'	],#	5,5
			[	'H','H','H','H','H','H','H','H','H','H'	],#	6,6
			[	'H','H','H','H','H','H','H','H','H','H'	],#	7,7
			[	'H','H','H','H','H','H','H','H','H','H'	],#	8,8
			[	'H','H','H','H','H','H','H','H','H','H'	],#	9,9
			[	'H','H','H','H','H','H','H','H','H','H'	],#	10,10
			[	'H','H','H','H','H','H','H','H','H','H'	],#	A,A
			]
