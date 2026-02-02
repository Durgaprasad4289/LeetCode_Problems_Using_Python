# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting
# some (can be none) of the characters without disturbing the relative positions of the remaining
# characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

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