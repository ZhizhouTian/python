#!/usr/bin/python

def sort(arr):
	arrlen = len(arr)-1
	isSorted = False

	while not isSorted:
		isSorted = True
		for i in range(arrlen):
			if arr[i] > arr[i+1]:
				isSorted = False
				arr[i], arr[i+1] = arr[i+1], arr[i]
		print arr

def main():
	arr = [4, 3, 2, 1, 7, 5, 6, 8, 9]
	sort(arr)
	print arr

main()
