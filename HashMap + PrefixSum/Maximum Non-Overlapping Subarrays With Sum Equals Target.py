class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        if len(nums)<1:
            return 0
        res = 0
        cur_sum = 0
        hash_set = {0}
        for num in nums:
            cur_sum += num
            if cur_sum-target in hash_set:
                res+=1
                hash_set = {0}
                cur_sum = 0
            else:
                hash_set.add(cur_sum)   
        return res