def even_odd(A):
	"Given a array of number returns even number on one of side of array and odd on other side"

	next_even,next_odd = 0,len(A)-1

	while next_even < next_odd:

		if A[next_even] % 2 == 0:
			next_even += 1
		else:
			A[next_even],A[next_odd] = A[next_odd],A[next_even]
			next_odd -=1

	return A

print(even_odd([1,2,3,4,5,6,7,8,9]))