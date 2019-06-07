def disjoint_2(A,B,C):
	"Return true if there is no element commmon to all the three list"
	for a in A:
		for b in B:
			if a == b:
				for c in C:
					if a==c:
						return False

	return True

print(disjoint_2([1,2,3],[4,5,6],[7,8,9]))