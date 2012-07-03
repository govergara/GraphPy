import copy	# Para hacer copias superficiales (shallow copies)

class Matrix:
	"""Clase que maneja la Matriz de Adyacencia/Incidencia"""
	
	def __init__(self, dim):
		self.__dimMatrix = dim
		self.__matrix = self.__set_matrix(dim)
<<<<<<< HEAD
		self.__stackUndo=[]
		self.__stackRedo[]

=======
	
>>>>>>> 8703c6a828e61b3ea85c3a0a03d32a1f3cafec01
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
<<<<<<< HEAD
	def unDo(self)
		"""unDo agrega la matriz actual en una pila "redo" (rehacer) y luego
		define una nueva matriz actual, que es la última guardada en la pila de deshacer"""
		"""Cada vez que deshagas, lo que deshagas será guardado en una pila de "rehacer" """
		self.__stackRedo.append(self.__matrix)
		self.__matrix=self.__stackUndo.pop()

	def reDo(self)
		"""reDo agrega la matriz actual en una pila "undo" (deshacer) y luego
		define una nueva matriz actual, que es la última guardada en la pila rehacer"""
		"""Cada vez que rehagas, lo que rehagas será guardado en una pila de "deshacer" """
		self.__stackUndo.append(self.__matriz)
		self.__matrix=self.__stackRedo.pop()

	def push_stack(self,matrix):
		"""Empila una matriz en una lista de deshacer"""
		self.__stackUndo.append(matrix)
=======
>>>>>>> 8703c6a828e61b3ea85c3a0a03d32a1f3cafec01
	
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
<<<<<<< HEAD
		Retorna la nueva dimension de la matriz
		y empila la matriz en unDo antes de ser modificada"""
		push_stack(self.__matrix)
		new = []
		dim = self.__dimMatrix
		for i in range(dim):
			new.append(0)
		self.__matrix.append(new)
		dim += 1
		for i in range(dim):
			self.__matrix[i].append(0)
		return dim

	def del_node(self, target):
		"""Para un indice "target":
		Elimina los datos de un nodo (fila & columna respectiva)
		Retorna la nueva dimension de la matriz
		y empila la matriz en unDo antes de ser modificada"""
		push_stack(self.__matrix)
		dim = self.__dimMatrix
		self.__matrix.pop(target)
		for i in self.__matrix:
			self.__matrix[i].pop(target)
		dim -= 1
		return dim

=======
		Retorna la nueva dimension de la matriz"""
		try:
			new = []
			dim = self.__dimMatrix
			for i in range(dim):
				new.append(0)
			self.__matrix.append(new)
			dim += 1
			self._Matrix__dimMatrix += 1
			for i in range(dim):
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
			for i in self.__matrix:
				self.__matrix[i].pop(target)
			self._Matrix__dimMatrix -= 1
		except:
			return False
		return True
	
>>>>>>> 8703c6a828e61b3ea85c3a0a03d32a1f3cafec01
	def symmetry(self):
		"""Determina si la matriz es simetrica o no
		Retorna 'True' si es simetrica, 'False' si no lo es"""
		dim = self.__dimMatrix
		for i in dim:
			for j in dim:
				if j <= i:
					continue
				if self.__matrix[i][j] != self.__matrix[j][i]:
					return False
		return True
	
	def set_entry(row, col, value):
		"""Inserta un valor en el elemento (row, col) de la matriz
		y empila la matriz en unDo antes de ser modificada"""
		push_stack(self.__matrix)
		self.__matrix[row][col] = value
	
	def num_relations(self, entry):
		dim = self.__dimMatrix
		relations = 0
		for i in dim:
			if self.__matrix[node][i] != 0:
				relations += 1
		return relations
