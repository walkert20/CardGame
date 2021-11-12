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
	deck = None
	assert deck == None
	deck = cardGame.build_deck()
	assert deck != None
	assert len(deck) == 52
	print("Deck Constructs. ")
	print("")

#def main():
#	test_constructor()
#	test_build_deck()
