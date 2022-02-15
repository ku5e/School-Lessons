#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:
import random
random.seed()
suites = ['H', 'C', 'S', 'D']
cards = []
for suite in suites:
	for i in range(1, 14):
		if i == 1:
			cards.append(suite + 'A')
		elif i > 10:
			if i == 11:
				cards.append(suite + 'J')
			elif i == 12:
				cards.append(suite + 'Q')
			else:
				cards.append(suite + 'K')
		else:
			cards.append(suite + str(i))

print(cards)
random.shuffle(cards)
random.shuffle(cards)
random.shuffle(cards)
print(cards)

for i in range(256):
	num = random.randint(0, 256)
	print(hex(num)[2:], end='')
print()


letter = ['a', 'b', 'c', 'd']
print(random.choice(letter)) #chooses random index from list
random.shuffle(letter)
print(letter)
print(random.randint(1,4))  #endpoints are both included
print(random.randrange(1, 10))  #stop is excluded
print(random.random() * 10)
print(random.uniform(1, 10))