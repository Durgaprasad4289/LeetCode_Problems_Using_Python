class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum = 0 
        res = []
        for num in nums:
            cur_sum+=num
            res.append(cur_sum)
        return res
        