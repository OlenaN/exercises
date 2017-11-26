#!usr/bin/python

class Node:
	def __init__ (self, value):
		self.next = None
		self.value = value
		
	def getValue(self):
		return self.value
		
	def getNext(self):
		return self.next
		
	def setValue(self, newValue):
		self.value = newValue
	
	def setNext(self, newNext):
		self.next = newNext

		
class List:		
	
	def __init__(self):
		self.head = None
		
	def getHead(self):
		return self.head
		
	def setHead(self, newHead):
		self.head = newHead
		
	def printList(self):
		curr = self.head
		print("Start of list")
		while(curr != None):
			print(curr.value)
			curr = curr.next
		
		print("End of list")
	
	def addToFront(self, value):
		newNode = Node(value)
		newNode.next = self.head
		self.head = newNode
		
		
def recursivelyDelNode(node, k):
	
	if k < 1:
		return node
	
	if node == None:
		return None
		
	#base case
	if k == 1:
		temp = node.next
		del(node)
		return temp
	
	node.next = recursivelyDelNode(node.next, k-1)
	return node
	
		
		
newList = List()
newList.addToFront(5)
newList.addToFront(4)
newList.addToFront(3)
newList.addToFront(2)
newList.addToFront(1)

newList.head = recursivelyDelNode(newList.head, 3)
newList.printList()
