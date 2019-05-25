class Range:
	""" A class that mimic the built in range class"""

	def __init__(self,start,stop=None,step=1):
		""" Initialize a range instance.

		semantics is similar to built in range class """

		if step == 0:
			raise ValueError("step cannot be zero")

		if step is None:
			start,stop = 0,start

		# calculate effictive length once
		self._length = max(0,(stop-start+step-1)//step)

		# need knowledge of start and step to support __getitem__
		self._start = start
		self._step = step

	def __len__(self):
		""" Returns the number of entries in the range"""
		return self._length

	def __getitem__(self,k):
		""" return entry at index k (using standard interpretation if negative)"""

		if k < 0:
			k += len(self)

		if not 0 <= k < self._length:
			raise IndexError("index out of range")

		return self._start + k * self._step

