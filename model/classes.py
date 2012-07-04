import copy	# Para hacer copias superficiales (shallow copies)

class Matrix:
	"""Clase que maneja la Matriz de Adyacencia/Incidencia"""
	
	def __init__(self, dim):
		self.__dimMatrix = dim
		self.__matrix = self.__set_matrix(dim)
	
	#
	#  PRIVATE METHODS
	#
	
	def __set_matrix(self, dim):
		"""Para una dimension "dim":
		Crea una nueva matriz. Todos sus elementos tienen el valor '0'
		Retorna la nueva matriz"""
		matrix = []
		for i in range(dim):
			matrix.append([])
			for j in range(dim):
				matrix[i].append(0)
		return matrix
	
	#
	#  PUBLIC METHODS
	#
	
	def get_dim(self):
		"""Retorna una copia 'superficial' (por valor) de la dimension"""
		dim = copy.copy(self.__dimMatrix)
		return dim
	
	def get_matrix(self):
		"""Retorna una copia 'superficial' (por valor) de la matriz"""
		matrix = copy.copy(self.__matrix)
		return matrix
	
	def add_entry(self):
		"""Agrega los datos de un nodo (nueva fila y columna)
		Retorna la nueva dimension de la matriz"""
		try:
			new = []
			for i in range(self.__dimMatrix):
				new.append(0)
			self.__matrix.append(new)
			self.__dimMatrix += 1
			for i in range(self.__dimMatrix):
				self.__matrix[i].append(0)
		except:
			return False
		return True
	
	def del_entry(self, target):
		"""Para un indice "target":
		Elimina los datos de un nodo (fila & columna respectiva)
		Retorna la nueva dimension de la matriz"""
		try:
			self.__matrix.pop(target)
			for i in range(self.__dimMatrix - 1):
				self.__matrix[i].pop(target)
			self.__dimMatrix -= 1
		except:
			return False
		return True
	
	def set_relation(self, row, col, value):
		"""Inserta un valor en el elemento (row, col) de la matriz"""
		self.__matrix[row][col] = value
	
	def symmetry(self):
		"""Determina si la matriz es simetrica o no
		Retorna 'True' si es simetrica, 'False' si no lo es"""
		dim = self.__dimMatrix
		for i in range(dim):
			for j in range(dim):
				if j <= i:
					continue
				if self.__matrix[i][j] != self.__matrix[j][i]:
					return False
		return True
	
	def num_relations(self, entry):
		dim = self.__dimMatrix
		relations = 0
		for i in range(dim):
			if self.__matrix[entry][i] != 0:
				relations += 1
		return relations


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
		if target >= 0 and target < dim:
			return True
		print "Invalid Target!"
		return False
	
	#
	#  PUBLIC METHODS
	#
	
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
			self.__matrix.set_relation(orig, dest, weight)
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
		for i in range(cantNodos):
			if self.degree(i) != (cantNodos - 1):
				return False
		return True
	
	def bipartite(self):
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
		return None
	
	def dijkstra(self, origin): # revisar error
		"""Para un nodo 'origin':
		Determina el camino mas corto desde 'origin' al resto de los nodos
		Retorna una lista de diccionarios con los datos de Dijkstra"""
		roads = []
		dim = self.__matrix.get_dim()
		matrix = self.__matrix.get_matrix()
		for i in range(dim):
			roads.append([])
			data = {'dist': -1, 'from': -1, 'set': 0}
			#  'dist': distancia acumulada, (-1) representa distancia infinita
			#  'from': nodo del que proviene la distancia menor, (-1) indica sin origen
			#  'set': (0) no visitado, (1) visitado como "destino", (2) utilizado como origen
			if i == origin:
				data['dist'] = 0
			roads[i].append(data)
		print roads
		for i in range(dim):
			for j in range(dim):
				roads[origin]['set'] = 2 # aqui esta el error
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

# Esto es para probar el algoritmo

g = Graph()
g.add_node()
g.add_node()
g.change_relation(0,1,7)
g.change_relation(1,0,7)
