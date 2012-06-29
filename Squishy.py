try:
	from Tkinter import *
except:
	print "PARA EJECUTAR GRAPHPY NECESITAS TK INSTALADO EN TU SO"


class Nodo:

	def __init__(self, id=-1, posicion=None, etiqueta=None):
		self.__id = id
		self.__etiqueta = etiqueta
		self.__posicion = posicion
	
	def setEtiqueta(self, nuevaEtiqueta):
		try:
			self.__etiqueta = nuevaEtiqueta
			return True
		except:
			return False
	
	def getEtiqueta(self):
		try:
			return self.__etiqueta
		except:
			return None
	
	def setId(self, nuevoId):
		try:
			self.__id = nuevoId
			return True
		except:
			return False

	def getId(self):
		try:
			return self.__id
		except:
			return None
	
	def setPosicion(self, nuevaPosicion):
		try:
			self.__posicion = nuevaPosicion
			return True
		except:
			return False
	def getPosicion(self):
		try:
			return self.__posicion
		except:
			return None
	def __str__(self):
		return "NODO ID: {0:d}\n".format(self.__id)


class Arista:
	
	def __init__(self, peso, conexion):
		self.__peso = peso
		self.__conexion = conexion
	
	def setConexion(self, nuevaConexion):
		try:
			self.__conexion = nuevaConexion
			return True
		except:
			return False
	
	def getConexion(self):
		try:
			return self.__conexion
		except:
			return None
	
	def setPeso(self, nuevoPeso):
		try:
			self.__peso = nuevoPeso
			return True
		except:
			return False
	
	def getPeso(self):
		try:
			return self.__peso
		except:
			return None
	
	def __str__(self):
		return  "ARISTA CONEXION : ({0:d},{1:d})\n ".format(self.__conexion[0],self.__conexion[1])

class Grafo:

	def __init__(self):
		self.__nodos = []
		self.__aristas = []
	
	def nuevoNodo(self, id, et, pos):
		try:
			tmp = Nodo(id,pos,et)
			self.__nodos.append(tmp)
			return True
		except:
			return False
	
	def nuevaArista(self, peso,conexion):
		try:
			tmpArista = Arista(peso,conexion)
			self.__aristas.append(tmpArista)
			return True
		except:
			return False
	
	def obtieneNodos(self):
		return self.__nodos
	
	def obtieneAristas(self):
		return self.__aristas
	
	def eliminaNodo(self, idTarget):
		try:
			self.__nodos.remove(idTarget)
			return True
		except:
			return False

	def elimiaArista(self, arisTarget):
		try:
			self.__aristas.remove(arisTarget)
			return True
		except:
			return False
	
	def getNodo(self, idTarget):
		try:
			for i in self.__nodos:
				if idTarget == i.getId():
					return i
		except:
			return None
	
	def actualizaVertices(self,antiguo, nuevoId):
		for i in self.__aristas:
			conexion = i.getConexion()
			if conexion[0] == antiguo:
				nuevo = (nuevoId,conexion[1])
				i.setConexion(nuevo)
			elif conexion[1] == antiguo:
				nuevo = (conexion[0],nuevoId)
				i.setConexion(nuevo)
		

class Squishy:

	def __init__(self):
		# estado 1 -> mover nodos
		# estado 2 -> agrega nodos
		# estado 3 -> agrea arista
		self.__grafo = Grafo()
		tmp = Tk()
		self.__areaDibujo = Canvas(tmp,width=500, height=500)
		self.__areaDibujo.pack()
		self.__areaDibujo.bind("<B1-Motion>",self.__onMotion)
		self.__areaDibujo.bind("<Button-3>",self.__onBackClick)
		self.__areaDibujo.bind("<Double-Button-1>", self.__onDoubleClick)
		self.__estado = 1
		self.__widgets = []
		self.__tmpId =  None

	def lanzarSquishy(self):
		try:
			mainloop()
		except:
			return False
	
	def obtieneGrafo(self):
		try:
			return self.__grafo
		except:
			return None
	
	def obtieneImagen(self, strRuta):
		pass
	
	def setEstado(self, nuevoEstado):
		try:
			self.__estado = nuevoEstado
			return True
		except:
			return False
	
	def getEstado(self):
		return self.__estado
	
	def setGrafo( self, nuevoGrafo):
		try:
			self.__grafo = nuevoGrafo
			return True
		except:
			return False
	
	def __dibujar(self):
		lienzo = self.__areaDibujo
		nodos = self.__grafo.obtieneNodos()
		aristas = self.__grafo.obtieneAristas()
		lienzo.delete(ALL)
		for i in nodos:
			pos = i.getPosicion()
			supIzX = pos[0] - 10
			supIzY = pos[1] - 10
			infDerx = pos[0] + 10
			infDerY = pos[1] + 10 
			tmpId = lienzo.create_oval(supIzX,supIzY,infDerx,infDerY,fill='black')
			id = i.getId()
			i.setId(tmpId)
			self.__grafo.actualizaVertices(id,tmpId)


		for i in aristas:
			conectados = i.getConexion()
			nod1 = self.__grafo.getNodo(conectados[0])
			nod2 = self.__grafo.getNodo(conectados[1])
			print "CONECTADOS SOSPECHOSOS",conectados[1]
			pos1 = nod1.getPosicion()
			pos2 = nod2.getPosicion()
			lienzo.create_line(pos1[0],pos1[1],pos2[0],pos2[1],arrow=LAST)
	
	def __onBackClick(self, evento):
		self.__tmpId = None
		supIzqX = evento.x - 10
		supIzqY = evento.y - 10
		infDerX = evento.x + 10
		infDerY = evento.y + 10
		id = self.__areaDibujo.create_oval(supIzqX,supIzqY,infDerX,infDerY,fill='black')
		self.__grafo.nuevoNodo(id,"NUevo",(evento.x,evento.y))
		self.__dibujar()
	
	def __onMotion(self,evento):
		self.__tmpId = None
		can = self.__areaDibujo
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
		can = self.__areaDibujo
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

		

	

		

