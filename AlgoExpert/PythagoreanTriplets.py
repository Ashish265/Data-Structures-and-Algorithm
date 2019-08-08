def pythagoreanTriplets(num):

	c = 0
	m = 2

	while c < num:
		 for n in range(1,m):
		 	a = m*m - n*n
		 	b = 2*m*n
		 	c = m*m + n*n

		 	if c > num:
		 		break

		 	if(a==0 or b==0 or c==0):
		 		break

		 	print(a,b,c)

		 m += 1


pythagoreanTriplets(40)