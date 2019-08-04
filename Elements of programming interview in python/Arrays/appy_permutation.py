def applyPermutation(perm,A):

	for i in range(len(A)):
		while perm[i] != i:
			A[perm[i]],A[i] = A[i],A[perm[i]]
			perm[perm[i]],perm[i] = perm[i],perm[perm[i]]

	return perm,A