def find(S, val):
	"Return index j such that s[j]==val or -1 if no such element"
	n = len(S)
	j=0

	while j<n:
		if S[j]==val:
			return j
		j +=1

	return -1

print(find([1,2,3,4,5,6],4))