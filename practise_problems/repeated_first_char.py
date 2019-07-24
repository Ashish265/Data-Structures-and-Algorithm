def repeated_first_characters(S):

    l =[]
    for i in range(0,len(S)):
        if S[i] in S[:i]or S[i] in S[i+1:]:
            l.append(S[i])
        else:
            continue
            
            
    if len(l) > 0:
        return l[0]
    return None

print(repeated_first_characters("abdcabc"))
print(repeated_first_characters("abdc"))