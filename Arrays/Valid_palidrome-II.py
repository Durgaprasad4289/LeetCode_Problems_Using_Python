# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true

class Solution(object):
    def validPalindrome(self, s):
        if len(s)==1:
            return True
        i=0
        j=len(s)-1

        while i<=j:
            if s[i]!=s[j]:
                s1=s[i+1:j+1]
                s2=s[i:j]
                print(s1,s2)
                return s1==s1[::-1] or s2==s2[::-1]
            i+=1
            j-=1
        return True
s=Solution()
s1=s.validPalindrome("abc")

print(s1)
        