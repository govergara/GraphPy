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


import Squishy
import Palettes
import Controller



class Ui:

	def __init__(self):
		self.__loader = Gtk.Builder()
		self.__loader.add_from_file("view/view_model/ventanas.glade")
		self.__menu = MenuWindow(self.get_object("vetanaMenu"))
		self.__tools = MenuTools(self.get_object("ventanaHerramientas"))
		self.__draw = Squishy.Squishy()
		self.__controller = Controller.Controller()
		self.__connect_signals()

	def __connect_signals(self):
		self.__loader.connect(self.__controller)

	def throw_Ui(self):
		gtk.main()
		self.__draw.throw_squishy()