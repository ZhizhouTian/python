#!/usr/bin/python
from __future__ import print_function
import getopt
import sys

class user_operations(object):
	va=''
	vb=''

	def __init__(this):
		pass

	def __init__(this, va='', vb=''):
		this.va = va
		this.vb = vb
		return

	def __str__(this):
		return 'va:'+this.va+' vb:'+this.vb

def usage(argv):
	print("Usage: %s [-h | --help] [--a va] [--b vb]"%argv[0])
	return

def main(argc, argv):
	if argc <= 1:
		usage(argv)
		return 0

	try:
		opts, args = getopt.getopt(argv[1:], 'h', ['help', 'a=', 'b='])
		#raise getopt.GetoptError, "error"
	except getopt.GetoptError:
		print("Invalid argument", file=sys.stderr);
		return -1

	user_opt = user_operations()

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage(argv)
			return 0
		if opt in '--a':
			user_opt.va = arg
		if opt in '--b':
			user_opt.vb = arg
	print(user_opt)
	return 0

if __name__ == "__main__":
	main(len(sys.argv), sys.argv)
