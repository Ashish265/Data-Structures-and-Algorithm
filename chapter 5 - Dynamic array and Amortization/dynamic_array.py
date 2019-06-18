import ctypes

class DynamicArray:

	""" A Dynamic array class akin to a simplified python list"""

	def __init__(self):
		""" Create an empty array """

		self._n = 0                     # count actual elements
		self._capacity = 0              # default array capacity
		self._A = self._make_array(self._capacity)  # low-level array

	def __len__(self):
		""" Returns number of elements stored in an array """
		return self._n

	def __getitem__(self,k):
		""" Return an element at index k"""
		if not 0<= k < self._n:
			raise IndexError("Invalid index")
		return self._A[k]

	def append(self,obj):
		""" Add object to end of the array """
		if self._n == self._capacity:
			self._resize(2*self._capacity)
		self._A[self._n] = obj
		self._n +=1

	def _resize(self,c):
		""" Resize internal array to capacity c """
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A = B
		self._capacity = c

	def _make_array(self,c):
		""" return new array with capacity c """

		return (c*ctypes.py_object)()