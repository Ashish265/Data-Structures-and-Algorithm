"""
1     1
12   21
123 321
1234321

"""

for r in range(1,5):
	s = ""
	counter = 1
	for c in range(7):
		if counter > r:
			s += " "
		else:

			s +=str(counter)

		if c < 3:
			counter +=1
		else:
			counter -=1
	print(s)

