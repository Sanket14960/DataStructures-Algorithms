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
		
# 	def delete(self, value): 

# 		findNode = lookup(value)

# 		if findNode.left == True and findNode.right == True:
# 			if findNode.left.value > findNode.right.value:

	def breadthFirstSearch(self):
		currentNode = self.root
		list = []
		queue = []

		queue.append(currentNode)

		while len(queue) > 0:
			currentNode = queue.pop(0)
			list.append(currentNode.value)
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)
		
		return list

	def depthFirstSearchInOrder(self):
		return traverseInOrder(self.root, [])
	
	def depthFirstSearchPreOrder(self):
		return traversePreOrder(self.root, [])
	
	def depthFirstSearchPostOrder(self):
		return traversePostOrder(self.root, [])

# Recursive functions for DFS
def traverseInOrder(node, list):
	if node.left:
		 traverseInOrder(node.left, list)
	list.append(node.value)
	if node.right:
		 traverseInOrder(node.right, list)
	
	return list

def traversePreOrder(node, list):
	list.append(node.value)
	if node.left:
		 traversePreOrder(node.left, list)
	if node.right:
		 traversePreOrder(node.right, list)
	
	return list

def traversePostOrder(node, list):
	if node.left:
		 traversePostOrder(node.left, list)
	if node.right:
		 traversePostOrder(node.right, list)
	list.append(node.value)
	
	return list
			
emptyTree = BinarySearchTree()
