#!/usr/bin/python
from __future__ import print_function
import os

def main(filename, word):
	if not os.path.exists(filename):
		print("file %s not exists" %filename)
		return

	with open(filename, 'w') as f:
		for i in range(10):
			print(word, file=f)
	print("write file %s success."%filename)

if __name__ == '__main__':
	main("test.txt", "hello world")
