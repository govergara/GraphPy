try:
	from gi.repository import Gtk
except:
	print "DEPENCENCIAS INSATIFECHAS:  >= GTK3 "
	exit(1)



class Ui:

	def __init__(self):
		self.loader = Gtk.Builder()
		self.loader.add_from_file("view/view_model/ventanas.glade")
		self.__menu = MenuWindow(self.get_object(""))
		self.__tools = None