#
# Find the smallest range which still containts at least one element from each list when passed a list of lists
#


#!usr/bin/python

def minRange(listOfLists):

	k = len(listOfLists)
	listRemaining = 1
	firstpass = 1
	bestMax = 0
	bestMin = 0
	while(listRemaining):
		maxList = 0
		minList = 0
		for j in range(0, k):
			if len(listOfLists[j]) > 1:
				if listOfLists[j][0] < listOfLists[minList][0]:
					minList = j
				if listOfLists[j][0] > listOfLists[maxList][0]:
					maxList = j
		
		if firstpass:
			firstpass = 0
			bestMax = listOfLists[maxList][0]
			bestMin = listOfLists[minList][0]
		
		elif ((maxList != minList) and (listOfLists[maxList][0] - listOfLists[minList][0]) < (bestMax - bestMin)):
			bestMax = listOfLists[maxList][0]
			bestMin = listOfLists[minList][0]
			
		if len(listOfLists[minList]) > 1:
			del listOfLists[minList][0]
		else:
			listRemaining = 0
	
	print("min is " + str(bestMin))
	print("max is " + str(bestMax))
				
				
				
lists = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
minRange(lists)
