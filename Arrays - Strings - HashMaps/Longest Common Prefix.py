strs = ["reflower","flow","flight"]
def longestCommonPrefix( strs):
    min_str=min(strs,key=len)
    t=""
    res=""
    c=0
    k=0
    for i in range(len(min_str)):
        if c==1 and k==0:
            return ""
        t+=min_str[i]
        if all( t in j[:i+1] for j in strs):
            res=t
            k=1
        else:
            c=1
    return res
print(longestCommonPrefix(strs))