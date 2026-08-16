class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur_sum = min_sum = 0
        for num in nums:
            cur_sum += num
            min_sum = min(min_sum,cur_sum)
        return abs(min_sum)+1