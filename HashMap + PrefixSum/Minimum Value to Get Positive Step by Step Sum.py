class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        cursum = 0
        minPrefixSum = 0
        for num in nums:
            cursum += num
            minPrefixSum = min(cursum,minPrefixSum)
        return abs(minPrefixSum)+1