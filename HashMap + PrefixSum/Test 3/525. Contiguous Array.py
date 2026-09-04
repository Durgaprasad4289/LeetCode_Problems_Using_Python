class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        cur_sum = 0
        table = {0:-1}
        res = 0
        for idx,num in enumerate(nums):
            cur_sum += num if num == 1 else -1
            if cur_sum in table:
                res = max(res,idx-table[cur_sum])
            else:
                table[cur_sum] = idx
        return res