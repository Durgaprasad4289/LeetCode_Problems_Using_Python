class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
       
        max_sum = cur_sum = sum(nums[:k])
        l=0
        for r in range(k,len(nums)):
            cur_sum +=(nums[r]-nums[l])
            max_sum = max(max_sum,cur_sum)
            l+=1
        return max_sum/k