class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        res = cur_sum = 0
        freq_sum = {0:1}
        for num in nums:
            cur_sum+=num
            if cur_sum - k in freq_sum:
                res += freq_sum[cur_sum - k]
            freq_sum[cur_sum] = freq_sum.get(cur_sum, 0 )+1
        return res
