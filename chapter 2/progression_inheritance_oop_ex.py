class Progression:
	""" Iterator producing an generic progression 

	default iterator produces the progression 1 2 3 ..
	"""

	def __init__(self,start=0):
		""" Initialize current to the first value of progression """
		self._current = start

	def _advance(self):
		""" Update self.current to new value

		This should be overriden by subclass to customize progression

		By convention if current is set to none, this designates the end of a finite progression"""

		self._current +=1

	def __next__(self):
		""" Return the next element or else raise StopIteraton error"""
		if self._current is None:
			raise StopIteraton()

		else:
			answer = self._current
			self._advance()
			return answer

	def __iter__(self):
		""" By convention interator must return itself as an iterator """

		return self

	def print_progression(self,n):
		""" Print next n values of the progression"""

		print(' '.join(str(next(self))for j in range(n)))


class ArithmeticProgression(Progression):
	""" Iterator producing an arithmetic progression"""

	def __init__(self,increment=1,start=0):
		""" Creates a new arithmetic progression 

		increment  the fixed constatnt to add to each term
		start      the first term of the progression
		"""

		super().__init__(start)
		self._increment = increment

	def _advance(self):
		""" Update current value by fixed increment"""
		self._current += self._increment

class GeometricProgression(Progression):
	""" Iterator producing an Geometric progression"""

	def __init__(self,base=2,start=1):
		""" Creates a new Geometric progression 

		base  the fixed constatnt multiplied to each term 
		"""

		super().__init__(start)
		self._base = base

	def _advance(self):
		""" Update current value by fixed increment"""
		self._current *= self._base

class FibonacciProgression(Progression):
	""" Iterator producing an Fibonacci progression"""

	def __init__(self,first=0,second=1):
		""" Creates a new Fibonacci progression 

		base  the fixed constatnt multiplied to each term 
		"""

		super().__init__(first)
		self._prev = second - first

	def _advance(self):
		""" Update current value by fixed increment"""
		self._prev,self._current = self._current, self._prev + self._current


		

