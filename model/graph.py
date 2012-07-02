class Graph:

	def __init__(self):
		self.__matrix = Matrix(1)
		self.__nodes

	#
	#  PRIVATE METHODS
	#

	#
	#  PUBLIC METHODS
	#
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
			for j in dim:
				if self.__matrix[i][node] ==1:
					c+=1
		return c