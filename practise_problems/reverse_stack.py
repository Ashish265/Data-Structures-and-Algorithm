from pprint import pprint
class Stack:

	def __init__(self):

		self.item = []

	def push(self,data):

		self.item.append(data)

	def pop(self):

		if self.isEmpty():
			return "Stack is empty"

		return self.item.pop()

	def peek(self):

		if self.isEmpty():
			return "Stack is empty"

		return self.item[-1]

	def isEmpty(self):
		return self.item == []

	def __repr__(self):
		return "Stack {0}".format(self.stack)


def reverseStack(stack):
	def reverseStackRecursive(stack,newStack= Stack()):
		if not stack.isEmpty():
			newStack.push(stack.pop())
			reverseStackRecursive(stack,newStack)

		return newStack

	return reverseStackRecursive(stack)

stk = Stack()
stk.push(3)
stk.push(2)
stk.push(1)
pprint(vars(stk))
pprint(vars(reverseStack(stk)))

