class Graph: 
	def __init__(self, numberOfNodes = -1, adjacentList = {}, edgeList = {}):
		self.numberOfNodes = numberOfNodes
		self.adjacentList = adjacentList

	def addVertex(self, node):
		if node not in self.adjacentList.keys():
			self.adjacentList.update({node: []})
			self.numberOfNodes += 1
		else: 
			pass
		
	def addEdge(self, node1, node2):

		if node1 not in self.adjacentList.get(node1):
			self.adjacentList[node1].append(node2)

		if node2 not in self.adjacentList.get(node2):
			self.adjacentList[node2].append(node1)


myGraph = Graph()

myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')


myGraph.addEdge('3','1')
myGraph.addEdge('3','4')
myGraph.addEdge('4','2')
myGraph.addEdge('4','5')
myGraph.addEdge('1','2')
myGraph.addEdge('1','0')
myGraph.addEdge('0','2')
myGraph.addEdge('6','5')
