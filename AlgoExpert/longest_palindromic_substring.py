def longestPalindromicSubstring(string):

	currentLongest = [0,1]

	for i in range(len(string)):

		odd = getLongestPalindromFrom(string,i-1,i+1)

		even = getLongestPalindromFrom(string,i-1,i)

		longest = max(odd, even,key = lambda x: x[1] - x[0])

		currentLongest = max(longest, currentLongest,key = lambda x: x[1] - x[0])

	return string[currentLongest[0]:currentLongest[1]]


def getLongestPalindromFrom(string,leftIdx,rghtIdx):

	while leftIdx >=0 and rghtIdx < len(string):

		if string[leftIdx] != string[rghtIdx]:
			break

		leftIdx -= 1
		rghtIdx += 1

	return [leftIdx + 1,rghtIdx]


print(longestPalindromicSubstring('abaxyzzyxf'))

