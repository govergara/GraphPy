import ui
import threading




class Controller:
	def __init__(self):
		self.__view = ui.Ui()
		self.__view.connect_signals(self)
	
	def throw_app(self):
		self.__view.throw_ui()
		
	def on_close(self,widget,data=None):
		self.__view.stop_ui()
<<<<<<< HEAD
	
	def on_cursor(self, widget,data=None): #Accede al Cursor
		self.__view.change_operation(2)
	
	def on_node(self,widget,data=None): #Accede a Crear el Nodo
		self.__view.change_operation(1)
	
	def on_add_edge(self, widget, data=None): #Accede a Crear el Arco
		self.__view.change_operation(3)
	
	def on_select(self, widget, data=None): #Accede a Seleccion
		self.__view.change_operation(4)

	def on_to_pdf(self, widget, data=None):
		self.__view.show_window_export()

	def on_print(self, widget, data=None):
		self.__view.show_print()

	def on_export_clicked(self, widget, data=None):
		self.__view.to_pdf()

	def on_destroyloader(self, widget, data=None):
		self.__view.destroy_export()

	def on_clicked(self, widget, data=None):
		self.option_clicked(data)

	def motion_clicked(self, widget, data=None):
		self.__view.option_moved(data)

	def on_click_released(self, widget, data=None):
		self.option_released(data)

	#FUNCIONES PASADAS DESDE LA VISTA

	def option_clicked(self, data = None):
		if self.__view.get_draw_status() == 1:
			if data.button == 1:
				self.__view.insert_new_node(data)

		if self.__view.get_draw_status() == 2:
			return True

		if self.__view.get_draw_status() == 3:
			self.__view.insert_edge(data)

		if self.__view.get_draw_status() == 4:
=======
		
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
>>>>>>> upstream/master

			if data.button == 1:
				self.__view.select_area(data)
			if data.button == 3:
				self.__view.reset()

		if data.button == 3:
			if self.__view.get_draw_over(data) == 1:
				return True
			if self.__view.get_draw_over(data) == 2:
				print "ARISTA"
				return True
			if self.__view.get_draw_over(data) == 3: 
				self.__view.call_popup();

	def option_released(self, data = None):
		if self.__view.get_draw_status() == 1:
			return True
		if self.__view.get_draw_status() == 2:
			return True
		if self.__draw.get_draw_status() == 3:
			return True
		if self.__draw.get_status() == 4:
			if data.button == 1:
				if self.__view.get_draw_ind() == 0:
					self.__view.select_area_end(data)



a = Controller()
a.throw_app()
		
