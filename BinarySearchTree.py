class BinarySearchTreeNode:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		newNode = BinarySearchTreeNode(value)

		currentNode = self.root
		
		if self.root == None:
			self.root = newNode
		else: 
			
			while currentNode != None:
				if currentNode.value > newNode.value:
					if currentNode.left == None:
						break
					else:
						currentNode = currentNode.left
				else:
					if currentNode.right == None:
						break
					else:
						currentNode = currentNode.right

			if currentNode.value > newNode.value:
				currentNode.left = newNode
			else:
				currentNode.right = newNode

	def lookup(self, value):
		currentNode = self.root

		while currentNode != None:
			if currentNode == None:
				return None
				break
			elif currentNode.value == value:
				return currentNode
				break
			elif currentNode.value > value:
				currentNode = currentNode.left
			else:
				currentNode = currentNode.right
		
	def delete(self, value): 

		findNode = lookup(value)

		if findNode.left == True and findNode.right == True:
			if findNode.left.value > findNode.right.value:
			
emptyTree = BinarySearchTree()
