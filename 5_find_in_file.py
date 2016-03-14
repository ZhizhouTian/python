#!/usr/bin/python
import os

def main(filename, word):
	with open(filename, 'r') as f:
		for i, x in enumerate(f):
			#common = set(x) & set(word)
			#if common:
				#print "".join(common)
			if word in x:
				print word

if __name__ == '__main__':
	main("test.txt", "hel")
