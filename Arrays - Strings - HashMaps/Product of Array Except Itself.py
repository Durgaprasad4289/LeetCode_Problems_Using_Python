
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
