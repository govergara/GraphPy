
try:
	from Tkinter import *
except:
	print "PARA EJECUTAR GRAPHPY NECESITAS TK INSTALADO EN TU SO"



class Node:

	def __init__(self, id=-1, position=None, label=None):
		self.__id = id
		self.__label = label
		self.__position = position
			
	def set_label(self, newLabel):
		try:
			self.__label = newLabel
			return True
		except:
			return False
	
	def get_label(self):
		try:
			return self.__label
		except:
			return None
	
	def set_id(self, newId):
		try:
			self.__id = newId
			return True
		except:
			return False

	def get_id(self):
		try:
			return self.__id
		except:
			return None
	
	def set_position(self, newPosition):
		try:
			self.__position = newPosition
			return True
		except:
			return False

	def get_position(self):
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
	
	def set_connection(self, newConnection):
		try:
			self.__connection = newConnection
			return True
		except:
			return False
	
	def get_connection(self):
		try:
			return self.__connection
		except:
			return None
	
	def set_weight(self, newWeight):
		try:
			self.__weight = newWeight
			return True
		except:
			return False
	
	def get_weight(self):
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
	
	def new_node(self, id, et, pos):
		try:
			tmp = Node(id,pos,et)
			self.__nodes.append(tmp)
			return True
		except:
			return False
	
	def new_edge(self, weight,connection):
		try:
			tmpEdge = Edge(weight,connection)
			self.__edges.append(tmpEdge)
			return True
		except:
			return False
	
	def get_nodes(self):
		return self.__nodes
	
	def get_edges(self):
		return self.__edges
	
	def del_node(self, idTarget):
		try:
			self.__nodes.remove(idTarget)
			return True
		except:
			return False

	def del_edge(self, edgeTarget):
		try:
			self.__aristas.remove(edgeTarget)
			return True
		except:
			return False
	
	def get_node(self, idTarget):
		try:
			for i in self.__nodes:
				if idTarget == i.get_id():
					return i
		except:
			return None
	
	def update_edges(self,old, newId):
		for i in self.__edges:
			connection = i.get_connection()
			if connection[0] == old:
				new = (newId,connection[1])
				i.set_connection(new)
			elif connection[1] == old:
				new = (connection[0],newId)
				i.set_connection(new)
		

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
	

	def throw_squishy(self):
		mainloop()
		
	def get_graph(self):
		try:
			return self.__graph
		except:
			return None
	
	def get_picture(self, strRuta):
		pass
	
	def set_status(self, newStatus):
		try:
			self.__status = newStatus
			return True
		except:
			return False
	
	def get_status(self):
		return self.__status
	
	def set_sraph( self, newGraph):
		try:
			self.__graph = newGraph
			return True
		except:
			return False
	
	def __draw(self):
		canvas = self.__drawArea
		nodes = self.__graph.get_nodes()
		edges = self.__graph.get_edges()
		canvas.delete(ALL)
		for i in nodes:
			pos = i.get_position()
			supIzX = pos[0] - 10
			supIzY = pos[1] - 10
			infDerx = pos[0] + 10
			infDerY = pos[1] + 10 
			tmpId = canvas.create_oval(supIzX,supIzY,infDerx,infDerY,fill='black')
			id = i.get_id()
			i.set_id(tmpId)
			self.__graph.update_edges(id,tmpId)


		for i in edges:
			connected = i.get_connection()
			nod1 = self.__graph.get_node(connected[0])
			nod2 = self.__graph.get_node(connected[1])
			pos1 = nod1.get_position()
			pos2 = nod2.get_position()
			canvas.create_line(pos1[0],pos1[1],pos2[0],pos2[1],arrow=LAST)
	
	def __onBackClick(self, event):
		self.__tmpId = None
		supIzqX = event.x - 10
		supIzqY = event.y - 10
		infDerX = event.x + 10
		infDerY = event.y + 10
		id = self.__drawArea.create_oval(supIzqX,supIzqY,infDerX,infDerY,fill='black')
		self.__graph.new_node(id,"Nuevo",(event.x,event.y))
		self.__draw()
	
	def __onMotion(self,event):
		self.__tmpId = None
		can = self.__drawArea
		supIzqX = event.x - 15
		supIzqY = event.y - 15
		infDerX = event.x + 15
		infDerY = event.y + 15
 		element = can.find_overlapping(supIzqX,supIzqY,infDerX,infDerY)
		if len(element) >=1 :
			if can.type(element[0]) == "oval":
				nodo = self.__graph.get_node(element[0])
				nodo.set_position((event.x,event.y))
				self.__draw()
	
	def __onDoubleClick(self, event):
		can = self.__drawArea
		supIzqX = event.x - 15
		supIzqY = event.y - 15
		infDerX = event.x + 15
		infDerY = event.y + 15
 		elements = can.find_overlapping(supIzqX,supIzqY,infDerX,infDerY)
		if len(elements) >= 1:
			if can.type(elements[0]) == "oval":
				if self.__tmpId is None:
					self.__tmpId = elements[0]
				else:
					if self.__tmpId != elements[0]:
						connection = (self.__tmpId, elements[0])
						self.__graph.new_edge(0,connection)
						self.__tmpId = None
						self.__draw()
					else:
						self.__tmpId = None
			

		

	

		

