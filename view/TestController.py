from ui import *

class Controller:
	def __init__(self):
		self.__view = Ui()
		self.__view.connect_signals(self)
	
	def throw_app(self):
		self.__view.throw_ui()
	
	def on_close(self,widget,data=None):
		self.__view.stop_ui()
	
	def on_change_operation(self, widget,data=None):
		self.__view.change_operation(2)
	
	def on_node(self,widget,data=None):
		self.__view.change_operation(1)
	
	def on_add_edge(self, widget, data=None):
		self.__view.change_operation(3)
	
	def on_to_pdf(self, widget, data=None):
		self.__view.show_window_export()
	
	def on_export_clicked(self, widget, data=None):
		self.__view.to_pdf()
	
	def on_destroyloader(self, widget, data=None):
		self.__view.destroy_export()

a = Controller()
a.throw_app()
