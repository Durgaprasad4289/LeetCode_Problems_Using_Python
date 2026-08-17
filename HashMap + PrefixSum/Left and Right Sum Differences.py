class Solution:
    def leftRightDifference(self, nums):
        leftTotal = 0
        leftSum = []
        for num in nums:
            leftSum.append(leftTotal)
            leftTotal+=num
        leftTotal = 0
        for i in range(len(nums)-1,-1,-1):
            leftSum[i] = abs(leftSum[i]-leftTotal)
            leftTotal += nums[i]
            
        return leftSum