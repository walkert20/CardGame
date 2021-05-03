#cardGame.py

# chapter 8-3
print("Hello.")
import random


deck = []
suites = ["Clubs","Hearts", "Spades", "Diamonds"]

##########		WRITE TEST FOR 		##########

def build_deck():
	for suite in suites:
		deck.append("Ace of " + suite)
		for i in range(2,11):
			deck.append( str(i) + " of " + suite )
		deck.append("Jack of " + suite)
		deck.append("Queen of " + suite)
		deck.append("King of " + suite)
	return 

def clear_deck():
	while len(deck) != 0:
		deck.pop(0)

def get_suit(string):
	for suite in suites:
		if suite in string:
			return suite

def get_value(string):
	return string[0]

#This function  works on 2+ cards.
def same_value(list_object):
	if len(list_object) <= 1:
		return "List is too small."
	if len(list_object) == 2:
		return get_value(list_object[0]) == get_value(list_object[1])

	card = list_object[0]
	for x in list_object[1:-1]:
		if get_value(card) == get_value(x) :
			return True

	return same_value(list_object[1:-1])

def same_suit(string1, string2):
	return get_suit(string1) == get_suit(string2)

def deal_top_card():
	card = deck[0]
	deck.pop(0)
	return card
	
def get_random_card():
	x = random.choice(deck)
	deck.remove(x)
	return x

def shuffle():
	random.shuffle(deck)

def deal_hand(int):
	hand = []
	for i in range(int):
		hand.append(deal_top_card())
	return hand	

# Extra funtion: deal_hands(the dck, the # of hands, size of each hand)
#
#
#
#############		TEST		############# dauntless dominate dragon "reverse" + dauntless drive dragon




build_deck()
print("deck is ready to be used")
#print (deck)

def play_Go_Fish():
	print ("Hey! Let's play Go Fish!")
	shuffle()
	player_hand = deal_hand(7)
	opponent_hand = deal_hand(7)
	table = []
	player_points = 0
	opponent_points = 0
	print("Any pairs?")

	while same_value(player_hand) != False:
		player_points += 1
		remove_pairs(player_hand)
	while same_value(opponent_hand) != False:
		opponent_points += 1
		remove_pairs(opponent_hand)

	print("Alright. You go first.")

	while len(player_hand) != 0 && len(opponent_hand) != 0:
		player_turn()
		opponent_turn()


	

#### Go Fish helper functions:

#def check_for_pairs(list_object):
#	return same_value(list_object)

def remove_pairs(list_object):
	if len(list_object) == 2:
		if same_value(list_object):
			list_object.pop(0)
			list_object.pop(0)
			return list_object
		else:
			return list_object

	card = list_object[0]
	for x in list_object[1:-1]:
		if get_value(card) == get_value(x) :
			list_object.pop(x)
			list_object.pop(card)
			return list_object

def player_turn():

def opponent_turn():
	# Note: for varying difficulties, have the 
	# opponent remember cards the player asked for.
