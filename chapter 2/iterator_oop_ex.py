class SequenceIterator(object):
	"""An iterator for any of python's sequence datatype"""
	def __init__(self, sequence):
		self._seq = sequence
		self._k = -1

	def __next__(self):
		""" Returns the next element or raise the StopIteration error"""
		self._k +=1
		if self._k < len(self._seq):
			return (self._seq[self._k])
		else:
			raise StopIteration()

	def __iter__(self):
		""" By Convention, an iterator must return itself as an iterator"""
		return self
	
		