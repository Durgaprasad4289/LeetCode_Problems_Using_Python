#  - Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements ofnums except nums[i].
#  - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#  -You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product=right_propuct=1
        left_product_array=[]

        for i  in range(len(nums)):
            left_product_array.append(left_product)
            left_product*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            nums[i],right_propuct=right_propuct,nums[i]*right_propuct
        for i in range(len(nums)):
            nums[i]=nums[i]*left_product_array[i]
        
        return nums

s=Solution()
a=s.productExceptSelf([1,2,3,4])

print(a)
