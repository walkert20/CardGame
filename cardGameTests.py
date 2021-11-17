# Hello. This is the testing file.

import random
import time
import cardGame

def test_constructor():
	print("")
	print ("Testing the constructor....")
	card = None
	assert card == None
	card = cardGame.card(3, "Hearts")
	assert card != None
	print ("Constructor is functioning.")
	print("")

def test_build_deck():
	print("Testing the deck constructor....")
	deck = []
	deck = cardGame.build_deck()
	assert len(deck) == 52
	print("Deck Constructs. ")
	print("")

def test_get_suite():
	print("Testing getter function for suite....")
	card = cardGame.card(3, "Hearts")
	suite = "Hearts"
	assert cardGame.get_suite(card) == suite

	suite = "Spades"
	assert cardGame.get_suite(card) != suite
	print("Getter function for suite is working.")
	print("")

def test_get_value():
	print("Testing getter function for value....")
	card = cardGame.card(3, "Hearts")
	value = 3
	assert cardGame.get_value(card) == value
	value = 6
	assert cardGame.get_value(card) != value
	print("Getter function for value is working.")
	print("")

def test_same_value():
	print("Testing for same value cards....")
	print("with different suites....")
	card1 = cardGame.card(3, "Hearts")
	card2 = cardGame.card(3, "Spades")
	assert cardGame.get_value(card1) == cardGame.get_value(card2)
	assert cardGame.get_suite(card1) != cardGame.get_suite(card2)
	assert cardGame.same_value(card1, card2) == True

	print("with different values, but same suite....")
	card3 = cardGame.card(5, "Hearts")
	assert cardGame.same_value(card1, card3) == False

	print("with different values and different suits....")
	assert cardGame.same_value(card2, card3) == False
	print("Same value function is functioning.")
	print("")

def test_same_value_list():
	print("Testing for same value cards within a list....")
	test_same_value_list_1()
	test_same_value_list_2()
	print("Tests passed.")
	print("")

def test_same_value_list_1():
	# Case where list size is 0.
	hand = []
	assert cardGame.same_value_list(hand) == False

	# Case where the list size is 1.
	hand.append(cardGame.card(1, "Hearts"))
	assert cardGame.same_value_list(hand) == False

	# Case where the list size is 2 and there isn't a pair.
	hand.append(cardGame.card(2, "Hearts"))
	assert cardGame.same_value_list(hand) == False

	#Case where the list size is 2 and there is a pair.
	hand.pop(1)
	hand.append(cardGame.card(1, "Diamonds"))
	assert cardGame.same_value_list(hand) == True

def test_same_value_list_2():
	# Case where the list size is 3 and the pair is the first 
	# and last card.
	hand = []
	hand.append(cardGame.card(1, "Diamonds"))
	hand.append(cardGame.card(4, "Diamonds"))
	hand.append(cardGame.card(1, "Spades"))
	assert cardGame.same_value_list(hand) == True

	# Case where there are numerous pairs within a larger list.
	hand.pop(2)
	hand.append(cardGame.card(3, "Clubs"))
	hand.append(cardGame.card(4, "Clubs"))
	hand.append(cardGame.card(3, "Hearts"))
	assert cardGame.same_value_list(hand) == True

	# Case where the list is longer, but there are no pairs.
	hand.pop(-1)
	hand.pop(-1)
	hand.append(cardGame.card(7, "Clubs"))
	hand.append(cardGame.card("King", "Clubs"))
	hand.append(cardGame.card("Jack", "Hearts"))
	assert cardGame.same_value_list(hand) == False

	# Case where there is a pair of face cards.
	hand.append(cardGame.card("King", "Spades"))
	for x in hand:
		print(cardGame.get_value(x))
	assert cardGame.same_value_list(hand) == True

def test_same_suite():
	print("Testing for same suite cards....")
	card1 = cardGame.card(3, "Hearts")
	card2 = cardGame.card(3, "Spades")
	assert cardGame.same_suite(card1, card2) == False

	card3 = cardGame.card(6, "Hearts")
	assert cardGame.same_suite(card1, card3) == True
	print("Tests passed.")
	print("")

def test_deal_top_card():
	print("Testing the dealing of the top card....")
	deck = cardGame.build_deck()
	temp = deck[0]
	assert (temp == cardGame.deal_top_card())
	assert (temp != deck[0])
	assert (temp == cardGame.discard[0])
	assert (len(deck) == 51)
	print("Tests passed.")
	print("")

def test_get_random_card():
	print("Testing drawing a random card from the deck")
	deck = cardGame.build_deck()
	temp = cardGame.get_random_card()
	assert (temp == cardGame.discard[0])
	assert (temp not in deck)
	assert (len(deck) == 51)
	print("Random card drawn. Tests passing.")
	print("")


def main():
	test_constructor()
	test_build_deck()
	test_get_suite()
	test_get_value()
	test_same_value()
	test_same_value_list()
	test_same_suite()
	test_deal_top_card()
	test_get_random_card()
