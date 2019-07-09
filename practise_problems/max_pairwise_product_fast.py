def maxPairwiseFast(number,a):
	"Returns the product of the two maximum number in an array"

	max_index1 = -1
	max_index2 = -1

	for i in range(0,number):
		if a[i] > a[max_index1]:
			max_index1 = i
		else:
			continue

	for j in range(0,number):
		if (a[j] !=a[max_index1]) and (a[j] > a[max_index2]):
			max_index2 = j
		else:
			continue

	res = a[max_index1]*a[max_index2]

	return res

print(maxPairwiseFast(5,[1,8,9,7,5]))
print(maxPairwiseFast(6,[1,8,9,7,5,10]))
