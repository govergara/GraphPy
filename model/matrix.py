class Matrix:

	def __int__(self, dim):
		self.__dimMatrix = dim
		self.__matrix = self.__set_matrix(dim)
		self.__identity = self.__set_identity(dim)

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

	def __set_identity(self, dim):
		"""Para una dimension "dim":
		Crea una nueva matriz. Todos sus elementos tienen el valor '0'
		Los elementos de la diagonal principal toman el valor '1'
		Retorna la nueva matriz"""
		identity = self.__set_matrix(dim)
		for i in range(dim):
			identity[i][i] = 1
		return identity

	#
	#  PUBLIC METHODS
	#

	#  NOT IMPLEMENTED YET
	#	ADDITION (necessary?)
	#	MULTIPLICATION (necessary?)
	#	SYMMETRY (directed / no directed)

	def get_dim(self):
		return self.__dimMatrix

	def add_node(self):
		"""Agrega los datos de un nodo (nueva fila y columna)
		Retorna la nueva dimension de la matriz"""
		new = []
		dim = self.__dimMatrix
		for i in range(dim):
			new.append(0)
		self.__matrix.append(new)
		dim += 1
		for i in range(dim):
			self.__matrix[i].append(0)
		return dim

	def set_element(row, col, value):
		"""Inserta un valor en el elemento (row, col) de la matriz"""
		self.__matrix[row][col] = value

	def del_node(self, target):
		"""Para un indice "target":
		Elimina los datos de un nodo (fila & columna respectiva)
		Retorna la nueva dimension de la matriz"""
		dim = self.__dimMatrix
		self.__matrix.pop(target)
		for i in self.__matrix:
			self.__matrix[i].pop(target)
			dim -= 1
		return dim
