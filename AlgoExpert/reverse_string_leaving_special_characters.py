def reverseStringLeavingChar(string,chara):
	"Reverse the string keeping the character in the argument at its index"

	leftIdx = 0
	rightIdx = len(string) - 1
	str_list = list(string)

	while leftIdx < rightIdx:

		if str_list[leftIdx] == chara:
			leftIdx += 1

		if str_list[rightIdx] == chara:
			rightIdx -= 1

		if str_list[leftIdx] != chara and str_list[rightIdx] != chara:

			str_list[leftIdx],str_list[rightIdx] = str_list[rightIdx],str_list[leftIdx]

			leftIdx += 1

			rightIdx -= 1
	return "".join(str_list)

print(reverseStringLeavingChar("ashish",'a'))