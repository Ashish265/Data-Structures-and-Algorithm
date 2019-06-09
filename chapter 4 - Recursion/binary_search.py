def binary_searchh(data,target,low,high):
	""" Returns True if target is found in indicated portion of a python list"""

	if low > high:
		return False
	else:
		mid = (low+high)//2

		if target == mid:
			return True
		elif target < data[mid]:
			#recur on the portion on the left of the mid
			return binary_searchh(data,target,low,mid-1)

		else:
			return binary_searchh(data,target,mid+1,high)

print(binary_searchh([1,2,3,4,5,6],5,1,6))