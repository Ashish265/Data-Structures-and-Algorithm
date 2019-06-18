from stack import ArrayStack

def is_matched_html(raw):
	""" Returns True if all HTML tags are properly matched, False otherwise """
	S = ArrayStack()

	j = raw.find('<')                 # find first < character if any

	while j != -1:
		k = raw.find(">",j+1)         # find next > character if any

		if k==-1:
			return False              # invalid tag

		tag = raw[j+1:k]              # dtrip away <>

		if not tag.startswith('/'):
			S.push(tag)
		else:
			if S.is_empty():
				return False
			if tag[1:] != S.pop():
				return False

		j = raw.find("<",k+1)

	return S.is_empty()