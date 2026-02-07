# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums=sorted(set(nums))
        nums.sort()
        sequnce_len=0
        cur_ele=nums[0]
        smale_len=0
        for i in nums[1:]:
            cur_ele+=1
            if cur_ele==i:
                smale_len+=1
                sequnce_len=max(sequnce_len,smale_len)
            else:
                smale_len=0
                cur_ele=i
        return sequnce_len+1



       