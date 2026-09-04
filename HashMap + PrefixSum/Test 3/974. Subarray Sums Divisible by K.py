class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        res = 0
        cur_sum = 0
        table = {0:1}
        for num in nums:
            cur_sum += num
            reminder = (cur_sum-k)%k
            if reminder in table:
                res+= table[reminder]
            table[reminder] = table.get(reminder,0)+1
        return res