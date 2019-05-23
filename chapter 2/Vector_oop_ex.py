class Vector:

	""" Represent a Vector in multidimensional space"""

	def __init__(self,d):
		""" Create a dimension vector of zeros"""
		self._coords = d

	def __len__(self):
		""" Return the dimension of the vector"""
		return(len(self._coords))

	def __getitem__(self,j):
		""" Return the jth coordinate of the vector """
		return(self._coords[j])

	def __set__(self,j,val):
		""" Set jth coordinate of the vector to the given value """
		self._coords[j]=val

	def __add__(self,other):
		""" Return the sum of two vectors """
		if len(self)!=len(other):
			raise ValueError("Dimension must agree")
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __eq__(self,other):
		""" Return True if vector has same coordinate as others"""
		return (self._coords == other._coords)

	def __ne__(self,other):
		""" Return True if vector differ from others"""
		return not self == other

	def __str__(self):
		""" Produces a string representation of other"""
		return "<" + str(self._coords)[1:-1]+">"
