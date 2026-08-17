class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        # total = 0
        # for i in range(len(arr)):
        #     cur_sum = 0
        #     for j in range(i,len(arr)):
        #         cur_sum += arr[j]
        #         if (j-i+1) % 2 != 0:
        #             total += cur_sum
        # return total

        res = 0
        n = len(arr)
        for idx,num in enumerate(arr):
            res += ((idx+1)*(n-idx)+1)//2*num
        return res
