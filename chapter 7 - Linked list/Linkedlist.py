class LinkedStack:
	""" LIFO stack implementation using a singly linked list for storage"""
	#----------------------------Nested class Node ---------------------------------------

	class _Node:
		""" Lightweight, nonpublic class for storing a singly linked node """

		__slots__ = '_element',"_next"     #streamline memory usage


		def __init__(self,element,next):
			self._element = element
			self._next = next

	#------------------------------Stack methods-----------------------------------------------

	def __init__(self):
		""" Create an empty stack"""
		self._head = None
		self._size = 0

	def __len__(self):
		"""Returns the number of elements in the stack"""
		return self._size

	def is_empty(self):
		""" Returns True if stack is empty """
		return self._size==0

	def push(self,e):
		""" Add element e to the top of the stack"""
		self._head = self._Node(e,self._head)
		self._size += 1

	def top(self):
		""" Return (but donot remove) the element at the top of the stack

		Raise empty exception if the stack is empty

		"""

		if self.is_empty():
			raise Empty("Stack is empty")
		return self._head._element


	def pop(self):
		""" Return and remove the element at the top of the stack

		Raise empty exception if the stack is empty

		"""

		if self.is_empty():
			raise Empty("Stack is empty")
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		return answer








