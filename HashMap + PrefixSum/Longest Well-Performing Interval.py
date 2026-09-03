class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = cur_sum = 0
        table = {0:-1}
        for i in range(len(hours)):
            cur_sum += 1 if hours[i] >8 else -1
            if cur_sum > 0:
                res = i+1
            if cur_sum - 1 in table  :
                res = max(res,i-table[cur_sum-1])
            if cur_sum not in table :
                table[cur_sum] = i
        return res
