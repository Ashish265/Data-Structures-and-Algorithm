def findClosestValueInBst(tree, target):
    # Write your code here.
	closest = float('inf')
	currentNode = tree
	
	while currentNode is not None:
		
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
			
		if target < currentNode.value:
			currentNode = currentNode.left
			
		elif target > currentNode.value:
			currentNode = currentNode.right
			
		else:
			break
	return closest