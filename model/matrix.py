from copy import copy	# Para hacer copias superficiales (shallow copies)

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
		dim = copy(self.__dimMatrix)
		return dim
	
	def get_matrix(self):
		"""Retorna una copia 'superficial' (por valor) de la matriz"""
		dim = self.get_dim()
		matrix = []
		for i in range(dim):
			temp = copy(self.__matrix[i])
			matrix.append(temp)
		return matrix
	
	def add_entry(self):
		"""Agrega los datos de un nodo (fila & columna respectiva)
		Retorna 'True' si se ejecuta correctamente, 'False' en otro caso"""
		try:
			dim = self.get_dim()
			new = []
			for i in range(dim):
				new.append(0)
			self.__matrix.append(new)
			self.__dimMatrix += 1
			dim = self.get_dim()
			for i in range(dim):
				self.__matrix[i].append(0)
			return True
		except:
			return False
	
	def del_entry(self, target):
		"""Para un indice "target":
		Elimina los datos de un nodo (fila & columna respectiva)
		Retorna 'True' si se ejecuta correctamente, 'False' en otro caso"""
		try:
			self.__matrix.pop(target)
			self.__dimMatrix -= 1
			dim = self.get_dim()
			for i in range(dim):
				self.__matrix[i].pop(target)
			return True
		except:
			return False
	
	def set_entry(self, row, col, value):
		"""Inserta un valor en el elemento (row, col) de la matriz"""
		self.__matrix[row][col] = value
	
	def symmetry(self):
		"""Determina si la matriz es simetrica o no
		Retorna 'True' si es simetrica, 'False' si no lo es"""
		dim = self.get_dim()
		for i in range(dim):
			for j in range(dim):
				if j <= i:
					continue
				if self.__matrix[i][j] != self.__matrix[j][i]:
					return False
		return True
	
	def get_simmetric(self):
		"""Si la matriz es simetrica, retorna una copia de la matriz
		Si no, retorna una matriz simetrica construida a partir de la original"""
		matrix = self.get_matrix()
		if self.symmetry():
			return matrix
		
		dim = self.get_dim()
		for i in range(dim):
			for j in range(dim):
				if j <= i:
					continue
				if matrix[i][j] != 0:
					matrix [j][i] = matrix[i][j]
		return matrix
