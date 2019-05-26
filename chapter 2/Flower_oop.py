class Flower:

	def __init__(self,nameOfFlower,numberOfPetal,price):

		self.set_name(nameOfFlower)
		self.set_petals(numberOfPetal)
		self.set_price(price)

	def set_name(self,nameOfFlower):
		self._nameOfFlower = str(nameOfFlower)

	def get_name(self):
		return self._nameOfFlower

	def set_petals(self,numberOfPetal):
		if type(numberOfPetal) == int:
			self._numberOfPetals = numberOfPetal
		else:
			raise ValueError('invalid literal for int() with base 10')

	def get_petals(self):
		return self._numberOfPetals

	def set_price(self,price):
		if type(price) == float:
			self._price = float(price)
		else:
			raise ValueError('Enter floating point number')

	def get_price(self):
		return self._price

f = Flower("abc",10,50.0)
