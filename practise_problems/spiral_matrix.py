def spiralOrder(A):

	top = 0
	bottom = len(A) -1

	left = 0
	right = len(A[0])-1

	while left <= right and top <= bottom :

		for i in range(left ,right+1):
		    print(A[left][i])

		top = top +1

		for j in range(top,bottom+1):
			print(A[j][right])

		right = right -1

		for k in range(right,left-1,-1):
			print(A[bottom][k])
		bottom = bottom -1

		for l in range(bottom,top-1,-1):
			print(A[l][left])
		left = left + 1


#A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

A = [[1,2,3],[4,5,6],[7,8,9]]

"""A =[
  [1, 2],
  [3, 4],
  [5, 6]
]"""

spiralOrder(A)
