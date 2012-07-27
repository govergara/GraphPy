class StackActions:
	def __init__(self):
		self.__count_actions = 0
		self.__actions = []


	def push(self, action):
		if self.__count_actions <= 20:
			self.__actions.append(action)
			self.__count_actions += 1
		else:
			self.__actions.pop(0)
			self.__actions.append(action) 

	def pop(self):
		try:
			self.__count_actions -= 1
			return self.__actions.pop()
		except:
			return None