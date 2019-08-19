def kadanesAlgorithm(array):
	maxEndingHere = array[0]
	maxSoFar = array[0]

	for num in array[1:]:
		maxEndingHere = max(maxEndingHere + num, num)
		maxSoFar = max(maxSoFar,maxEndingHere)
	return maxSoFar


print(kadanesAlgorithm([100,8,5,-9,1,3,-2,3,4,7,2,-18,6,3,1,-5,6,20,-23,15,1,-3,4]))



