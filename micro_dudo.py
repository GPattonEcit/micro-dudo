# Micro Dudo
# Run this script using the command: `python3 micro_dudo.py`
# This python script is written in python3
import random
import sys
from itertools import cycle

def roll_dice():
	# Roll Dice
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	return d1, d2

try:
	attempt = 0
	while attempt < 3:	# allow 3 attempts before aborting
		go = input("Enter y when you're ready: ")
		if attempt == 2:
			print("Too many invalid options... exiting...")
			sys.exit()
		elif go != 'y':
			print("Invalid option... try again")
			attempt += 1
		elif go == 'y':
			break
	# if attempt == 3:
	# 	print("flag2")
	# 	sys.exit()
except:
	sys.exit()

player1_d1, player1_d2 = roll_dice()
player2_d1, player2_d2 = roll_dice()

dice_on_table = [player1_d1, player1_d2, player2_d1, player2_d2]

print("Your roll is {}, {}".format(player1_d1, player1_d2))
#print("Dice on table is {}".format(dice_on_table))


def player1_turn(player):
	bid = input("{} --> Make your bid (e.g. if you think there are two 2s write `2x2`:\n\tbid = ".format(player))
	bid_num = bid[0]	# Number of this roll on the table
	bid_roll = bid[2]	# The roll number
	print("Player {} bids there are {} {}s on the table..".format(player, bid_num, bid_roll))
	return bid_num, bid_roll

def player2_turn(player, p1_bid_num, p1_bid_roll):
	# Check player 1's bid
	# For now increment player 1's bid by one
	while p1_bid_roll < 6:	# can't have a roll over 6
		# if roll under 6, just increment the roll by 1 and keep the numeber the same
		bid_num = p1_bid_num
		bid_roll = p1_bid_roll + 1
	else:
		# if the roll is 6, increment the number by one and go back to roll of 1
		bid_num = p1_bid_num + 1
		bid_roll = '1'

for player in cycle(["Player1", "Player2"]):
	p1_bid_num, p1_bid_roll = player1_turn(player)

