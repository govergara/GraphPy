import copy		# Para hacer copias superficiales (shallow copies)
import itertools	# Realizar permutaciones (permutations)
import matrix

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
		while True: # almacena los nodos en orden inverso
			path.append(temp)
			temp = status[temp]['from']
			if temp == -1:
				break
		path.reverse() # revierte el orden de los nodos
		return path
	
	def __fleury_algorithm(self, origin):
		"""Para un nodo 'origin':
		Determina, aplicando el Algoritmo de Fleury, un camino euleriano del grafo
		Retorna el camino euleriano encontrado (lista de nodos)"""
		dim = self.__matrix.get_dim()
		traveledEdges = self.get_matrix()
		path = []
		path.append(origin)
		
		finished = False
		while not finished:
			# crea una copia superficial de 'traveledEdges' en 'matrix'
			matrix = []
			for i in range(dim):
				matrix.append( copy.copy(traveledEdges[i]) )
			# terminada la copia
			
			for i in range(dim):
				if matrix[origin][i] == 0:
					continue
				candidate = i
				matrix[origin][i] = 0
				data = self.__breadthfirst_search(matrix, origin)
				connected = 1
				# connected: 1, es conexo
				# connected: 0, no es conexo
				for j in range(dim):
					if data[j]['set'] == 0:
						connected = 0
						break
				if connected == 1:
					break
			
			if self.directed():
				traveledEdges[origin][candidate] = 0
			else:
				traveledEdges[origin][candidate] = 0
				traveledEdges[candidate][origin] = 0
			
			if origin == candidate:
				# 'origin' sera igual a 'candidate' solo si
				# 'origin' no tiene conexiones. Si eso pasa,
				# no existe camino
				return None
			
			origin = candidate
			finished = True
			
			for i in range(dim):
				for j in range(dim):
					if traveledEdges[i][j] != 0:
						finished = False
			path.append(origin)
		
		return path
	
	def __kruskal_algorithm(self):
		# llamar a funcion utilizada en __hamiltonian_path()
		pass
	
	def __hamilton_algorithm(self, pivot):
		matrix = self.get_matrix()
		dim = self.__matrix.get_dim()
		nodes = []
		for i in range(dim):
			if i == pivot:
				continue
			nodes.append(i)
		permut = []
		for i in itertools.permutations(nodes):
			permut.append(i)
		for i in range( len(permut) ):
			actual = pivot
			next = permut[i][0]
			count = 0
			path = [actual]
			unconnected = 0
			for j in range(dim - 2):
				if matrix[actual][next] == 0:
					unconnected = 1
				actual = permut[i][j]
				next = permut[i][j + 1]
				path.append(actual)
			path.append(next)
			if unconnected == 0:
				return path
		return None
				
					
	
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
		Retorna 'True' si es dirigido, 'False' si no lo es"""
		if self.__matrix.symmetry(): # Comprueba si la matriz es simetrica
			return False # Si es simetrica, entonces el grafo no es dirigido
		return True # Si no es simetrica, entonces el grafo es dirigido
	
	def connected(self):
		"""Determina, utilizando Busqueda en Profundidad, si el grafo es conexo o no
		Retorna 'True' si es conexo, 'False' si no lo es"""
		matrix = self.get_matrix()
		return self.__connected_matrix(matrix)
	
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
		if self.__validate_target(node):
			return self.__matrix.num_relations(node)
		return None
	
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
		dim = self.__matrix.get_dim()
		matrix = self.get_matrix()
		roads = self.__breadthfirst_search(matrix, origin)
		paths = []
		for i in range(dim):
			temp = self.__get_path(roads, i)
			paths.append(temp)
		return paths
	
	def kruskal(self):
		pass
	
	def hamiltonian_path(self):
		dim = self.__matrix.get_dim()
		if not self.connected():
			return None
		
		minDegree = self.degree(0)
		node = 0
		for i in range(dim):
			if self.degree(i) < minDegree:
				minDegree = self.degree(i)
				node = i
		return self.__hamilton_algorithm(node)
	
	def eulerian_path(self):
		"""Determina un camino/ciclo euleriano, en caso de que exista
		Retorna 'None' si no existe. Retorna el resultado de __fleury_algorithm en otro caso"""
		dim = self.__matrix.get_dim()
		if not self.connected():
			return None
		
		oddCounter = []
		for i in range(dim):
			if self.degree(i)%2 == 1:
				oddCounter.append(i)
		
		if len(oddCounter) != 0 and len(oddCounter) != 2:
			return None
		if len(oddCounter) == 2:
			if self.degree(oddCounter[0]) > self.degree(oddCounter[1]):
				start = oddCounter[0]
			else:
				start = oddCounter[1]
		if len(oddCounter) == 0:
			start = 0
		
		return self.__fleury_algorithm(start)

# Instrucciones para probar el algoritmo

g = Graph(4)
g.change_relation(0,1,3)
g.change_relation(0,2,4)
g.change_relation(1,0,3)
g.change_relation(1,2,2)
g.change_relation(2,0,4)
g.change_relation(2,1,2)
g.change_relation(2,3,1)
g.change_relation(3,2,1)
