#!/usr/bin/python
import os

def main():
	print os.path.dirname(os.path.abspath(__file__))
	print os.getcwd()
	print os.path.abspath(".")
	print os.path.abspath("~")

if __name__ == "__main__":
	main()
