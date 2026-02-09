
class Solution(object):
    def romanToInt( self,s):
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        prev=0
        for curr in s:
            if prev >d[curr]:
                res-=d[curr]
            else:
                res+=d[curr]
            prev=d[curr]
        return res
    
s=Solution()
a=s.romanToInt('III')
print(a)