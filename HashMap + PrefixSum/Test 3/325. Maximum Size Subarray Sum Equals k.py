
# ========= Solution 1 ======== 

class Solution:
    def maxSubarraySum(self, arr, k):
        if not arr:
            return 0
        l = 0
        cur_sum = max_sum = sum(arr[:k])
        for r in range(k,len(arr)):
            cur_sum += (-arr[l]+arr[r])
            max_sum = max(max_sum,cur_sum)
            l+=1
        return max_sum

# ========= Solution 2 ======== 
