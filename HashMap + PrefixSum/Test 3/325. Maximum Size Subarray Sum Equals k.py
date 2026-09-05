class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        cur_sum = max_sum = 0
        table = {0:-1}
        for idx,num in enumerate(arr):
            cur_sum += num
            if cur_sum-k in table:
                max_sum = max(max_sum,idx-table[cur_sum-k])
            if cur_sum not in table:
                table[cur_sum] = idx
        return max_sum