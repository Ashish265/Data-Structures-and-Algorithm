def unique_1(S):
	"Return True if there are no duplicate elements in sequence S"
	for j in range(len(S)):
		for k in range(j+1,len(S)):
			if S[j]==S[k]:
				return False
	return True

print(unique_1([1,2,3,4,5,6,7,8,9,1]))