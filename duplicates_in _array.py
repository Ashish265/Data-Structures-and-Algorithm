def duplicatesInArray(A):

	for i in range(0,len(A)):
		if A[abs(A[i])] < 0:
			print("Duplicates present",A[i])
			return
		else:
			A[A[i]] = -A[A[i]]

	print("No duplicates present in the array")

duplicatesInArray([1,2,3,3,5,5,7])
