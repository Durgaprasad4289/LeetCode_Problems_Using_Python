# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


#--------------- Shorter Form ---------------
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums))!=len(list(nums))
    
# --------------- Longer Form ---------------
class Solution(object):
    def containsDuplicate(self, nums):
        d={}
        for i in nums:
            if i in d:
                return True
            d[i]=1
        return False
    
s=Solution()
print(s.containsDuplicate([1,2,3,1]))