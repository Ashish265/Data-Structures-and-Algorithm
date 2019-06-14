def power(x,n):
	"Computes the value x**n for integer n"
	if n==0:
		return 1

	else:
		return x*power(x,n-1)

print(power(5,2))
print(power(5,3))