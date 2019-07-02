"""
     *
    ***
   *****
  *******
 *********
***********
"""

rows = 5
no_spaces = rows -1
no_stars = 1

for row in range(1,rows+1):
	s=""
	for sp in range(no_spaces):
		s += " "
	no_spaces -= 1

	for st in range(no_stars):
		s += "*"
	no_stars += 2

	print(s)




