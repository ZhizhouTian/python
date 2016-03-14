#!/usr/bin/python

def sort(arr):
	idx=0
	while idx < len(arr):
		i=0
		val=0
		for i, val in enumerate(arr[idx:]):
			print arr
			if val < arr[idx]:
				arr[i]=arr[idx]
				arr[idx]=val
		idx+=1

def main():
	arr = [4, 3, 2, 1, 7, 5, 6, 8, 9]
#for i in range(10):
#		val = raw_input("input element %d: "%i)
#		arr.append(int(val))
	sort(arr)
	print arr

main()
