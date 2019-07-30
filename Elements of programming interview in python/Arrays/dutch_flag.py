def dutcFlag(pivot_index:int,A):
	pivot = A[pivot_index]

	smaller = 0

	for i in range(len(A)):
		if A[i] < pivot:
			A[i],A[smaller] = A[smaller],A[i]
			smaller +=1

	larger = len(A)-1

	for i in reversed(range(len(A))):
		if A[i] > pivot:
			A[i],A[larger] = A[larger],A[i]
			larger -=1

	return A

print(dutcFlag(2,[0,1,2,0,2,1,1]))