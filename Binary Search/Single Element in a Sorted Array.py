class Solution:
    def singleNonDuplicate(self, nums) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        xor_sum = 0
        for num in nums:
            xor_sum^=num
        return xor_sum
s = Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))

# TIME COMPLEXITY O(N)
# SPACE COMPLEXITY O(1)

# =========== MUCH OPTIMAL WAY (BINARY SEARCH) ============

