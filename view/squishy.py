
try:
	from Tkinter import *
except:
	print "PARA EJECUTAR GRAPHPY NECESITAS TK INSTALADO EN TU SO"


class Node:

	def __init__(self, id=-1, position=None, label=None):
		self.__id = id
		self.__label = label
		self.__position = position
			
	def setLabel(self, newLabel):
		try:
			self.__label = newLabel
			return True
		except:
			return False
	
	def getLabel(self):
		try:
			return self.__label
		except:
			return None
	
	def setId(self, newId):
		try:
			self.__id = newId
			return True
		except:
			return False

	def getId(self):
		try:
			return self.__id
		except:
			return None
	
	def setPosition(self, newPosition):
		try:
			self.__position = newPosition
			return True
		except:
			return False

	def getPosition(self):
		try:
			return self.__position
		except:
			return None

	def __str__(self):
		return "NODO ID: {0:d}\n".format(self.__id)


class Edge:
	
	def __init__(self, weight, connection):
		self.__weight = weight
		self.__connection = connection
	
	def setConnection(self, newConnection):
		try:
			self.__connection = newConnection
			return True
		except:
			return False
	
	def getConnection(self):
		try:
			return self.__connection
		except:
			return None
	
	def setWeight(self, newWeight):
		try:
			self.__weight = newWeight
			return True
		except:
			return False
	
	def getWeight(self):
		try:
			return self.__weight
		except:
			return None
	
	def __str__(self):
		return  "ARISTA CONEXION : ({0:d},{1:d})\n ".format(self.__conexion[0],self.__conexion[1])

class Graph:

	def __init__(self):
		self.__nodes = []
		self.__edges = []
	
	def nuevoNode(self, id, et, pos):
		try:
			tmp = Node(id,pos,et)
			self.__nodes.append(tmp)
			return True
		except:
			return False
	
	def nuevaEdge(self, weight,connection):
		try:
			tmpEdge = Edge(weight,connection)
			self.__edges.append(tmpEdge)
			return True
		except:
			return False
	
	def getNodes(self):
		return self.__nodes
	
	def getEdges(self):
		return self.__edges
	
	def delNode(self, idTarget):
		try:
			self.__nodes.remove(idTarget)
			return True
		except:
			return False

	def delEdge(self, edgeTarget):
		try:
			self.__aristas.remove(edgeTarget)
			return True
		except:
			return False
	
	def getNode(self, idTarget):
		try:
			for i in self.__nodes:
				if idTarget == i.getId():
					return i
		except:
			return None
	
	def updateEdges(self,old, newId):
		for i in self.__edges:
			connection = i.getConnection()
			if connection[0] == old:
				new = (newId,connection[1])
				i.setConnection(new)
			elif connection[1] == old:
				new = (connection[0],newId)
				i.setConnection(nuevo)
		

class Squishy:

	def __init__(self):
		# estado 1 -> mover nodos
		# estado 2 -> agrega nodos
		# estado 3 -> agrea arista
		self.__graph = Graph()
		tmp = Tk()
		self.__drawArea = Canvas(tmp,width=500, height=500)
		self.__drawArea.pack()
		self.__drawArea.bind("<B1-Motion>",self.__onMotion)
		self.__drawArea.bind("<Button-3>",self.__onBackClick)
		self.__drawArea.bind("<Double-Button-1>", self.__onDoubleClick)
		self.__status = 1
		self.__widgets = []
		self.__tmpId =  None

	def throwSquishy(self):
		try:
			mainloop()
		except:
			return False
	
	def getGraph(self):
		try:
			return self.__graph
		except:
			return None
	
	def getPicture(self, strRuta):
		pass
	
	def setStatus(self, newStatus):
		try:
			self.__status = newStatus
			return True
		except:
			return False
	
	def getStatus(self):
		return self.__status
	
	def setGraph( self, newGraph):
		try:
			self.__graph = newGraph
			return True
		except:
			return False
	
	def __draw(self):
		canvas = self.__drawArea
		nodes = self.__grafo.getNodes()
		edges = self.__grafo.getEdges()
		cavas.delete(ALL)
		for i in nodoes:
			pos = i.getPosition()
			supIzX = pos[0] - 10
			supIzY = pos[1] - 10
			infDerx = pos[0] + 10
			infDerY = pos[1] + 10 
			tmpId = canvas.create_oval(supIzX,supIzY,infDerx,infDerY,fill='black')
			id = i.getId()
			i.setId(tmpId)
			self.__grafo.updateEdges(id,tmpId)


		for i in aristas:
			conectados = i.getConexion()
			nod1 = self.__grafo.getNodo(conectados[0])
			nod2 = self.__grafo.getNodo(conectados[1])
			pos1 = nod1.getPosicion()
			pos2 = nod2.getPosicion()
			lienzo.create_line(pos1[0],pos1[1],pos2[0],pos2[1],arrow=LAST)
	
	def __onBackClick(self, evento):
		self.__tmpId = None
		supIzqX = evento.x - 10
		supIzqY = evento.y - 10
		infDerX = evento.x + 10
		infDerY = evento.y + 10
		id = self.__drawArea.create_oval(supIzqX,supIzqY,infDerX,infDerY,fill='black')
		self.__grafo.nuevoNodo(id,"Nuevo",(evento.x,evento.y))
		self.__dibujar()
	
	def __onMotion(self,evento):
		self.__tmpId = None
		can = self.__drawArea
		supIzqX = evento.x - 15
		supIzqY = evento.y - 15
		infDerX = evento.x + 15
		infDerY = evento.y + 15
 		elemento = can.find_overlapping(supIzqX,supIzqY,infDerX,infDerY)
		if len(elemento) >=1 :
			if can.type(elemento[0]) == "oval":
				nodo = self.__grafo.getNodo(elemento[0])
				nodo.setPosicion((evento.x,evento.y))
				self.__dibujar()
	
	def __onDoubleClick(self, evento):
		can = self.__drawArea
		supIzqX = evento.x - 15
		supIzqY = evento.y - 15
		infDerX = evento.x + 15
		infDerY = evento.y + 15
 		elementos = can.find_overlapping(supIzqX,supIzqY,infDerX,infDerY)
		if len(elementos) >= 1:
			if can.type(elementos[0]) == "oval":
				if self.__tmpId is None:
					self.__tmpId = elementos[0]
				else:
					if self.__tmpId != elementos[0]:
						conexion = (self.__tmpId, elementos[0])
						self.__grafo.nuevaArista(0,conexion)
						self.__tmpId = None
						self.__dibujar()
					else:
						self.__tmpId = None
			


a = Squishy()
a.lanzarSquishy()

		

	

		

