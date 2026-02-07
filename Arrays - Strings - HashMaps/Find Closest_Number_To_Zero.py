# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1

class Solution(object):
    def findClosestNumber(self,nums):
        res=float('inf')
        for i in nums:
            if abs(i)<abs(res):
                res=i
            elif abs(i)==abs(res):
                if i>res:
                    res=i
        return res

s=Solution()
res=s.findClosestNumber( [3,3,4,2,-1,-2])

print(res)
