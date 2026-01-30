# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

 

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1

# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.

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