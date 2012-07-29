import StackActions
from view import ui
import copy
#import model

class Controller:
	def __init__(self):
		self.__view = ui.Ui()
		self.__view.connect_signals(self)
		self.__undo_stack = StackActions.StackActions()
		self.__redo_stack = StackActions.StackActions()
		self.__papelera = []
		self.__copy_o_paste = 1
		self.__tmp = 0
	
	def throw_app(self):
		self.__view.throw_ui()
		self.__redo_stack.push(self.__view.get_draw_graph())
		
	def on_close(self,widget,data=None):
		self.__view.stop_ui()
	
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
		self.option_moved(data)

	def on_click_released(self, widget, data=None):
		self.option_released(data)

	def on_redo(self,widget,data=None):
		tmp = self.__redo_stack.pop()
		print "deshaciendo en redo con grafo igual a ",tmp
		if tmp is not None:
			self.__undo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
			self.__view.set_draw_graph(copy.deepcopy(tmp))

	def on_undo(self, widget, data=None):
		tmp = self.__undo_stack.pop()
		if tmp is not None:
			self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
			self.__view.set_draw_graph(copy.deepcopy(tmp))

	#FUNCIONES PASADAS DESDE LA VISTA

	def option_clicked(self, data = None):
		if self.__view.get_draw_status() == 1:
			if data.button == 1:
				self.__redo_stack.push(self.__view.get_draw_graph())
				self.__view.insert_new_node(data)

		if self.__view.get_draw_status() == 2:
			self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))

		if self.__view.get_draw_status() == 3:
			if data.button == 1:
				if self.__tmp == 0:
					self.__view.insert_edge(data)
					self.__tmp += 1
				else:	
					self.__redo_stack.push(self.__view.get_draw_graph())
					self.__view.insert_edge(data)
					self.__tmp = 0
			

		if self.__view.get_draw_status() == 4:
			if data.button == 1:
				self.__view.select_area(data)
			if data.button == 3:
				self.__view.reset()

		if data.button == 3:
			if self.__view.get_draw_over(data) == 1:
				self.__view.call_popup(data, 1)
			if self.__view.get_draw_over(data) == 2:
				self.__view.call_popup(data, 2)
			if self.__view.get_draw_over(data) == 3: 
				self.__view.call_popup(data, 3)


	def option_moved(self, data = None):
		if self.__view.get_draw_status() == 1:
			return True
		if self.__view.get_draw_status() == 2:
			self.__view.move_node(data)
		if self.__view.get_draw_status() == 3:
			return True
		if self.__view.get_draw_status() == 4:
			self.__view.move_selected(data)

	def option_released(self, data = None):
		if self.__view.get_draw_status() == 1:
			return True
		if self.__view.get_draw_status() == 2:
			return True
		if self.__view.get_draw_status() == 3:
			return True
		if self.__view.get_draw_status() == 4:
			if data.button == 1:
				if self.__view.get_draw_ind() == 0:
					self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
					self.__view.select_area_end(data)

	def show_label(self, widget, data = None):
		self.__view.show_label()

	def set_label(self, widget, data = None):
		self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
		self.__view.set_new_label()

	def show_color(self, widget, data = None):
		self.__view.show_color()

	def set_color(self, widget, data = None):
		self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
		self.__view.set_new_color()

	def del_nodo(self, widget, data = None):
		self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
		self.__view.del_nodo()

	def del_edge(self, widget, data = None):
		self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
		self.__view.del_edge()

	def show_malla(self, widget, data=None):
		self.__view.set_malla(widget.get_active())

	def show_coordenates(self, widget, data=None):
		self.__view.show_coordenates()

	def set_coordenates(self, widget, data=None):
		self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
		self.__view.set_coordenates()

	def show_tamanio(self, widget, data=None):
		self.__view.show_tamanio()

	def set_tamanio(self, widget, data=None):
		self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
		self.__view.set_tamanio()

	def show_forma_nodo(self, widget, data=None):
		self.__view.show_forma_nodo()

	def set_forma_nodo(self, widget, data=None):
		self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
		self.__view.set_forma_nodo()

	def show_forma_arista(self, widget, data=None):
		self.__view.show_forma_arista()

	def set_forma_arista(self, widget, data=None):
		self.__redo_stack.push(copy.deepcopy(self.__view.get_draw_graph()))
		self.__view.set_forma_arista()

	def copy_selected(self, widget, data=None):
		self.__papelera = self.__view.copy_selected()
		self.__copy_o_paste = 1

	def paste_selected(self, widget, data=None):
		self.__view.paste_selected(self.__papelera, self.__copy_o_paste)
		if self.__copy_o_paste == 2:
			del self.__papelera[:]





a = Controller()
a.throw_app()