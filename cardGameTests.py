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

def test_get_suite():
	print("Testing getter function for suite....")
	card = cardGame.card(3, "Hearts")
	suite = "Hearts"
	assert cardGame.get_suite(card) == suite
	suite = cardGame.get_suite(card)
	assert cardGame.get_suite(card) == suite
	print("Getter function for suite is working.")
	print("")

def test_get_value():
	print("Testing getter function for value....")
	card = cardGame.card(3, "Hearts")
	value = 3
	assert cardGame.get_value(card) == value
	value = cardGame.get_value(card)
	assert cardGame.get_value(card) == value
	print("Getter function for value is working.")
	print("")

def main():
	test_constructor()
	test_build_deck()
	test_get_suite()
	test_get_value()
