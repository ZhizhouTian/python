#!/usr/bin/python
import os
import sys
import re

def main(argc, argv):
	filename = argv[argc - 1]
	if not os.path.exists(filename):
		print "file %s not exists" %filename
		return

	with open(filename, 'r') as f:
		for row in f:
			data = row.split()
			for i in range(len(data)-1):
				print "%s\t" %data[i],
			numstr = data[len(data)-1]
			num = re.findall(r'\d+', numstr)
			print "%s" %num[0],
			print ''

if __name__ == '__main__':
	main(len(sys.argv), sys.argv)
