class Solution:
    def longestSubarray(self, nums, k):  
        if not nums :
            return 0
        res = cur_sum = 0
        freq_map = {0:-1}
        for idx in range(len(nums)):
            cur_sum += nums[idx]
            if cur_sum - k in freq_map:
                res = max(res,idx-freq_map[cur_sum - k])
            if cur_sum not in freq_map:
                freq_map[cur_sum] = idx
                
        return res