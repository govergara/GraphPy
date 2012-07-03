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
		"""Inserta un valor en el elemento (row, col) de la matriz"""
		self.__matrix[row][col] = value
