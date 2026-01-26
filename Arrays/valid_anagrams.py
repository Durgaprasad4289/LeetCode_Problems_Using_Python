class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        a=[0]*26

        for i in range(len(s)):
            a[ord(s[i])-ord('a')]+=1
        
        for i in range(len(s)):
            a[ord(s[i])-ord('a')]-=1
        
        for i in range(26):
            if a[i] !=0 :
                return False
        return True

        
s=Solution()
print(s.isAnagram("anagram","ngaram"))