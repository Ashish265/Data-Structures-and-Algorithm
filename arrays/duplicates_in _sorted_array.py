def duplicatesArray(A):

	A.sort()

	for i in range(len(A)-1):

		if A[i] == A[i - 1]:
			print(str(A[i])+ " is a duplicate")

	return

duplicatesArray([2,6,5,9,8,4,6,5,2])
duplicatesArray([2,3,4,5,6])