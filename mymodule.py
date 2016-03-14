#!/usr/bin/python
import os

def readfile(filename):
	try:
		with open(filename) as filp:
			i=0
			for line in filp:
				print "%d\t"%i +line ,
				i+=1
			
			#print filp.fileno()
			filp.close()
	except IOError, e:
		print 'file open error:', e
	return 0
print __name__
