import matrix	# Para instanciar la Matriz de Adyacencia/Incidencia

class Graph:
	"""Clase que representa un grafo en un determinado momento
	Utiliza la Matriz de Adyacencia/Incidencia"""
	
	def __init__(self):
		self.__matrix = Matrix(0)
		self.__nodes = 0
	
	#
	#  PRIVATE METHODS
	#
	
	def __validate_target(self, target):
		dim = self.__matrix.get_dim()
		if target >= 0 and target < dim
			return True
		print "Invalid Target!"
		return False
	
	#
	#  PUBLIC METHODS
	#
<<<<<<< HEAD
	def complete(self):
		"""Determina si la matriz (en nuestro caso el grafo) es completa o no
		Retorna 'True' si es completa, 'False' si no lo es"""
		dim = self.__matrix.__dimMatrix
		for i in dim:
			for j in dim:
				if j == i:
					continue
				elif self.__matrix[i][j] == 0:
					return False
		return True
		
	def degree(self,node):
		"""Devuelve el grado de un nodo seleccionado"""
		dim = self.__matrix.__dimMatrix
		c=0
		if nodo>dim:
			return false
		for i in dim:
			if self.__matrix[i][node] ==1:
				c+=1
		return c
=======
	
	def add_node(self):
		return self.__matrix.add_entry()
	
	def del_node(self, node):
		if self.__validate_target(node):
			return self.__matrix.del_entry(node)
		return False
	
	def change_relation(self, orig, dest, weight):
		"""Para dos indices 'orig' y 'dest', y un peso de camino 'Weight':
		Modifica (o setea) una relacion entre dos nodos
		Retorna 'False' si los indices no son validos, 'True' en otro caso"""
		if self.__validate_target(orig) and self.__validate_target(dest):
			self.__matrix.set_entry(orig, dest, weight)
			return True
		return False
	
	def get_matrix(self):
		"""Retorna una copia de la Matriz de Incidencia/Adyacencia"""
		return self.__matrix.get_matrix()
	
	def directed(self):
		"""Determina si el grafo es dirigido o no dirigido"""
		return self.__matrix.symmetry()
	
	def connected(self):
		pass
	
	def complete(self):
		"""Determina si el grafo es completo o no
		Retorna 'True' si es completa, 'False' si no lo es"""
		cantNodos = self.__nodes
		for i in cantNodos:
			if self.degree(i) != (cantNodos - 1):
				return False
		return True
	
	def bipartite(self):
		color1 = 1
		color2 = 2
		matrix = self.__matrix.get_matrix()
		dim = self.__matrix.get_dim()
		colored = []
		for i in dim:
			colored.append(0)
		
		for i in dim:
			for j in dim:
				if colored[i] == 0:
					colored[i] = 1
				if matrix[i][j] != 0:
					if colored[j] == 0 and colored[i] == 1
						colored[j] == 2
					if colored[j] == 0 and colored[i] == 2
						colored[j] == 1
					if colored[j] != 0 and colored[i] == colored[j]
						return False
		return True
	
	def degree(self, node):
		"""Para un nodo 'node':
		Retorna el grado del nodo"""
		if self.__validate_target(node):
			return self.__matrix.num_relations()
		return None
>>>>>>> 8703c6a828e61b3ea85c3a0a03d32a1f3cafec01
