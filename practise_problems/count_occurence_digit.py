def countOccurence(number,digit):
	"Returns the occurence of a digit in a number"
	counter = 0
	while number > 0:
		rem = number % 10
		if digit == rem:
			counter +=1
		number = number//10
	return counter


print(countOccurence(31412,1))
print(countOccurence(31112,1))