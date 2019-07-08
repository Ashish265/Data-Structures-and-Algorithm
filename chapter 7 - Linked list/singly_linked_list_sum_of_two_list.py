from linked_list import LinkedList
def sum_two_list(self,llist):
	p = self.head
	q = self.head

	sum_list = LinkedList()

	carry = 0

	while p or q:
		if not p:
			i=0
		else:
			i=p.data

		if not q:
			j=0
		else:
			j = q.data

		s = i+j+carry

		if s >=10:
			carry = 1
			remainder = s%10
			sum_list.append(remainder)
		else:
			carry = 0
			sum_list.append(s)


		if p:
			p = p.next
		if q:
			q = q.next

		sum_list.print_llist()


llist1 = LinkedList()
llist2 = LinkedList()

llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2.append(8)
llist2.append(4)
llist2.append(2)

llist1.sum_two_list(llist2)

