import ui
import threading
import Tkinter




class Controller:
	def __init__(self):
		self.__view = ui.Ui()
		self.__view.connect_signals(self)
	
	def throw_app(self):
		self.__view.throw_ui()

	def onClickNew(self, widget,data = None):
		pass






a = Controller()
a.throw_app()
		