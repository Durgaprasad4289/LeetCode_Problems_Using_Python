class Solution:
    def subarraySum(self, nums, k: int) -> int:
        freq = {0:1}
        res = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in freq:
                res += freq[cur_sum-k]
            freq[cur_sum] = freq.get(cur_sum,0)+1
        return res 