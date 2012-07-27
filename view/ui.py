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
from squishy import Squishy

class Ui:
	
	def __init__(self):

		self.__loader = Gtk.Builder()
		self.__loader.add_from_file("view_model/ventanas.ui")
		self.__mainWindow = self.__loader.get_object("principal")
		self.__darea = self.__loader.get_object("workstation")
		self.__exportWindow = self.__loader.get_object("export")
		self.__draw = Squishy(self.__darea)
	
	def connect_signals(self,controller):
		self.__loader.connect_signals(controller)
	
	def show_elements(self):
		self.__mainWindow.show()
	
	def change_operation(self, opId):
		self.__draw.set_status(opId)
	
	def throw_ui(self):
		self.show_elements()
		Gtk.main()
	
	def show_window_export(self):
		self.__exportWindow.show()
	
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
		self.__exportWindow.hide()
