#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:
import random

input('Hit enter to roll d20. ')

dieRoll = random.randint(1,20)
print(dieRoll)

if dieRoll >= 12:
	sides = int(input('Enter the num of sides of your attack die. '))
	dieRoll = random.randint(1, sides)
	print(dieRoll)
