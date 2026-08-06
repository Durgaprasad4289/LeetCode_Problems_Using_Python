class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = [0]*26
        s2 = [0]*26

        for ch1,ch2 in zip(s,t):
            s1[ord(ch1)-97]+=1
            s2[ord(ch2)-97]+=1
        return s1 == s2