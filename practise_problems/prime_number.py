import math
num = 37


isPrime = True

for i in range(2,int(math.sqrt(num))+1):
	if num % i == 0:
		isPrime = False
		break

if isPrime:
	print("Prime")
else:
	print("Not Prime")