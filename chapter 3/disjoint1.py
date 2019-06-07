def disjoint_1(A,B,C):
	"Return true if there is no element commmon to all the three list"
	for a in A:
		for b in B:
			for c in C:
				if a==b==c:
					return False
	return True 

print(disjoint_1([1,2,3],[4,5,6],[7,8,9]))