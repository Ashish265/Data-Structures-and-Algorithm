def reverse(S,start,stop):
	"Reverse the elements in implicit slice S[start:stop]"
	if start < stop-1:
		S[start],S[stop-1] = S[stop-1],S[start]
		reverse(S,start+1,stop-1)
	return S


print(reverse([4,3,6,2,8,9,5],0,7))