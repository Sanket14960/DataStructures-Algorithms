class linkedListNode:
	def __init__(self, value, nextNode=None, previousNode=None):
		self.value = value
		self.nextNode = nextNode
		self.previousNode = previousNode
		
class Stack:
	def __init__(self, top=None, bottom=None, length=0):
		self.top = linkedListNode(top)
		self.bottom = self.top
		self.length = 1

	def isEmpty(self):
		if self.top != None:
			print(f"Stack has {self.length} node.")
		else:
			print("Stack is empty.")
			
	def peek(self):
		if self.length > 0:
			currentNode = self.top
			while currentNode != None:
				print(currentNode.value)
				currentNode = currentNode.previousNode
				
		else:
			print("Stack is empty.")

	def push(self, value):
		newNode = linkedListNode(value)
		if self.length == 0:
			self.top = linkedListNode(value)
			self.bottom = self.top
		else:
			newNode.previousNode = self.top
			self.top.nextNode = newNode
			self.top = newNode
	
		self.length += 1

	def pop(self):
		if self.length == 1:
			self.top = None
			self.bottom = None
		else:
			self.top.previousNode.nextNode = None
			self.top = self.top.previousNode
	
		self.length -= 1
