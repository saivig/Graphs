class Graph:
	def __init__(self,edgeList=[],vertList=[],directed=False):
		self.vertList={}
		self.numVert = 0
		self.directed = directed
		if len(edgeList)!=0:
			self.addEdges(edgeList)
		else:
			self.addVerts(vertList)
		
	def addEdge(self,frm,to,wt=1):
		if self.directed:
			if frm not in self.vertList:
				self.vertList[frm]={to:wt}
				self.numVert+=1
			else:
				self.vertList[frm][to]=wt

			if to not in self.vertList:
				self.vertList[to]={}
				self.numVert+=1

		else:
			if frm not in self.vertList:
				self.vertList[frm]={to:wt}
				self.numVert+=1
			else:
				self.vertList[frm][to]=wt

			if to not in self.vertList: 
				self.vertList[to]={frm:wt}
				self.numVert+=1
			else:
				self.vertList[to][frm]=wt

	def addEdges(self,edgeList=[]):
		if len(edgeList)==0:
			raise "addEdges format is [(a,b,2),...]"
		else:
			if len(edgeList[0])==2:
				for tupl in edgeList:
					self.addEdge(tupl[0],tupl[1])
			elif len(edgeList[0])==3:
				for tupl in edgeList:
					self.addEdge(tupl[0],tupl[1],tupl[2])
			else:
				raise "Edge Tuple Size Can be only 2(for unDWeighted) & 3(for Weighted)"
	def addVert(self,vert):
		if vert in self.vertList:
			print "Vertex Already Exist ignoring Operation"
		else:
			self.vertList[vert] = {}
			self.numVert+=1
	def addVerts(self,vertL = []):
		for vert in vertL:
			addVert(vert)

	def show(self):
		isDir = "Directed" if self.directed else "unDirected"
		print self.vertList
		print "Number of Vertices in Graph:",self.numVert,",Type of Graph:",isDir


G = Graph([(1,2),(2,3),(4,5)])
G.show()
G.addEdges([(4,6)])
G.show()
