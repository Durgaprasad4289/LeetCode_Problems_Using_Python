class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        res = 0
        cur_sum = 0
        l = 0
        freq = {0:1}
        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum - goal in freq:
                res += freq[cur_sum - goal]
            freq[cur_sum] = freq.get(cur_sum,0)+1
        return res
