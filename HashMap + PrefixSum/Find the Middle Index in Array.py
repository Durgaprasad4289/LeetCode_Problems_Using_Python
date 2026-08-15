class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for idx in range(len(nums)):
            right = total - left - nums[idx]
            if left == right:
                return idx
            left += nums[idx]

        return -1