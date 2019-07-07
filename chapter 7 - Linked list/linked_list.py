class Node:
	"Creates a node for a linked list"

	def __init__(self,data):

		self.data = data
		self.next = None

class LinkedList:
	"Create a linked list using the class node"

	def __init__(self):
		self.head = None

	def print_list(self):
		"Print the elements of the linked list"
		curr_node = self.head

		while curr_node:

			print(curr_node.data)
			curr_node = curr_node.next

	def append(self,data):
		"add element to the linked list"

		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node = self.head

		while last_node.next:
			last_node = last_node.next

		last_node.next = new_node 

	def prepend(self,data):
		"add node to the head"

		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self,prev_node,data):
		"Insert element after a node in linked list"

		if not prev_node:
			print("Previous node is not in the linked list")

			return

		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def len_iterative(self):
		"returns the length of the linked list"

		count=0
		curr_node = self.head

		while curr_node:

			count += 1
			curr_node = curr_node.next

		return count

	def delete_node(self,key):
		"Delete element from the linked list which is equla to key"

		curr_node = self.head

		if curr_node and curr_node.data == key:
			self.head = curr_node.next
			curr_node = None

		prev = None

		while curr_node and curr_node != key:
			prev = curr_node

			curr_node = curr_node.next

		if curr_node is None:
			return
		prev.next  = curr_node.next
		curr_node = None
			

	def delete_node_at_pos(self,pos):
		"Delete node at a position pos"

		curr_node = self.head

		if pos == 0:
			self.head = curr_node.next
			curr_node = None

		prev = None
		count = 1

		while curr_node and count != pos:
			prev = curr_node
			curr_node = curr_node.next
			count +=1

		if curr_node is None:
			return

		prev = curr_node.next
		curr_node = None



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#llist.print_list()

llist.prepend("E")
#llist.insert_after_node(llist.head.next,"F")
#llist.insert_after_node(llist.head.next.next,"Z")
llist.delete_node_at_pos(0)
llist.delete_node("B")
llist.print_list()
print(llist.len_iterative())

