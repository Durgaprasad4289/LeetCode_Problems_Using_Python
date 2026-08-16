class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        total = 0
        for num in nums:
            total+=num
        left = 0
        for idx in range(len(nums)):
            right = total - left - nums[idx]
            if left == right:
                return idx
            left += nums[idx]
        return -1