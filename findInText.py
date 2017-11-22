#
# Find if a substring can be made out of a bigger text, both in the correct order, and out of correct order
#

#!usr/bin/python

import sys

print("input main text:")
res = sys.stdin.readline()

print("input find text:")
find = sys.stdin.readline()


def straight_find(res, find):
	found_index = 0
	counter = 0
	indexes = []
	for char in res:
		if (found_index >= len(find) - 1):
			print("Entire 'Find Text' found at indexes:")
			print(indexes)
			break
			
		if (char == find[found_index]):
			indexes.append(counter)
			found_index += 1
			
		counter += 1
		
	if (found_index < len(find) - 1):
		print("It does not appear the Find Text is found in order in the main text")
	
	
	
def mix_find(res, find):
	
	main_dict = {}
	for char in res:
		if char in main_dict:
			main_dict[char] += 1;
		else:
			main_dict[char] = 1;

	find_dict = {}
	for char in find:
		if char in find_dict:
			find_dict[char] += 1;
		else:
			find_dict[char] = 1;
	
	found = 1
	for char in find:
		if char not in main_dict:
			found = 0
			break
		if char in main_dict:
			if main_dict[char] < find_dict[char]:
				found = 0
				break
	if not found:
		print("cannot make Find phrase from Main phrase")
	else:
		print("Success!")
			
	
	

straight_find(res, find)
#mix_find(res, find)
