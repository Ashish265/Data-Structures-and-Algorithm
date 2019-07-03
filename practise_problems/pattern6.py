"""
*** ***
**   **
*     *
**   **
*** ***
"""

rows = 5
numStars = rows//2
numSpaces = 1

for row in range(1,rows+1):
	s=""
	for st in range(numStars+1):
		s += "*"
	

	for sp in range(numSpaces):
		s += " "

	for st in range(numStars+1):
		s += "*"
	
	print(s)

	if row <= rows//2:
		numStars -= 1
		numSpaces += 2
	else:
		numStars += 1
		numSpaces -= 2