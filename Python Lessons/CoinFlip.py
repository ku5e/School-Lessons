#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:
import random

coin = ['heads', 'tails']
input('Press enter to start flipping the coin.')

count = 0
tries = 0
trig = 0
while count != 2:
	tries += 1
	flip = random.choice(coin)
	print(flip)
	if(flip == 'heads' and trig < 2):
		count += 1
		trig += 1
	elif(flip == 'heads'):
		count += 1
	else:
		count = 0
	

print('It took %s flips' % tries)
	
