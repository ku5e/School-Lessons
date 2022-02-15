#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:
import random

def dealCards(deal):
	player = []
	for i in range(deal):
		player.append(cards[i])
		cards.remove(cards[i])
	return player

suites = ['H', 'D', 'S', 'C']
cards = []

for suite in suites:
	for i in range(1, 14):
		if i == 1:
			cards.append('A' + suite)
		elif i > 10:
			if i == 11:
				cards.append('J' + suite)
			elif i == 12:
				cards.append('Q' + suite)
			else:
				cards.append('K' + suite)
		else:
			cards.append(str(i) + suite)
			
random.shuffle(cards)
random.shuffle(cards)
random.shuffle(cards)

deal = 5
mario = dealCards(5)
kumail = dealCards(5)
banning = dealCards(5)
pratham = dealCards(5)
#hand1 = []
#hand2 = []
#
#for i in range(deal):
#	hand1.append(cards[i])
#	cards.remove(cards[i])
			
print(mario)
print(kumail)
print(banning)
print(pratham)

print(cards)
	