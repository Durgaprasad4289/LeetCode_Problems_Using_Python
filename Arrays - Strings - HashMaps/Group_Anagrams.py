
strs = ["eat","tea","tan","ate","nat","bat"]

def anagram(a):
    if len(a)==0:
        return []
    d={}
    for i in a:
        j="".join(sorted(i))
        if j in d:
            d[j].append(i)
        else:
            d[j]=[i]
    return list(d.values())

print(anagram(strs))