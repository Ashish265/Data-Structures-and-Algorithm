"""
1
23
456
78910
"""
counter = 1
for row in range(1,5):
	s=""
	for col in range(row):
		s=s + str(counter)
		counter +=1
	print(s)