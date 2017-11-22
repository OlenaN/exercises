#
# find the least number of changes required to make word b into word a
# eg: venmo -> venom has a distance of 2
#


#!usr/bin/python

import sys

a = sys.stdin.readline()
b = sys.stdin.readline()


# a is correct
# b is incorrect
def editDistance(a , b):
	
	if (a == b):
		return 0
	if (len(a) == 0 or len(b) == 0):
		return max(len(a), len(b))
		
	if (a[0] == b[0]):
		return editDistance(a[1:], b[1:])
	
	change = editDistance(a[1:], b[1:])
	add = editDistance(a[1:], b)
	subtract = editDistance(a, b[1:])
	
	return 1 + min(change, add, subtract)
			
print(editDistance(a, b))
