def factorial(n):
	"Return the factorial of n"

	if n==0:
		return 1
	else:
		return n*factorial(n-1)


f=factorial(5)
print(f)