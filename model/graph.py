import matrix	# Para instanciar la Matriz de Adyacencia/Incidencia

class Graph:
	"""Clase que representa un grafo en un determinado momento
	Utiliza la Matriz de Adyacencia/Incidencia"""
	
	def __init__(self):
		self.__matrix = Matrix(1)
		self.__nodes = 1
	
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
	
	def add_node(self):
		pass
	
	def del_node(self):
		pass
	
	def change_relation(self):
		pass
	
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
		matrix = 
		for i in cantNodos:
			if self.degree(i) != (cantNodos - 1):
				return False
		return True
	
	def bipartite(self):
		pass
	
	def degree(self, node):
		"""Para un nodo 'node':
		Retorna el grado del nodo"""
		if self.__validate_target(node):
			return self.__matrix.num_relations()
		return None
