class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        freq = {0:-1}
        max_len = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i] if nums[i]==1 else -1
            if cur_sum in freq:
                max_len = max(max_len,i-freq[cur_sum])
            else: freq[cur_sum] = i
        return max_len