class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # return max(d,key=d.get)
        max=0
        prev=0
        for i,j in d.items():
            if j>prev:
               max=i
               prev=j
        return(max)

s=Solution()
print(s.majorityElement([3,3,3,3,2,1,1,1]))
        