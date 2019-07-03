"""
   1
  232
 45654
4567654
"""
numOfSpaces = 3
for r in range(1,5):
	s=""
	counter = r
	numColumn = 2*r - 1
	for sp in range(numOfSpaces):
		s += " "
	for c in range(2*r - 1):
		s +=str(counter)

		if c < numColumn//2:
			counter +=1
		else :
			counter -=1
	numOfSpaces -=1

	print(s)

