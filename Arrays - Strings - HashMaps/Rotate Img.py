class Solution(object):
    def rotate(self, nums):
        if not nums:
            return []
        nums=list(zip(*nums))
        return [list(i)[::-1] for i in nums]
    
n= [[1,2,3],[4,5,6],[7,8,9]]
s=Solution()
print(s.rotate(n))