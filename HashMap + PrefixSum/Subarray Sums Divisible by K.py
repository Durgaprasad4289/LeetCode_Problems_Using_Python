
class solution:
    def subarraySumDivisibleByK(nums,k):
        if len(nums)<1:
            return 0
        res = 0
        prefixSum = 0
        freq_map = {0:1}
        for num in nums:
            prefixSum += num
            reminder = prefixSum % k
            if reminder in freq_map:
                res += freq_map[reminder]
            freq_map[reminder] = freq_map.get(reminder,0)+1
        return res
    
    