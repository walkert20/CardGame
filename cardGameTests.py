# Hello. This is the testing file.

import random
import time
import cardGame

def constructor_test():
	print ("Testing the constructor....")
	card = None
	assert card == None
	card = cardGame.card(3, "Hearts")
	assert card != None
	print ("Constructor is functioning.")

constructor_test()
