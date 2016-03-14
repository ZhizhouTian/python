#!/usr/bin/python

def sort(arr):
	arrlen = len(arr)

	for i in range(arrlen-1):
		for j in range(i, arrlen-1):
			if arr[j] < arr[i]:
				arr[j], arr[i] = arr[i],arr[j]

def main():
	arr = [4, 3, 2, 1, 7, 5, 9, 0, 9]
	sort(arr)
	print arr

main()
