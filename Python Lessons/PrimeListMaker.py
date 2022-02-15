#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:
#import cProfile, pstats
#pr = cProfile.Profile()
#pr.enable()
import sys

'''
create variable
	int
	float
	boolean
	str
create list
	list = [1, 2, ...]
iterate over the list or string (count controlled list)
	for i in range (something): #normal for
	for in in list: #enhanced for loop
note: itterater can not be effected except by the loop
other loop (condition controlled loop)
	while (condition):
math
	+, -, *, /, //, **, %, ()
comparisons
	<, >, <=, >=, ==, !=
function 
	def name(what it takes in):

'''

#def primeList(x):
#	list = [2]
#	for i in range(3, sys.maxsize, 2):
#		if isPrime(i, list):
#			list.append(i)
#		if len(list) >= x:
#			return list

def primes(n):
	sieve = [True] * n
	for i in range(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
	return [2] + [i for i in range(3,n,2) if sieve[i]]

#def isPrime(x, arr):
#	for nums in arr:
#		if x % nums == 0:
#			return False
#	return True
	
#print(primeList(10000))
print(primes(30))

#pr.disable()
#ps = pstats.Stats(pr).print_stats()