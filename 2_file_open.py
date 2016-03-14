#!/usr/bin/python
import os

def readfile(filp):
	try:
		i=0
		for line in filp:
			print "%d\t"%i +line ,
			i+=1
		
		#print filp.fileno()
		filp.close()
	except IOError, e:
		print 'file open error:', e
	return 0
	
def main():
	filename=raw_input("input a filename: ")
	print filename
	
	try:
		if os.path.exists(filename):
			filp=open(filename, 'rw')
		else:
			print "file not found."
			return -1
			#filp=open(filename, 'w+')
		print isinstance(filp, file)
		print type(readfile)
		readfile(filp)
	except IOError, e:
		print 'file open error:', e

main()
