import math
import random
import time
import cairo
from gi.repository import Gtk,Gdk
import copy

class Node:

	def __init__(self, id=-1, position=None, label=None, color=None):
		"""Funcion Constructora que Genera un Nodo, requiere el ID_asociado, la posicion que
		es una Tupla, la etiqueta del Nodo y su color (Tupla RGB)"""
		self.__id = id
		self.__label = label
		self.__position = position
		self.__color = (0,0,0)
		self.__tam = 10
		self.__form = 1

	def set_form(self, newForm):
		"""Asigna una nueva Forma al Nodo"""
		try:
			self.__form = newForm
			return True
		except:
			return False

	def get_form(self):
		"""Obtiene la Forma del Nodo"""
		try:
			return self.__form
		except:
			return None
			
	def set_label(self, newLabel):
		"""Asigna una nueva Etiqueta al Nodo"""
		try:
			self.__label = newLabel
			return True
		except:
			return False
	
	def get_label(self):
		"""Obtiene el Valor de la Etiqueta del Nodo"""
		try:
			return self.__label
		except:
			return None

	def get_tam(self):
		"""Obtiene el Valor del grosor o del Tamanioo del Nodo"""
		try:
			return self.__tam
		except:
			return None

	def set_tam(self, newTam):
		"""Asigna un Nuevo Tamanio al Nodo"""
		try:
			self.__tam = newTam
		except:
			return False
	
	def set_id(self, newId):
		"""Asigna un nuevo Id al Nodo"""
		try:
			self.__id = newId
			return True
		except:
			return False

	def get_id(self):
		"""Obtiene el Valor del ID del Nodo"""
		try:
			return self.__id
		except:
			return False
	
	def set_position(self, newPosition):
		"""Asigna posicion al Nodo"""
		try:
			self.__position = newPosition
			return True
		except:
			return False

	def get_position(self):
		"""Retorna la Posicion de un Nodo"""
		try:
			return self.__position
		except:
			return None

	def set_color(self, newColor):
		"""Asigna una Tupla (Color RGB) al Nodo"""
		try:
			self.__color = newColor
			return True
		except:
			return False

	def get_color(self):
		"""Obtiene la Tupla (Color RGB) del nodo"""
		try:
			return self.__color
		except:
			return False

	def __str__(self):
		return "NODO ID: {0:d}\n".format(self.__id)


class Edge:
	
	def __init__(self, weight, connection):
		"""Funcion Constructora de la Clase Edge o Arista, recibe el Peso,
		una Tupla (Conexion de los 2 nodos unidos), color RGB y el tamanio o grosor
		OBS: la variable grosor se llama tam para no generar demasiadas funciones"""
		self.__weight = weight
		self.__connection = connection
		self.__color = (0,0,0)
		self.__tam = 2
		self.__form = 1
	
	def set_form(self, newForm):
		"""Asigna una nueva Forma a la Arista"""
		try:
			self.__form = newForm
			return True
		except:
			return False

	def get_form(self):
		"""Obtiene la Forma de la Arista"""
		try:
			return self.__form
		except:
			return None
			
	def set_connection(self, newConnection):
		"""Asigna una Nueva Conexion a la Arista"""
		try:
			self.__connection = newConnection
			return True
		except:
			return False
	
	def get_connection(self):
		"""Obtiene la Conexion de la Arista"""
		try:
			return self.__connection
		except:
			return None
	
	def set_tam(self, newTam):
		"""Asigna Un Nuevo grosor a  la Arista"""
		try:
			self.__tam = newTam
			return True
		except:
			return False

	def get_tam(self):
		"""Obtiene el Grosor de la Arista"""
		try:
			return self.__tam
		except:
			return None

	def set_label(self, newWeight):
		"""Asigna el Peso de la Arista"""
		try:
			self.__weight = newWeight
			return True
		except:
			return False
	
	def get_label(self):
		"""Obtiene el Peso de la Arista"""
		try:
			return self.__weight
		except:
			return None

	def set_color(self, newColor):
		"""Asigna un nuevo Color RGB a la Arista (Tupla)"""
		try:
			self.__color = newColor
			return True
		except:
			return False

	def get_color(self):
		"""Obtiene el Color de la Arista (Tupla)"""
		try:
			return self.__color
		except:
			return False

	def __str__(self):
		return  "ARISTA CONEXION : ({0:d},{1:d})\n ".format(self.__connection[0],self.__connection[1])

class Graph:

	def __init__(self):
		"""Constructor del Grafo, genera una Lista de nodos y de Arcos"""
		self.__nodes = []
		self.__edges = []
	
	def new_node(self, id, et, pos):
		"""Inserta un nuevo Nodo en el Grafo, recibe el ID, Etiqueta y la Posicion (x,y)"""
		try:
			tmp = Node(id,pos,et)
			self.__nodes.append(tmp)
			return True
		except:
			return False
	
	def new_edge(self, weight,connection):
		"""Inserta una Arista al Grafo, recibe el Peso de la arista y la Conexion 
		(ID Nodo Origen, ID Nodo Destino)"""
		try:
			tmpEdge = Edge(weight,connection)
			self.__edges.append(tmpEdge)
			return True
		except:
			return False
	
	def get_nodes(self):
		"""Obtiene la Lista de Nodos del Grafo"""
		return self.__nodes

	def get_edges(self):
		"""Obtiene la Lista de Aristas del Grafo"""
		return self.__edges
	
	def del_node(self, idTarget):
		"""Elimina un Nodo del grafo por su ID"""
		for i in self.__nodes:
			if i.get_id() == idTarget:
				for j in self.__edges:
					if j.get_connection()[0] == idTarget or j.get_connection()[1] == idTarget:
						self.__edges.remove(j)
				self.__nodes.remove(i)
				return True
		return False

	def del_edge(self, connection):
		"""Elimina una Arista del Grafo por su Conexion"""
		for i in self.__edges:
			if i.get_connection() == connection:
				self.__edges.remove(i)
				return True
		return False
	
	def get_node(self, idTarget):
		"""Obtiene un Nodo del Grafo por su ID"""
		try:
			for i in self.__nodes:
				if idTarget == i.get_id():
					return i
		except:
			return None
	
	def exist_edge(self, connection):
		"""Verifica si existe una Arista que Une a 2 Nodos (Conexion) en el Grafo"""
		for i in self.__edges:
			if i.get_connection() == connection:
				return True
		return False
	

class Squishy:

	def __init__(self, drawArea):
		"""Constructor de Squishy, recibe el area donde se puede Dibujar"""
		self.__graph = Graph()
		self.__drawArea = drawArea
		self.__connect_signals_draw()
		self.__status = 1
		self.__ind = 0
		self.__tmpSelection = None
		self.__frameInicio = (0,0) 
		self.__frameFinal = (0,0)
		self.__deltaI = (0,0)
		self.__deltaF = (0,0)
		self.__band = 0
		self.__sf = None
		self.__cntx = None
		self.__temp = []
		self.__malla = True
	
	
	def __connect_signals_draw(self):
		"""Conecta las Seniales de los Eventos"""
		self.__drawArea.connect("draw",self.repaint)
		self.__drawArea.add_events(Gdk.ModifierType.BUTTON1_MASK)
		self.__drawArea.add_events(Gdk.EventMask.BUTTON1_MOTION_MASK)
		self.__drawArea.add_events(Gdk.EventMask.BUTTON_RELEASE_MASK)
	
	def __draw(self, pdf = False, png = False, jpg = False):
		"""Dibuja en Pantalla o en Archivo el Grafo que se esta Creando"""
		if pdf is False and png is False and jpg is False:
			self.__sf=cairo.ImageSurface(cairo.FORMAT_ARGB32,740,500)
		else:
			self.__drawArea.queue_draw()
			if pdf is True:
				self.__sf = cairo.PDFSurface(self.__folder + self.__format,740,500)	
			if png is True:
				self.__sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 740, 500)
			if jpg is True:
				pass
		self.__cntx = cairo.Context(self.__sf)
		if self.__malla == True :
			self.__cntx.set_source_surface(cairo.ImageSurface.create_from_png("view/cuadricula.png"))
			self.__cntx.paint()
		print self.__graph.get_edges()
		for i in self.__graph.get_edges():
			self.__cntx.set_source_rgb(i.get_color()[0], i.get_color()[1], i.get_color()[2])
			tmpx1 = self.__graph.get_node(i.get_connection()[0]).get_position()[0]
			tmpy1 = self.__graph.get_node(i.get_connection()[0]).get_position()[1]
			tmpx2 = self.__graph.get_node(i.get_connection()[1]).get_position()[0]
			tmpy2 = self.__graph.get_node(i.get_connection()[1]).get_position()[1]
			self.__cntx.move_to(tmpx1,tmpy1)
			self.__cntx.set_line_width(i.get_tam())
			if i.get_form() == 1:
				self.__cntx.line_to(tmpx2,tmpy2)	
			if i.get_form() == 2:
				self.__cntx.set_dash([i.get_tam()*2,10], 0);
				self.__cntx.line_to(tmpx2,tmpy2)	
			if i.get_form() == 3:
				self.__cntx.set_dash([i.get_tam()*4, 10], 0);
				self.__cntx.line_to(tmpx2,tmpy2)	
			if i.get_form() == 4: 
				self.__cntx.set_dash([i.get_tam(),i.get_tam()], 2);
				self.__cntx.line_to(tmpx2,tmpy2)	

			self.__cntx.move_to(((tmpx1+tmpx2)/2)+i.get_tam(),((tmpy1+tmpy2)/2)+i.get_tam())
			self.__cntx.show_text(str(i.get_label()))
			self.__cntx.stroke()
		for i in self.__graph.get_nodes():
			self.__cntx.set_source_rgb(i.get_color()[0], i.get_color()[1], i.get_color()[2])
			if i.get_form() == 1:
				self.__cntx.arc(i.get_position()[0],i.get_position()[1], i.get_tam(), 0, 2*math.pi)
				self.__cntx.fill()
			if i.get_form() == 2:
				self.__cntx.rectangle(i.get_position()[0]-i.get_tam(), i.get_position()[1]-i.get_tam(),i.get_tam()*2,i.get_tam()*2)
				self.__cntx.fill()
			self.__cntx.move_to(i.get_position()[0]+i.get_tam(),i.get_position()[1]-i.get_tam())
			self.__cntx.show_text(i.get_label())
		if self.__ind == 2:
			self.__cntx.set_source_rgba(0, 0, 255, 0.3)
			self.__change_delta()
			tmpx = self.__frameFinal[0] - self.__frameInicio[0]
			tmpy = self.__frameFinal[1] - self.__frameInicio[1]
			self.__cntx.rectangle(self.__frameInicio[0], self.__frameInicio[1], tmpx, tmpy)
			self.__cntx.fill()
		return self.__sf
		
		
	def get_graph(self):
		"""Obtiene una Copia del Grafo"""
		try:
			return copy.deepcopy(self.__graph)
		except:
			return None

	def get_graph_super(self):
		"""Obtiene el Grafo Original"""
		try:
			return self.__graph
		except:
			return False
	
	def get_picture(self, strRuta):
		"""Funcion que aun no es implementada"""
		pass
	
	def set_status(self, newStatus):
		"""Cambia el estado de Squishy:
		1.- Crear Nodo
		2.- Cursor
		3.- Crear Arista
		4.- Seleccionar (mover, copiar y pegar)"""
		try:
			self.__tmpSelection = None
			self.__status = newStatus
			return True
		except:
			return False
	
	def get_status(self):
		"""Obtiene el Estado de Squishy"""
		return self.__status
	
	def set_graph( self, newGraph):
		"""Funcion que asigna un nuevo grafo al grafo actual
		OBS: se utiliza para botones rehacer y deshacer"""
		try:
			self.__graph = copy.deepcopy(newGraph)
			print "seteando grafo",self.__graph
			self.__drawArea.queue_draw()
			return True
		except:
			return False

	def get_ind(self):
		"""Obtiene un valor que indica si se esta Seleccionando un Area (1)
		y si no se esta seleccionando (0)"""
		return self.__ind

	def set_malla(self, newState):
		"""Asigna a Squishy si en la vista se quiere ver una malla de Ayuda en el Dibujo
		TRUE or FALSE"""
		self.__malla = newState

	def insert_new_node(self, data=None, label="nuevo"):
		"""Funcion que agrega un nodo nuevo visualmente y lo agrega al grafo"""
		self.__graph.new_node(random.randint(1,1000),label,(data.x,data.y))
		self.__drawArea.queue_draw()

	def paste_node(self, data, label, color, tamanio, forma):
		"""Funcion que Pega un Nodo que esta en una Papelera"""
		self.__graph.new_node(random.randint(1,1000),label,data)
		tmp = self.get_node(data[0],data[1])
		tmp.set_color(color)
		tmp.set_tam(tamanio)
		tmp.set_form(forma)
		self.__drawArea.queue_draw()

	def insert_edge(self, data=None):
		"""Funcion que inserta una Arista entre dos Nodos y agrega la Arista al grafo"""
		if self.__tmpSelection == None:
			self.__tmpSelection = self.__over_nodes(data.x, data.y)
		else:
			other = self.__over_nodes(data.x, data.y)
			if other is None:
				self.__tmpSelection = None
			else:
				connected = (self.__tmpSelection.get_id(),other.get_id())
				if not self.__graph.exist_edge(connected):
					self.__graph.new_edge(0,connected)
					self.__drawArea.queue_draw()
			self.__tmpSelection = None
			other = None

	def select_area(self, data=None):
		"""Funcion que setea el punto de inicio del area de seleccion
		y ademas sirve para obtener el punto de inicio del delta de Movimiento"""
		if self.__ind == 0:
			self.__frameInicio = self.__drawArea.get_pointer()
			self.__ind = 2
		if self.__ind == 1:
			self.__deltaI = self.__drawArea.get_pointer()

	def select_area_end(self):
		"""Funcion que setea el punto final del area de seleccion"""
		self.__ind = 1
		self.__drawArea.queue_draw()

	def reset(self):
		"""Funcion que aplica un reset a variables que se utilizan de diferentes maneras
		en cada Estado de Squishy"""
		print "reset"
		self.__ind = 0
		self.__tmpSelection = None
		del self.__temp[:]

	def move_node(self, data=None):
		"""Funcion que mueve un Nodo Seleccionado"""
		self.__tmpSelection = None
		if self.__over_nodes(data.x,data.y) != False:
			self.__over_nodes(data.x,data.y).set_position((data.x,data.y))
		self.__drawArea.queue_draw()

	def move_selected(self, data=None):
		"""Funcion que mueve todos los Nodos que se encuentran en un Area Seleccionada"""
		if self.__ind == 1:
			if self.__tmpSelection == None:
				self.__over_select()
				self.__tmpSelection = True
			self.__selectMove(data)
			self.__drawArea.queue_draw()
			self.__deltaI = (data.x, data.y)

	def __over_nodes(self,x ,y ):
		"""Obtiene el Nodo que esta en la Posicion x,y"""
		for i in self.__graph.get_nodes():
			if i.get_form() == 1:
				resultado = (x-i.get_position()[0])*(x-i.get_position()[0]) + (y-i.get_position()[1])*(y-i.get_position()[1])
				if resultado <= (i.get_tam())*(i.get_tam()):
					return i
			if i.get_form() == 2:
				if x >= i.get_position()[0]-i.get_tam()/2 and x <= i.get_position()[0]+i.get_tam()/2:
					if y >= i.get_position()[1]-i.get_tam()/2 and y <= i.get_position()[1]+i.get_tam()/2:
						return i
		return False
	
	def get_node(self, x,y):
		"""Obtiene la Funcion over_nodes"""
		return self.__over_nodes(x,y)

	def __over_select(self):
		"""Agrega a una Lista todos los nodos que estan sobre un Area Seleccionada"""
		print self.__frameInicio, self.__frameFinal
		for i in self.__graph.get_nodes():
			pos = i.get_position()
			print "--",pos
			if(pos[0] >= self.__frameInicio[0] and pos[0] <= self.__frameFinal[0]):
				if(pos[1] >= self.__frameInicio[1] and pos[1] <= self.__frameFinal[1]):
					self.__temp.insert(len(self.__temp), i)

	def __over_edge(self, x, y ):
		"""Funcion que obtiene el Arco que esta sobre el punto x,y"""
		for i in self.__graph.get_edges():
			id_nodos = i.get_connection()
			for j in self.__graph.get_nodes():
				if j.get_id() == id_nodos[0]:
					tmpInicio = j.get_position()
				if j.get_id() == id_nodos[1]:
					tmpFinal = j.get_position()
			pend = ( tmpInicio[1] - tmpFinal[1] )/( tmpInicio[0] - tmpFinal[0])
			resultado = (pend*(x - tmpInicio[0]))-(y - tmpInicio[1])
			if resultado <= i.get_tam() and resultado >= -i.get_tam():
				if tmpInicio[0] < x and tmpFinal[0] > x:
					return i
				if tmpFinal[0] < x and tmpInicio[0] > x:
					return i
		return False

	def get_edge(self, data):
		"""Funcion que invoca a over_edge"""
		return self.__over_edge(data.x, data.y)

	def __selectMove(self, data=None):
		"""Mueve todos los nodos que estan en la lista de seleccionados"""
		for i in self.__temp:
			i.set_position((i.get_position()[0]+(data.x - self.__deltaI[0]),i.get_position()[1]+(data.y - self.__deltaI[1])))
	
	def _on_double_click(self, widget, data=None):
		"""Funcion no definida"""
		pass
    
	def __change_delta(self):
		"""Funcion que cambia deltas del area de seleccion"""
		x, y = self.__frameInicio
		w, z = self.__frameFinal
		if w < x:
			aux = w
			w = x
			x = aux
		if z < y:
			aux = z
			z = y
			y = aux
		self.__frameInicio = (x,y)
		self.__frameFinal = (w,z)

	def repaint(self, widget, event):
		"""Funcion que redibuja el area, UTILIZADA POR EVENTOS"""
		self.canvas = widget.get_window().cairo_create()
		self.canvas.set_source_surface(self.__draw())
		self.canvas.paint()
	
	def redrawing(self):
		"""Funcion utilizada para aplicar cambios en la vista, redibuja el Area"""
		self.__drawArea.queue_draw()

	def create_file(self, direction, format):
		"""Funcion que especifica que tipo de archivo se desea exportar o guardar"""
		self.__folder = direction
		self.__format = format
		if(format == '.pdf'):
			self.__draw(True, False, False)
		if(format == '.png'):
			self.__draw(False, True, False)
		if(format == '.jpg'):
			self.__draw(False, False, True)

	def get_over(self, data=None):
		"""Funcion que devuelve un valor al senialar en que posicion se encuentra el Mouse
		1.- Si esta en un Nodo
		2.- Si esta en una arista
		3.- Si esta en cualquier otra posicion"""
		if self.__over_nodes(data.x, data.y) != False:
			return 1
		if self.__over_edge(data.x, data.y) != False:
			return 2
		return 3

	def status_temp(self):
		self.__over_select()
		if len(self.__temp) != 0:
			return True
		else:
			return False

	def get_temp(self):
		try:
			return self.__temp
		except:
			return None

	def set_data(self):
		self.__frameFinal = self.__drawArea.get_pointer()
		self.__drawArea.queue_draw()


	

		

