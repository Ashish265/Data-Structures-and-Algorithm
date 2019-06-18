class ArrayStack:
	""" LIFO stack implemented using a python List as underlying storage"""

	def __init__(self):
		""" Ceate an empty stack """
		self._data = []

	def __len__(self):
		""" Return the number of element in the stack """
		return len(self._data)

	def is_empty(self):
		""" Return True if stack is empty """
		return len(self._data)==0

	def push(self,e):
		""" Add element e to the top of the stack """
		self._data.append(e)

	def top(self):
		"""Returns but donot remove the elememt at the top of the stack 
		Raise empty exceptio if stack is empty
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data[-1]

	def pop(self):
		"""Remove and returns the elememt at the top of the stack 
		Raise empty exceptio if stack is empty
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data.pop()



s = ArrayStack()
s.push(5)
s.push(6)
s.pop()
print(s.top())
