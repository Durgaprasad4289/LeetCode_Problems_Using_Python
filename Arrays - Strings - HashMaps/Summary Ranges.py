
class Solution(object):
    def summaryRanges(self, nums):
        last=prev=nums[0]
        res=[]
        for i in nums[1:]:
            if prev+1 != i:
                if last== prev:
                    res.append(str(last))
                else:
                    res.append(str(last)+"->"+str(prev))
                last=i
            prev=i
        if last!=prev:
            res.append(str(last)+"->"+str(prev))
        else:
            res.append(str(last))
        if len(res)==0:
            res.append(str(nums[0])+"->"+str(nums[-1]))
        return res 
nums = [0,1,2,4,6,7,8,9]
S=Solution()
print(S.summaryRanges(nums))
