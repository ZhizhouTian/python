#!/usr/bin/python
import os

"""my first class: extends from file"""
class MySelf(object):
	version="0.1"

	"""constructor"""
	def __init__(this, name="Zhizhou"):
		this.name=name

	def showName(this):
		print "Name is: "+this.name

	def showVer(this):
		print "Version is: "+this.version

def main():
	self=MySelf("Daidai")
	self.showName()
	self.showVer()
	print self.__class__.__name__

main()
