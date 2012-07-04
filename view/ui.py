try:
	from gi.repository import Gtk
except:
	print "DEPENCENCIAS INSATIFECHAS:  >= GTK3 "
	print "CORRIENDO CON GTK 2.X ... PUEDEN HABER PROBLEMAS"
	try:
		import gtk
	except:
		print "GTK NO DISPONIBLE EN TU SISTEMA"
		exit(1)

from Tkinter import *
import squishy
import palette
from multiprocessing import Process


class Ui:

	def __init__(self):
		self.__loader = Gtk.Builder()
		self.__loader.add_from_file("view_model/ventanas.glade")
		tmp = self.__loader.get_object("menu");
		self.__menu = palette.MenuWindow(tmp)
		tmp.connect("destroy",Gtk.main_quit)
		self.__tools = palette.MenuTools(self.__loader.get_object("paleta"))
		self.__draw = squishy.Squishy()
		
	def connect_signals(self,controller):
		self.__loader.connect_signals(controller)

	def show_elements(self):
		self.__menu.show()
		self.__tools.show()

	def throw_ui(self):
		self.show_elements()
		b = Process(target=Gtk.main)
		b.start()
		self.__draw.throw_squishy()
