

class Solution(object):
    def isSubsequence(self,s1, s2):
        if s1=="":
            return True
        if len(s1)>len(s2):
            return False
        i=0
        n1=len(s1)
        n2=len(s2)
        for j in range(n2):
            if n1==i:
                return True
            if s1[i]==s2[j]:
                i+=1
        return n1==i
        

s = "b"
t = "ahbgdc"
s=Solution()
print(s.isSubsequence(s,t))