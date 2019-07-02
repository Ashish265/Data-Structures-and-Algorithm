"""
     *
    ***
   *****
    ***
     *
"""

rows = 5
no_spaces = rows -1
no_stars = 1

for row in range(1,rows+1):
	s=""
	for sp in range(no_spaces):
		s += " "
	

	for st in range(no_stars):
		s += "*"
	
	print(s)

	if row <= rows//2:
		no_spaces -= 1
		no_stars += 2
	else:
		no_spaces += 1
		no_stars -= 2



