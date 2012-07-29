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

from multiprocessing import Process
from Tkinter import *
import squishy
import palette

class Ui:

	def __init__(self):

		self.__loader = Gtk.Builder()
<<<<<<< HEAD
		self.__loader.add_from_file("view/view_model/ventanas.ui")
		self.__mainWindow = self.__loader.get_object("principal")
		self.__darea = self.__loader.get_object("workstation")
		self.__exportWindow = self.__loader.get_object("export")
		self.__statusBar = self.__loader.get_object("statusbar1")
		self.__printWindow = self.__loader.get_object("printdial")
		self.__menuGrafo = self.__loader.get_object("menu-grafo")
=======
		self.__loader.add_from_file("view_model/ventanas.ui")
		self.__mainWindow = self.__loader.get_object("principal")
		self.__darea = self.__loader.get_object("workstation")
		self.__exportWindow = self.__loader.get_object("export")
>>>>>>> upstream/master
		self.__draw = squishy.Squishy(self.__darea)

		
	def connect_signals(self,controller):
		self.__loader.connect_signals(controller)

	def show_elements(self):
		self.__mainWindow.show()
	
	def change_operation(self, opId):
		self.__draw.set_status(opId)
<<<<<<< HEAD
		self.__draw.reset()
=======
>>>>>>> upstream/master
			
	def throw_ui(self):
		self.show_elements()
		Gtk.main()

	def show_window_export(self):
		self.__exportWindow.show()

<<<<<<< HEAD
	def show_print(self):
		self.__printWindow.show()

=======
>>>>>>> upstream/master
	def to_pdf(self):
		self.__direction = self.__loader.get_object("export").get_filename()
		self.__formatExport = self.__loader.get_object("formato").get_active_text()
		print self.__direction + self.__formatExport
		#print self.__direction
		self.__draw.create_file(self.__direction, self.__formatExport)
		self.destroy_export()
		
	def stop_ui(self):
		Gtk.main_quit()

	def destroy_export(self):
<<<<<<< HEAD
		self.__exportWindow.hide()

	def insert_new_node(self,data):
		self.__draw.insert_new_node(data)

	def insert_edge(self,data):
		self.__draw.insert_edge(data)

	def get_draw_status(self):
		return self.__draw.get_status()

	def call_popup(self):
		self.__menuGrafo.popup(None, None, None, None, data.button, data.time)

	def get_draw_over(self,data):
		self.__draw.get_over(data)

	def get_draw_ind(self):
		return self.__draw.get_ind()

	def select_area_end(self,data):
		self.__draw.select_area_end(data)

	def get_draw_graph(self):
		return self.__draw.get_graph()

	def set_draw_graph(self,graph):
		self.__draw.set_graph(graph)

	def select_area(self,data):
		self.__draw.select_area(data)

	def select_area_end(self,data):
		self.__draw.select_area_end(data)

	def move_selected(self,data):
		self.__draw.move_selected(data)

	def reset(self):
		self.__draw.reset()

 


=======
		self.__exportWindow.hide()
>>>>>>> upstream/master
