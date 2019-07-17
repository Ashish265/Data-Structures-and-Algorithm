def three_sum(A,targetSum):

	A.sort()
	triplets = []


	for i in range(len(A)-2):

		left = i + 1
		right = len(A)-1

		while left < right:
			currentSum = A[i] + A[left] + A[right]

			if currentSum == targetSum:

				triplets.append([A[i],A[left],A[right]])

				left += 1
				right -= 1

			elif currentSum < targetSum:
				left += 1

			elif currentSum > targetSum:

				right -=1

	return triplets



print(three_sum([12,3,1,2,-6,5,-8,6],0))
