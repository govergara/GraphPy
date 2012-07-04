class Menu:

	 def __init__(self, element):
	 	self.__object = element

	 def show(self):
	 	self.__object.show()

	 def hide(self):
	 	self.__object.hide()


class MenuTools(Menu):
	def __init__(self, widget):
		Menu.__init__(self,widget)

class MenuWindow(Menu):

	def __init__(self, widget):
		Menu.__init__(self,widget)

