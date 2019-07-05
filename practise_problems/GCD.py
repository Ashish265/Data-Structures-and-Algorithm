# Naive metod
def gcd(m,n):
	"Returns the gcd of m,n"

	factorsOfM = []
	for i in range(1,m+1):
		if m%i == 0:
			factorsOfM.append(i)

	factorOfN = []
	for j in range(1,n+1):
		if n%j==0:
			factorOfN.append(j)

	common_factors = []

	for k in factorsOfM:
		if k in factorOfN:
			common_factors.append(k)

	return(common_factors[-1])

# Better way to solve GCD

def gcd_improved(m,n):
	"Returns the GCD of m,n"
	common_factors = []

	for i in range(1,min(m,n)+1):
		if m%i ==0 and n%i==0:
			common_factors.append(i)
	return common_factors[-1]

# Much better implementation without list

def gcd_improved1(m,n):
	"Returns the GCD of m,n"


	for i in range(1,min(m,n)+1):
		if m%i ==0 and n%i==0:
			mrcf = i
	return mrcf

# Much better implementation without list and using while loop

def gcd_improved2(m,n):
	"Returns the GCD of m,n"

	i= min(m,n)+1

	while(i>0):
		if m%i ==0 and n%i==0:
			return i
		else:
			i = i-1



print(gcd(7,9))
print(gcd_improved(3,9))
print(gcd_improved1(3,9))
print(gcd_improved2(7,9))
