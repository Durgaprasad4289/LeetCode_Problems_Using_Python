class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        res=cur=0
        nums=set(nums)
        for i in nums:
            if i-1 not in nums:
                cur+=1
                y=i+1
                while y in nums:
                    cur+=1
                    y+=1
            res=res if res>cur else cur
            cur=0
        return res


nums = [100,4,200,1,3,2]

s=Solution()
print(s.longestConsecutive(nums))