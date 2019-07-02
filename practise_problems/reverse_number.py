num = 3247
result = 0
while num !=0:
	digit = num%10
	num = num//10
	result = result*10 +digit
print(result)

