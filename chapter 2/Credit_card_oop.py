class CreditCard:
	""" A consumer credit card """

	def __init__(self,customer,bank,acnt,limit):
		""" Create a new credit card instance.

		customer  the name of the customer 
		bank      the name of the bank
		acnt      the account identifier
		limit     credit limit
		"""
		self._customer = customer
		self._bank = bank
		self._acnt = acnt
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		""" Return name of the customer """
		return self._customer

	def get_bank(self):
		""" Returns the bank's name """
		return self._bank

	def get_account(self):
		""" Return the account number """
		return self._acnt

	def get_limit(self):
		""" Return the current credit limit """
		return self._limit

	def get_balance(self):
		""" Return current balance """
		return self._balance

	def charge(self,price):
		""" Charge given to the card, assuming sufficient credit limit

		Return True if the charge was processed : False if the charge was denied.
		"""
		if price + self._balance > self._limit:
			return False
		else:
			self._balance += price
			return True

	def make_payement(self,amount):
		""" Process customer payament that reduces balances"""
		self._balance -= amount


if __name__ =='__main__':
	wallet = []

	wallet.append(CreditCard('John Bowman','California Savings','5391 0375 9387 5309',2500))
	wallet.append(CreditCard('John Bowman','California Federal','3485 0399 3395 1954',3500))
	wallet.append(CreditCard('John Bowman','California Finance','5391 0375 9387 5309',5000))


	for val in range(1,17):
		wallet[0].charge(val)
		wallet[1].charge(2*val)
		wallet[2].charge(3*val)

	for c in range(3):
		print('customer =',wallet[c].get_customer())
		print('Bank =',wallet[c].get_bank())
		print('Account =',wallet[c].get_account())
		print('Limit =',wallet[c].get_limit())
		print('Balance =',wallet[c].get_balance())

		while wallet[c].get_balance() > 100:
			wallet[c].make_payement(100)
			print('New balance =',wallet[c].get_balance())
		print()

