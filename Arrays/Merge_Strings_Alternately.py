# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.


# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

class Solution(object):
    def mergeAlternately(self, w1, w2):
        a=b=0
        cur_word=1
        res=''
        while a < len(w1) and b<len(w2):
            if cur_word==1:
                res+=w1[a]
                a+=1
                cur_word=2
            else:
                res+=w2[b]
                b+=1
                cur_word=1
        while a<len(w1):
            res+=w1[a]
            a+=1
        while b<len(w2):
            res+=w2[b]
            b+=1
        return res
    
s=Solution()
a=s.mergeAlternately("abc","pqr")

print(a)