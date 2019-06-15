def min_max(S,n,what):
	"Returns the minimum and Maximum of the sequence"
	if n==1:
		return S[0]
	elif what == "mini":
		return min(S[n-1],min_max(S,n-1,"mini"))
	elif what == "maxi":
		return max(S[n-1],min_max(S,n-1,"maxi"))


print(min_max([1,2,3,4],4,"maxi"))

