def linearSum(S,n):
	"Returns the sum of the first n number of sequence S"
	if n==0:
		return 0
	else:
		return linearSum(S,n-1)+S[n-1]

print(linearSum([15,4,6,8,2],2))
print(linearSum([15,4,6,8,2],4))