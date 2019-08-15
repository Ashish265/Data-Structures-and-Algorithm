class Node(object):
	"""docstring fos Node"""
	def __init__(self,data,next=None):
		self.data = data
		self.next = next

class Stack:

	def __init__(self):
		self.head = None

	def push(self,data):

		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def pop(self):

		if self.isEmpty():
			return "Stack is empty"

		temp = self.head
		self.head = self.head.next
		removed = temp.data

		return removed

	def isEmpty(self):

		return True if self.head is None else False

s = Stack()
s.push(5)
s.push(10)
print(s.pop())
print(s.pop())


		