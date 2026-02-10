
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



       