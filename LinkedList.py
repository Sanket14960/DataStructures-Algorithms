
class linkedListNode:
	def __init__(self, value, nextNode=None, previousNode=None):
		self.value = value
		self.nextNode = nextNode
		self.previousNode = previousNode
		
class linkedList:
	def __init__(self, head=None, tail=None, count=0):
		self.head = linkedListNode(head)
		self.tail = self.head
		self.count = 1


# O(1)
	def append(self, addedValue):
		newNode = linkedListNode(addedValue)
		
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			newNode = linkedListNode(addedValue)
			newNode.previousNode = self.tail
			
			self.tail.nextNode = newNode
			self.tail = newNode
		self.count += 1
# O(1)
	def prepend(self, addedValue):

		newNode = linkedListNode(addedValue)

		self.head.previousNode = newNode
		newNode.nextNode = self.head
		self.head = newNode

#O(n)
	def lookup(self):

		currentNode = self.head

		while currentNode != None:
			print(currentNode.value)
			currentNode = currentNode.nextNode

#O(n)
	def reverse(self):
		
		currentNode = self.tail

		while currentNode != None:
			print(currentNode.value)
			currentNode = currentNode.previousNode

#O (n)
	def insert(self, addedValue, index):

		currentNode = self.head
		newNode = linkedListNode(addedValue)

		for i in range(index - 1):
			currentNode = currentNode.nextNode

		newNode.nextNode = currentNode.nextNode
		
		currentNode.nextNode.previousNode = newNode
		currentNode.nextNode = newNode

		newNode.previousNode = currentNode

		self.count += 1

#O (n)
	def delete(self, index):

		if index + 1 != self.count and index != 0:
		
			currentNode = self.head
			
			for i in range(index):
				currentNode = currentNode.nextNode
	
			currentNode.previousNode.nextNode = currentNode.nextNode
			currentNode.nextNode.previousNode = currentNode.previousNode

		elif index == 0:

			currentNode = self.head
			
			for i in range(1):
				currentNode = currentNode.nextNode

			self.head = currentNode
			currentNode.previousNode.nextNode = None
			currentNode.previousNode = None		
	
		else: 
			
			currentNode = self.head
			
			for i in range(index):
				currentNode = currentNode.nextNode

			currentNode.previousNode.nextNode = None 
			currentNode.previousNode = None

		self.count -= 1

#O(n)
	def reverseList(self):
		currentNode = self.tail
		while currentNode != None:
			nxtNode = currentNode.nextNode
			prvNode = currentNode.previousNode
			currentNode.nextNode = prvNode
			currentNode.previousNode = nxtNode
			if currentNode == self.tail:
				self.head = currentNode
			elif currentNode == self.head:
				self.tail = currentNode
			currentNode = prvNode
		
emptyList = linkedList()
