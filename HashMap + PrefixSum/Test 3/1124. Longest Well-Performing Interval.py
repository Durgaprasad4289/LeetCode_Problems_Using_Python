class Solution:
    def longestWPI(self, nums: List[int]) -> int:
        
        cur_sum = max_sum = 0
        table = {0:-1}
        for idx,num in enumerate(nums):
            cur_sum += 1 if num>8 else -1
            if cur_sum > 0:
                max_sum = idx+1
            if cur_sum-1 in table:
                max_sum = max(max_sum,idx-table[cur_sum-1])
            if cur_sum not in table:
                table[cur_sum] = idx
        return max_sum