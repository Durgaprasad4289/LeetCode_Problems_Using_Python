class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        max_len = 0
        table = {0:-1}
        cur_sum = 0
        for idx, num in enumerate(nums):
            if num == 0:
                cur_sum-=1
            else:
                cur_sum+=1
            if cur_sum in table:
                max_len = max(max_len,idx-table[cur_sum])
            else:
                table[cur_sum] = idx

        return max_len
        