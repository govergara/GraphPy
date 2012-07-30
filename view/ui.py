try:
	from gi.repository import Gtk, Gdk
except:
	print "DEPENCENCIAS INSATIFECHAS:  >= GTK3 "
	print "CORRIENDO CON GTK 2.X ... PUEDEN HABER PROBLEMAS"
	try:
		import gtk
	except:
		print "GTK NO DISPONIBLE EN TU SISTEMA"
		exit(1)

import squishy
import palette

class Ui:

	def __init__(self):

		self.__loader = Gtk.Builder()
		self.__loader.add_from_file("view/view_model/ventanas.ui")
		self.__mainWindow = self.__loader.get_object("principal")
		self.__darea = self.__loader.get_object("workstation")
		self.__exportWindow = self.__loader.get_object("export")
		self.__statusBar = self.__loader.get_object("statusbar1")
		self.__menuGrafo = self.__loader.get_object("menu-grafo")
		self.__menuNodo = self.__loader.get_object("menu-nodo")
		self.__menuArista = self.__loader.get_object("menu-arista")
		self.__labelWindow = self.__loader.get_object("get-label")
		self.__menuColor = self.__loader.get_object("color")
		self.__menuCoordenates = self.__loader.get_object("coordenadas")
		self.__menuTamanio = self.__loader.get_object("tamanio")
		self.__menuFormaNodo = self.__loader.get_object("forma-nodo")
		self.__menuFormaArista = self.__loader.get_object("forma-arista")
		self.__menuMatriz = self.__loader.get_object("matriz")
		self.__menuAlert = self.__loader.get_object("algoritmos")
		self.__printWindow = self.__loader.get_object("printdialog")
		self.__pageSetup = self.__loader.get_object("pagesetupdialog")
		self.__draw = squishy.Squishy(self.__darea)
	
	def connect_signals(self,controller):
		self.__loader.connect_signals(controller)

	def show_elements(self):
		self.__mainWindow.show()
	
	def change_operation(self, opId):
		self.__draw.set_status(opId)
		self.__draw.reset()
			
	def throw_ui(self):
		self.show_elements()
		Gtk.main()

	def show_window_export(self):
		self.__exportWindow.show()

	def show_print(self):
		self.__printWindow = Gtk.PrintOperation()
		self.__printWindow.set_n_pages(1)
		self.__printWindow.connect("draw_page", self.__printArea)
		res = self.__printWindow.run(Gtk.PrintOperationAction.PRINT_DIALOG, self.__mainWindow)
		return

	def __printArea(self, operation=None, context=None, page_nr=None):
		contexted = context.get_cairo_context()
		self.__cairo_context = self.__draw.draw_extern(contexted)
		return

	def to_pdf(self):
		self.__direction = self.__exportWindow.get_filename()
		if self.__direction == None:
			self.__exportWindow.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
		else:
			self.__formatExport = self.__loader.get_object("formato").get_active_text()
			print self.__direction + self.__formatExport
			#print self.__direction
			self.__draw.create_file(self.__direction, self.__formatExport)
			self.__exportWindow.hide()
		
	def stop_ui(self):
		Gtk.main_quit()

	def destroy_export(self):
		self.__exportWindow.hide()

	def insert_new_node(self,data):
		self.__draw.insert_new_node(data)

	def insert_edge(self,data):
		self.__draw.insert_edge(data)

	def get_draw_status(self):
		return self.__draw.get_status()

	def call_popup(self,data, valor):
		if valor == 1:
			self.__tmp = self.__draw.get_node(data.x, data.y)
			self.__menuNodo.popup(None, None, None, None, data.button, data.time)
		if valor == 2:
			self.__tmp = self.__draw.get_edge(data)
			self.__menuArista.popup(None, None, None, None, data.button, data.time)
		if valor == 3:
			self.__menuGrafo.popup(None, None, None, None, data.button, data.time)

	def get_draw_over(self,data):
		return self.__draw.get_over(data)

	def get_draw_ind(self):
		return self.__draw.get_ind()

	def get_draw_graph(self):
		return self.__draw.get_graph()

	def set_draw_graph(self,graph):
		self.__draw.set_graph(graph)

	def select_area(self,data):
		self.__draw.select_area(data)

	def select_area_end(self):
		self.__draw.select_area_end()
		return True

	def move_selected(self,data):
		self.__draw.move_selected(data)

	def move_node(self,data):
		self.__draw.move_node(data)

	def reset(self):
		self.__draw.reset()

	def show_label(self):
		self.__labelWindow.show()
		self.__labelText = self.__loader.get_object("label-nodo")

	def set_new_label(self):
		self.__tmp.set_label(self.__labelText.get_text())
		self.__draw.redrawing()
		self.__labelText.set_text("")
		self.__labelWindow.hide()
		self.__tmp = None
		self.__draw.reset()

	def show_color(self):
		self.__menuColor.show()
		self.__selectColor = self.__loader.get_object("colorselection")

	def set_new_color(self):
		tmp = self.__selectColor.get_current_rgba()
		self.__tmp.set_color((tmp.red, tmp.green, tmp.blue))
		self.__draw.redrawing()
		self.__menuColor.hide()
		self.__tmp = None
		self.__draw.reset()

	def del_nodo(self):
		if self.__draw.get_graph_super().del_node(self.__tmp.get_id()) == True:
			self.__draw.redrawing()
			return True

	def del_edge(self):
		if self.__draw.get_graph_super().del_edge(self.__tmp.get_connection()) == True:
			self.__draw.redrawing()
			return True

	def set_malla(self, boolean):
		self.__draw.set_malla(boolean)
		self.__draw.redrawing()

	def show_coordenates(self):
		self.__coord_x = self.__loader.get_object("coord-x")
		self.__coord_x.set_text(str(self.__tmp.get_position()[0]))
		self.__coord_y = self.__loader.get_object("coord-y")
		self.__coord_y.set_text(str(self.__tmp.get_position()[1]))
		self.__menuCoordenates.show()

	def set_coordenates(self):
		print self.__tmp.get_position()
		self.__tmp.set_position((float(self.__coord_x.get_text()), float(self.__coord_y.get_text())))
		self.__draw.redrawing()
		self.__coord_x.set_text("")
		self.__coord_y.set_text("")
		self.__menuCoordenates.hide()
		self.__tmp = None
		self.__draw.reset()
 
 	def show_tamanio(self):
 		self.__tamanio = self.__loader.get_object("get-tam")
 		self.__tamanio.set_text(str(self.__tmp.get_tam()))
 		self.__menuTamanio.show()

 	def set_tamanio(self):
 		self.__tmp.set_tam(float(self.__tamanio.get_text()))
 		self.__draw.redrawing()
 		self.__tamanio.set_text("")
 		self.__menuTamanio.hide()
 		self.__tmp = None
 		self.__draw.reset()

 	def show_forma_nodo(self):
 		self.__forma = self.__loader.get_object("formas")
 		self.__menuFormaNodo.show()

 	def set_forma_nodo(self):
 		if self.__forma.get_active_text() == "Circulo":
 			self.__tmp.set_form(1)
 		if self.__forma.get_active_text() == "Cuadrado":
 			self.__tmp.set_form(2)
 		self.__draw.redrawing()
 		self.__menuFormaNodo.hide()
 		self.__tmp = None
 		self.__draw.reset()

 	def show_forma_arista(self):
 		self.__forma = self.__loader.get_object("formas_arista")
 		self.__menuFormaArista.show()

 	def set_forma_arista(self):
 		if self.__forma.get_active_text() == "Normal":
 			self.__tmp.set_form(1)
 		if self.__forma.get_active_text() == "Segmentada 1":
 			self.__tmp.set_form(2)
 		if self.__forma.get_active_text() == "Segmentada 2":
 			self.__tmp.set_form(3)
 		if self.__forma.get_active_text() == "Punteada":
 			self.__tmp.set_form(4)
 		self.__draw.redrawing()
 		self.__menuFormaArista.hide()
 		self.__tmp = None
 		self.__draw.reset()

 	def copy_selected(self):
 		if self.__draw.status_temp() == True:
 			return self.__draw.get_temp()

 	def paste_selected(self, papelera, op):
 		if op == 1:
 			for i in papelera:
 				self.__draw.paste_node((i.get_position()[0], i.get_position()[1]+25), i.get_label(), i.get_color(), i.get_tam(), i.get_form())

 	def show_matriz(self, datos):
 		self.__matraz = self.__loader.get_object("matraz")
 		self.__menuMatriz.show()

 	def hide_matriz(self):
 		self.__menuMatriz.hide()

 	def show_algoritmo(self, string, option):
 		if option == 1:
 			self.__loader.get_object("titulo_algoritmo").set_text("Grafo Dirigido")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 		if option == 2:
 			self.__loader.get_object("titulo_algoritmo").set_text("Tabla de Grados")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 		if option == 3:
 			self.__loader.get_object("titulo_algoritmo").set_text("Completitud")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 		if option == 4:
 			self.__loader.get_object("titulo_algoritmo").set_text("Bipartito")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 		if option == 5:
 			self.__loader.get_object("titulo_algoritmo").set_text("Conexos")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 		if option == 6:
 			self.__loader.get_object("titulo_algoritmo").set_text("Ciclos Eulerianos")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 		if option == 7:
 			self.__loader.get_object("titulo_algoritmo").set_text("Caminos Hamiltonianos")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 		if option == 8:
 			self.__loader.get_object("titulo_algoritmo").set_text("Dijkstra")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 		if option == 9:
 			self.__loader.get_object("titulo_algoritmo").set_text("Kruskal")
 			self.__loader.get_object("resultado").set_text(string)
 			self.__menuAlert.show()
 
 	def set_data(self):
 		self.__draw.set_data()
