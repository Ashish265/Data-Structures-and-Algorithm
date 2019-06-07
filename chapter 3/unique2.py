def unique_2(S):
	"Return True if there are no duplicate elements in sequence S"
	temp = sorted(S)
	for j in range(1,len(temp)):
		if temp[j-1] == temp[j]:
			return False
	return True

print(unique_2([1,2,3,4,5,6,7,8,9,1]))