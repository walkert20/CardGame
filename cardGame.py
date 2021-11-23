#cardGame.py

# chapter 8-3
print("Hello.")
import random
import time


class card():
	def __init__(self, value, suite):
		self.value = value
		self.suite = suite

deck = []
table = []
discard=[]
suites = ["Clubs","Hearts", "Spades", "Diamonds"]


def build_deck():
	deck.clear()
	discard.clear()
	for suite in suites:
		for i in range (1,11):
			deck.append(card(i, suite))
		deck.append(card("Jack", suite))
		deck.append(card("Queen", suite))
		deck.append(card("King", suite))
	return deck

def get_suite(card):
	return card.suite

def get_value(card):
	return card.value

def same_value(card1, card2):
	return(card1.value == card2.value)

def same_value_list(list_object):
	if len(list_object) <= 1:
		return False
	if len(list_object) == 2:
		return get_value(list_object[0]) == get_value(list_object[1])	
	else:
		card = list_object[0]
		for i in range(1, len(list_object)):
			if get_value(card) == get_value(list_object[i]):
				return True
		temp = list_object
		temp.pop(0)
		return same_value_list(temp)

def same_suite(card1, card2):
	return get_suite(card1) == get_suite(card2)

def deal_top_card():
	card = deck[0]
	discard.append(deck[0])
	deck.pop(0)
	return card

def get_random_card():
	card = random.choice(deck)
	discard.append(card)
	deck.remove(card)
	return card

def shuffle():
	random.shuffle(deck)
	
def deal_hand(size):
	hand = []
	for i in range(size):
		hand.append(deal_top_card())
	return hand


# # Extra funtion: deal_hands(the deck, the # of hands, size of each hand)


#build_deck()
#print("Deck is ready to be used. ")

def play_Go_Fish():
	print ("Hey! Let's play Go Fish!")
	build_deck()
	shuffle()
	player_hand = deal_hand(7)
	opponent_hand = deal_hand(7)
	table = []
	player_points = 0
	opponent_points = 0
	print("Your hand: ")
	for x in player_hand:
		print(x.value, x.suite)
	print("")
	for x in opponent_hand:
		print(x.value, x.suite)
	print ("")

# 	while same_value_list(player_hand) != False:
#		player_points += 1
# 		player_hand = remove_pairs(player_hand)
# 		print("You have " + player_points + " points.")
# 		print("")
# 	while same_value(opponent_hand) != False:
# 		opponent_points += 1
# 		opponent_hand = remove_pairs(opponent_hand)
# 		print ("Your opponent has ", + opponent_points + " points.")
# 		print("")

# 	print("Alright. You go first.")

# 	while len(player_hand) != 0 and len(opponent_hand) != 0:
# 		player_turn()
# 		opponent_turn()


	

# #### Go Fish helper functions:

# #def check_for_pairs(list_object):
# #	return same_value(list_object)

def remove_pairs(list_object):
	card = list_object[0]
	for i in range(1, len(list_object)):
		if get_value(card) == get_value(list_object[i]):
			temp = list_object[i]
			table.append([(card.value, card.suite), 
				(temp.value, temp.suite)])
			list_object.pop(0)
			list_object.pop(i)
			temp = list_object
	return temp




#def player_turn():

#def opponent_turn():
	# Note: for varying difficulties, have the 
	# opponent remember cards the player asked for.