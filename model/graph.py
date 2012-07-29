from copy import copy	# Para hacer copias superficiales (shallow copies)
from matrix import *

class Graph:
	"""Clase que representa un grafo en un determinado momento
	Utiliza la Matriz de Adyacencia/Incidencia"""
	
	def __init__(self, nodes):
		self.__matrix = Matrix(nodes)
		self.__nodes = nodes
	
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
		return False
	
	def __connected_matrix(self, matrix):
		"""Para una matriz 'matrix':
		Determina, utilizando Busqueda en Profundidad, si el grafo es conexo o no
		Retorna 'True' si es conexo, 'False' si no lo es"""
		dim = len(matrix)
		for i in range(dim):
			tester = self.__breadthfirst_search(matrix, i)
			for j in range(dim):
				if tester[j]['set'] == 0:
					return False
		return True
	
	def __breadthfirst_search(self, matrix, origin):
		"""Para una matriz 'matrix' y un nodo 'origin':
		Realiza una busqueda en anchura
		Retorna una lista de diccionarios con la informacion recopilada"""
		status = []
		dim = len(matrix)
		for i in range(dim):
			data = {'dist': -1, 'from': -1, 'set': 0}
			#  'dist': distancia acumulada, (-1) representa distancia infinita
			#  'from': nodo del que proviene la distancia menor, (-1) indica sin origen
			#  'set': (0) no visitado, (1) visitado como "destino", (2) utilizado como origen
			if i == origin:
				data['dist'] = 0
			status.append(data)
		for i in range(dim):
			for j in range(dim):
				status[origin]['set'] = 2
				if matrix[origin][j] != 0:
					accumulated = matrix[origin][j] + status[origin]['dist']
					if status[j]['set'] == 0:
						status[j]['dist'] = accumulated
						status[j]['from'] = origin
						status[j]['set'] = 1
					elif status[j]['set'] == 1 and accumulated < status[j]['dist']:
						status[j]['dist'] = accumulated
						status[j]['from'] = origin
			menor = -1
			for j in range(dim):
				if status[j]['set'] == 1:
					if menor == -1 and status[j]['dist'] > 0:
						menor = j
					elif status[j]['dist'] < status[menor]['dist']:
						menor = j
			origin = menor
		return status
	
	def __get_path(self, status, target):
		"""Para un nodo 'target' y un resultado de __breadthfirst_search 'status':
		Guarda el menor camino recorrido para llegar a 'target' en 'path'
		Retorna el camino si 'target' existe, 'None' en otro caso"""
		if not self.__validate_target(target):
			return None
		if status[target]['from'] == -1:
			return None
		path = []
		temp = target
		while True:
			path.append(temp)
			temp = status[temp]['from']
			if temp == -1:
				break
		path.reverse()
		return path
	
	def __cicle(self, begin, matrix):
		"""Para un nodo a analizar 'begin' y una matriz 'matrix'
		Determina recursivamente si existe algun ciclo
		Retorna 'True' si existe un ciclo, 'False' si no existe"""
		father = begin
		actual = begin
		finished = False
		while not finished:
			for i in range( len(matrix) ):
				if i == father:
					continue
				if begin != father and matrix[actual][begin] != 0:
					return True
				if matrix[actual][i] != 0:
					father = actual
					actual = i
					break
				finished = True
		return False
	
	def __kruskal_algorithm(self, matrix):
		"""Para una matriz 'matrix':
		Obtiene el arbol recubridor minimo
		Retorna la matriz asociada al arbol, 'None' si no encuentra un arbol"""
		dim = len(matrix)
		kruskal = []
		for i in range(dim):
			kruskal.append([])
			for j in range(dim):
				kruskal[i].append(0)
		traveled = []
		
		while len(traveled) != dim or not self.__connected_matrix(kruskal):
			smaller = 0
			row = -1
			col = -1
			for i in range(dim):
				for j in range(dim):
					if matrix[i][j] != 0:
						if smaller == 0:
							row = i
							col = j
							smaller = matrix[i][j]
						elif smaller > matrix[i][j]:
							row = i
							col = j
							smaller = matrix[i][j]
			if smaller == 0:
				return None
			if traveled.count(row) == 0:
				traveled.append(row)
			if traveled.count(col) == 0:
				traveled.append(col)
			
			matrix[row][col] = 0
			matrix[col][row] = 0
			kruskal[row][col] = smaller
			kruskal[col][row] = smaller
			if self.__cicle(col, kruskal):
				kruskal[row][col] = 0
				kruskal[col][row] = 0
			if self.__cicle(row, kruskal):
				kruskal[row][col] = 0
				kruskal[col][row] = 0
		return kruskal
	
	def __hamilton_algorithm(self, actual, stack, paths):
		"""Para un nodo origen 'pivot', y una matriz 'matrix':
		Determina un recorrido para todos los nodos, sin repetirlos
		Retorna el camino encontrado, 'None' si no encuentra uno"""
		matrix = self.get_matrix()
		dim = self.__matrix.get_dim()
		stack.append(actual)
		if len(stack) == dim:
			temp = copy(stack)
			paths.append(temp)
		else:
			for i in range(dim):
				if stack.count(i) == 0 and matrix[actual][i] != 0:
					self.__hamilton_algorithm(i, stack, paths)
		stack.pop()
	
	def __edges(self):
		"""Retorna todas las aristas existentes en el grafo"""
		counter = 0
		matrix = self.__matrix.get_matrix()
		dim = self.__matrix.get_dim()
		for i in range(dim):
			for j in range(dim):
				if matrix[i][j] != 0:
					counter += 1
		return counter

	def __fleury(self, matrix, actual, array, path, edges, directed):
		"""Guarda en la variable 'array' todos los caminos eulerianos posibles"""
		dim = self.__matrix.get_dim()
		path.append(actual)
		if len(path) == (edges + 1):
			array.append(copy(path))
		else:
			for i in range(dim):
				if matrix[actual][i] != 0:
					if not directed:
						matrix[i][actual] = 0
					matrix[actual][i] = 0
					self.__fleury(matrix, i, array, path, edges, directed)
		if len(path) > 1:
			i = path[-2]
			if not directed:
				matrix[actual][i] = 1
			matrix[i][actual] = 1
		path.pop()
	
	def __filter(self,array):
		"""Para una lista 'array'
		Elimina caminos repetidos de la lista
		Incluye orden inverso y camino circular"""
		# revisa si array tiene caminos repetidos
		# el codigo se ve feo, supongo que se puede mejorar
		dim = self.__matrix.get_dim()
		for path in range( len(array) ):
			comparePath = path + 1
			while comparePath < len(array):
				i = j = 0
				while i < dim:
					if array[path][i] != array[comparePath][j]:
						j += 1
						if i > 0:
							break
					else:
						i += 1
						j += 1
						if j == dim:
							j = 0
				if i == dim:
					array.pop(comparePath)
					continue
				else:
					i = j = 0
					while i < dim:
						if array[path][i] != array[comparePath][j]:
							j += 1
							if i > 0:
								break
						else:
							i += 1
							j -= 1
							if j == -1:
								j = dim - 1
					if i == dim:
						array.pop(comparePath)
						continue
				comparePath += 1
	
	def __generic_degree(self, node, matrix):
		"""Para un nodo 'node', y una matriz 'matrix':
		Determina el grado de 'node'
		Retorna el grado, o'None' si 'node' no existe"""
		if not self.__validate_target(node):
			return None
		degree = 0
		for i in range( len(matrix) ):
			if matrix[node][i] != 0:
				degree += 1
		return degree
	
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
	
	def add_edge_dir(self, orig, dest, weight):
		"""Para dos indices 'orig' y 'dest', y un peso de camino 'weight':
		Modifica (o setea) una relacion dirigida entre ambos nodos
		Retorna 'False' si los indices no son validos, 'True' en otro caso"""
		if orig != dest:
			if self.__validate_target(orig) and self.__validate_target(dest):
				self.__matrix.set_entry(orig, dest, weight)
				return True
		return False
	
	def add_edge_ndir(self, node1, node2, weight):
		"""Para dos indices 'node1' y 'node2', y un peso de camino 'weight':
		Modifica (o setea) una relacion no dirigida entre ambos nodos
		Retorna 'False' si los indices no son validos, 'True' en otro caso"""
		if node1 != node2:
			if self.__validate_target(node1) and self.__validate_target(node2):
				self.__matrix.set_entry(node1, node2, weight)
				self.__matrix.set_entry(node2, node1, weight)
				return True
		return False
	
	def del_edge(self, node1, node2):
		"""Para dos nodos 'node1' y 'node2'
		Elimina la arista que une ambos nodos
		Retorna 'True' si fue eliminada, 'False' en otro caso"""
		if node1 != node2:
			if self.__validate_target(node1) and self.__validate_target(node2):
				if self.directed():
					self.__matrix.set_entry(node1, node2, 0)
				else:
					self.__matrix.set_entry(node1, node2, 0)
					self.__matrix.set_entry(node2, node1, 0)
				return True
		return False
	
	def get_matrix(self):
		"""Retorna una copia de la Matriz de Incidencia/Adyacencia"""
		return self.__matrix.get_matrix()
	
	def get_complementary(self):
		"""Retorna la Matriz del grafo complementario"""
		if self.directed():
			return None
		matrix = self.get_matrix()
		dim = self.__matrix.get_dim()
		complementary = []
		for i in range(dim):
			complementary.append([])
			for j in range(dim):
				if i == j:
					complementary[i].append(0)
					continue
				if matrix[i][j] == 0:
					complementary[i].append(1)
				else:
					complementary[i].append(0)
		return complementary
	
	def get_complete(self):
		"""Retorna la Matriz del grafo completo"""
		dim = self.__matrix.get_dim()
		complete = []
		for i in range(dim):
			complete.append([])
			for j in range(dim):
				if i == j:
					complete[i].append(0)
					continue
				complete[i].append(1)
		return complete
	
	def directed(self):
		"""Determina si el grafo es dirigido o no dirigido
		Retorna 'True' si es dirigido, 'False' si no lo es"""
		if self.__matrix.symmetry():
			return False
		return True
	
	def connected(self):
		"""Determina, utilizando Busqueda en Profundidad, si el grafo es conexo o no
		Retorna 'True' si es conexo, 'False' si no lo es"""
	#	conexo (no dirigido)
	#	fuertemente conexo (dirigido)
	#	debilmente conexo (dirigido)
	#	no conexo (todos los casos)
		matrix = self.__matrix.get_matrix()
		if self.directed():
			if self.__connected_matrix(matrix):
				print 'strongly connected'
				return True
			matrix = self.__matrix.get_simmetric()
			if self.__connected_matrix(matrix):
				print 'weakly connected'
				return True
		if self.__connected_matrix(matrix):
			print 'connected'
			return True
		print 'not connected'
		return False
	
	def weighted(self):
		"""Determina si el grafo es ponderado o no
		Retorna 'True' si es ponderado, 'False' si no lo es"""
		matrix = self.get_matrix()
		dim = self.__matrix.get_dim()
		for i in range(dim):
			for j in range(dim):
				if matrix[i][j] != 0 and matrix[i][j] != 1:
					return True
		return False
	
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
		matrix = self.get_matrix()
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
		Retorna el grado del nodo. Si 'node' no es valido, retorna 'None'"""
		matrix = self.get_matrix()
		return self.__generic_degree(node, matrix)
	
	#
	#  PUBLIC METHODS - GRAPH ALGORITHMS
	#
	
	def dijkstra(self, origin):
		"""Para un nodo 'origin':
		Determina el camino mas corto desde 'origin' a cualquier nodo
		Retorna 'None' si el nodo es invalido
		Retorna la lista del metodo '__breadthfirst_search' en otro caso"""
		if not self.__validate_target(origin):
			return None
		if not self.weighted():
			return None
		dim = self.__matrix.get_dim()
		matrix = self.get_matrix()
		roads = self.__breadthfirst_search(matrix, origin)
		paths = []
		for i in range(dim):
			temp = self.__get_path(roads, i)
			paths.append(temp)
		return paths
	
	def kruskal(self):
		"""Determina un arbol recubridor minimo
		Retorna la matriz del arbol"""
		if self.directed():
			return None
		if not self.weighted():
			return None
		matrix = self.get_matrix()
		return self.__kruskal_algorithm(matrix)
	
	def hamiltonian_paths(self):
		"""Determina un camino que recorre todos los nodos
		Retorna el camino"""
		dim = self.__matrix.get_dim()
		if not self.connected():
			return None
		temp = []
		path = []
		for i in range(dim):
			self.__hamilton_algorithm(i, temp, path)
		self.__filter(path)
		if len(path) == 0:
			return None
		return path

	def eulerian_paths(self):
		"""Determina un camino/ciclo euleriano, en caso de que exista
		Retorna 'None' si no existe. Retorna el resultado de __fleury en otro caso"""
		dim = self.__matrix.get_dim()
		if not self.connected():
			return None
		
		oddCounter = []
		for i in range(dim):
			if self.degree(i)%2 == 1:
				oddCounter.append(i)
		
		if len(oddCounter) != 0 and len(oddCounter) != 2 and self.__matrix.symmetry==False:
			return None
		if len(oddCounter) == 2:
			if self.degree(oddCounter[0]) > self.degree(oddCounter[1]):
				start = oddCounter[0]
			else:
				start = oddCounter[1]
		if len(oddCounter) == 0:
			start = 0
		array = []
		path = []
		matrix = copy(self.get_matrix())
		if self.__matrix.symmetry() == True:
			self.__fleury(matrix, start, array, path, self.__edges()/2, False)
		else:
			for i in range(dim):
				self.__fleury(matrix, i, array, path, self.__edges(), True)
				if len(array)>0:
					return array
		if len(array) == 0:
			return None
		return array
g = Graph(5)
g.add_edge_dir(0,3,5)
g.add_edge_dir(3,1,6)
g.add_edge_dir(3,4,1)
g.add_edge_dir(1,2,2)
g.add_edge_dir(2,3,5)
g.add_edge_dir(4,0,1)
