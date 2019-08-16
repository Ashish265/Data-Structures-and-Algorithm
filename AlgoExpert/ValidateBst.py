def validateBst(tree):
    # Write your code here.
	return ValidateBstHelper(tree,float("-inf"),float('inf'))

def ValidateBstHelper(tree,minValue,maxValue):
	if tree is None:
		return True
	if tree.value < minValue or tree.value >= maxValue :
		return False
	
	leftIsValid = ValidateBstHelper(tree.left,minValue,tree.value)
	
	return leftIsValid and ValidateBstHelper(tree.right,tree.value,maxValue)