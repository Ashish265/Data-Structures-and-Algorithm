def largestRange(array):
    # Write your code here.
	
	longestLength = 0
	bestRange = []
	nums = {}
	
	for num in array:
		nums[num] = True
		
	for num in array:
		if not nums[num]:
			continue
		
		nums[num]  = False
		
		left = num - 1
		right = num + 1
		currentLength = 1
		
		while left in nums:
			nums[left] = False
			currentLength += 1
			left -= 1
			
		while right in nums:
			nums[right] = False
			currentLength += 1
			right += 1
			
		if currentLength > longestLength:
			
			longestLength = currentLength
			
			bestRange = [left + 1, right - 1]
			
	return bestRange

print(largestRange([1,11,3,0,15,5,2,4,10,7,12,6]))
