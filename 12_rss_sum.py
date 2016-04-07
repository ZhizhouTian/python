#!/usr/bin/python
import os
import re

def main(filename, word):
	f = open(filename, 'r')
	line = f.readline()
	size_sum = 0
	while(line):
		if (word in line):
			siz = int(re.findall(r'\d+', line)[0])
			size_sum += siz
		line = f.readline()

	print("Sum_%s = %d"%(word,size_sum))

if __name__ == '__main__':
	main("./VMA", "Rss:")
	main("./VMA", "Pss:")
	main("./VMA", "Uss:")
