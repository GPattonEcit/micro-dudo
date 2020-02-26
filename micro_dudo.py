# Micro Dudo
# Run this script using the command: `python3 micro_dudo.py`
# This python script is written in python3
import random
import sys

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
print("Dice on table is {}".format(dice_on_table))

#bid = input("Make your bid (e.g. if you think there are two 2s write `2x2`")
