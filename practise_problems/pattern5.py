"""
1
22
303
4004
50005
"""

for r in range(1,6):
	s= ""
	for c in range(r):
		if c ==0 or c==(r-1):
			s += str(r)
		else:
			s += str(0)

	print(s)