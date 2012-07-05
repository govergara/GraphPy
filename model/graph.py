import matrix

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
		"""Para un nodo 'target':
		Determina si el nodo es valido (existe)
		Retorna 'True' si existe, 'False' si no existe"""
		dim = self.__matrix.get_dim()
		if target >= 0 and target < dim:
			return True
		print "Invalid Target!"
		return False
	
	#
	#  PUBLIC METHODS - BASIC FUNCTIONALITY
	#
	
	def add_node(self):
		"""Agrega un nuevo nodo sin conexiones
		Retorna el valor del metodo add_entry de la matriz"""
		return self.__matrix.add_entry()
	
	def del_node(self, node):
		"""Para un nodo 'node':
		Elimina el nodo 'node' del grafo
		Retorna 'False' si el nodo no a eliminar no existe
		Retorna el valor del metodo del_entry de la matriz en otro caso"""
		if self.__validate_target(node):
			return self.__matrix.del_entry(node)
		return False
	
	def change_relation(self, orig, dest, weight):
		"""Para dos indices 'orig' y 'dest', y un peso de camino 'Weight':
		Modifica (o setea) una relacion entre dos nodos
		Retorna 'False' si los indices no son validos, 'True' en otro caso"""
		if self.__validate_target(orig) and self.__validate_target(dest):
			self.__matrix.set_relation(orig, dest, weight)
			return True
		return False
	
	def get_matrix(self):
		"""Retorna una copia de la Matriz de Incidencia/Adyacencia"""
		return self.__matrix.get_matrix()
	
	def directed(self):
		"""Determina si el grafo es dirigido o no dirigido
		Retorna el valor del metodo 'symmetry' de la matriz asociada"""
		return self.__matrix.symmetry()
	
	def connected(self):
		"""Determina, utilizando Dijkstra, si el grafo es conexo o no
		Retorna 'True' si es conexo, 'False' si no lo es"""
		dim = self.__matrix.get_dim()
		for i in range(dim):
			tester = self.dijkstra(i)
			for j in range(dim):
				if tester[j]['set'] == 0:
					return False
		return True
	
	def complete(self):
		"""Determina si el grafo es completo o no
		Retorna 'True' si es completa, 'False' si no lo es"""
		cantNodos = self.__nodes
		for i in range(cantNodos):
			if self.degree(i) != (cantNodos - 1):
				return False
		return True
	
	def bipartite(self):
		"""Determina si el grafo es bipartito o no
		Retorna 'True' si es bipartito, 'False' si no lo es"""
		color1 = 1
		color2 = 2
		matrix = self.__matrix.get_matrix()
		dim = self.__matrix.get_dim()
		colored = []
		for i in range(dim):
			colored.append(0)
		
		for i in range(dim):
			for j in range(dim):
				if colored[i] == 0:
					colored[i] = 1
				if matrix[i][j] != 0:
					if colored[j] == 0 and colored[i] == 1:
						colored[j] = 2
					if colored[j] == 0 and colored[i] == 2:
						colored[j] = 1
					if colored[j] != 0 and colored[i] == colored[j]:
						return False
		return True
	
	def degree(self, node):
		"""Para un nodo 'node':
		Retorna el grado del nodo"""
		if self.__validate_target(node):
			return self.__matrix.num_relations(node)
		return 
	
	#
	#  PUBLIC METHODS - GRAPH ALGORITHMS
	#
	
	def dijkstra(self, origin):
		"""Para un nodo 'origin':
		Determina el camino mas corto desde 'origin' al resto de los nodos
		Retorna una lista de diccionarios con los datos de Dijkstra"""
		roads = []
		dim = self.__matrix.get_dim()
		matrix = self.__matrix.get_matrix()
		for i in range(dim):
			data = {'dist': -1, 'from': -1, 'set': 0}
			#  'dist': distancia acumulada, (-1) representa distancia infinita
			#  'from': nodo del que proviene la distancia menor, (-1) indica sin origen
			#  'set': (0) no visitado, (1) visitado como "destino", (2) utilizado como origen
			if i == origin:
				data['dist'] = 0
			roads.append(data)
		for i in range(dim):
			for j in range(dim):
				roads[origin]['set'] = 2
				if matrix[origin][j] != 0:
					accumulated = matrix[origin][j] + roads[origin]['dist']
					if roads[j]['set'] == 0:
						roads[j]['dist'] = accumulated
						roads[j]['from'] = origin
						roads[j]['set'] = 1
					elif roads[j]['set'] == 1 and accumulated < roads[j]['dist']:
						roads[j]['dist'] = accumulated
						roads[j]['from'] = origin
			menor = -1
			for j in range(dim):
				if roads[j]['set'] == 1:
					if menor == -1 and roads[j]['dist'] > 0:
						menor = j
					elif roads[j]['dist'] < roads[menor]['dist']:
						menor = j
			origin = menor
		return roads
	
	def kruskal(self):
		pass
	
	def path_hamilton():
		pass
	
	def path_euler():
		pass

# Esto es para probar el algoritmo

g = Graph()
g.add_node()
g.add_node()
g.change_relation(0,1,7)
g.change_relation(1,0,7)
