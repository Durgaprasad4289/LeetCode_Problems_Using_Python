
class Solution(object):
    def findClosestNumber(self,nums):
        res=float('inf')
        for i in nums:
            if abs(i)<abs(res):
                res=i
            elif abs(i)==abs(res):
                if i>res:
                    res=i
        return res

s=Solution()
res=s.findClosestNumber( [3,3,4,2,-1,-2])

print(res)
