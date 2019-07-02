"""
*
**
***
****
*****
"""
"""" Python specific"""
for i in range(1,6):
	print("*"*i)

"""" Python specific above version 3 """

for i in range(1,6):
	
	for j in range(i):
		print("*",end="")
	print()

""" Another method used in other languages """
for i in range(1,6):
	s= ""
	for j in range(i):
		s=s+"*"
	print(s)
