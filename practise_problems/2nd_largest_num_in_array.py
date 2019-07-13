#arr = [15,1,12,18,34,17]
arr = [2,6,4,3,3,3,6,1,6,9,6,9,9,0,8,1,0,9,6,9,7]
first = arr[0]
second = arr[0]
third =arr[0]
fourth = arr[0]
for i in range(len(arr)):
	if arr[i] > first:
		second = first
		first = arr[i]

	if (arr[i]>second) and (arr[i]<first):
		third = second
		second = arr[i]

	if (arr[i]>third) and (arr[i]<first) and (arr[i]<second):
		fourth = third
		third = arr[i]

	if (arr[i]>fourth) and (arr[i]<first) and (arr[i]<second) and (arr[i]<third):
		fourth = arr[i]
print(first)
print(second)
print(third)
print(fourth)


print("*"*10)


