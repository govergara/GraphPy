from view import squishy

class Files:
	def __init__(self, state=False,name):
		self.__state = state
		if not state:
			self.__file = open(name,"w")
		else:
			self.__file = open(name,"r")

	def new_open_file(self,name,mode):
		self.__file = open(name,mode)
		self.__state = True


	def open_from_file(self):
		if self.__state:
			tmp = squishy.Graph()
			cnt_nodes = int(self.__file.readline())
			for i in xrange(cnt_nodes):
				id = int(self.__file.readline())
				label = str(self.__file.readline())
				positionx = int(self.__file.readline())
				positiony = int(self.__file.readline())
				position = (positionx,positiony)
				color_r = int(self.__file.readline())
				color_g = int(self.__file.readline())
				color_b = int(self.__file.readline())
				tamanio = int(self.__file.readline())
				forma = int(self.__file.readline())
				tmpNode = new squishy.Node()
				tmpNode.set_id(id)
				tmpNode.set_label(label)
				tmpNode.set_position(position)
				tmpNode.set_color((color_r,color_g,color_b))
				tmpNode.set_tam(tamanio)
				tmpNode.set_form(forma)
				tmp.add_node(tmpNode)
			cnt_edges = int(self.__file.readline())
			for i in xrange(cnt_nodes):
				weight = int(self.__file.readline())
				connectionx = int(self.__file.readline())
				connectiony = int(self.__file.readline())
				color_r = int(self.__file.readline())
				color_g = int(self.__file.readline())
				color_b = int(self.__file.readline())
				tamanio = int(self.__file.readline())
				forma = int(self.__file.readline())
				tmpEdge = squishy.Edge()
				tmpEdge.set_weight(weight,(connectionx,connectiony))
				tmpEdge.set_color((color_r,color_g,color_b))
				tmpEdge.set_form(forma)
				tmpEdge.set_tam(tamanio)
				tmp.add_edge(tmpNode)
			self.__file.close()
			self.__state = False
			return tmp
		else:
			return False

	def save_on_file(self,graph,):
		if self.__state:
			self.__file.write(str(len(graph.get_nodes()))+"\n");
			for i in graph.get_nodes():
				self.__file.write(str(i.get_id)+"\n")
				self.__file.write(i.get_label+"\n")
				pos = i.get_position()
				self.__file.write(str(pos[0])+"\n")
				self.__file.write(str(pos[1])+"\n")
				color = i.get_color()
				self.__file.write(str(color[0])+"\n")
				self.__file.write(str(color[1])+"\n")
				self.__file.write(str(color[2])+"\n")
				self.__file.write(str(i.get_tam())+"\n")
				self.__file.write(str(i.get_form())+"\n")
			self.__file.write(str(len(graph.get_edges())+"\n")
			for i in graph.get_edges():
				self.__file.write(str(i.get_weight())+"\n")
				connection = i.get_connection()
				self.__file.write(str(connection[0])+"\n")
				self.__file.write(str(connection[1])+"\n")
				color = i.get_color()
				self.__file.write(str(color[0])+"\n")
				self.__file.write(str(color[1])+"\n")
				self.__file.write(str(color[2])+"\n")
				self.__file.write(str(i.get_tam())+"\n")
				self.__file.write(str(i.get_form())+"\n")
			self.__file.close()
			self.__state = False




