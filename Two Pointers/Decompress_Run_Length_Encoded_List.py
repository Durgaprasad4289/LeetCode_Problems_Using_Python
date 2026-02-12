class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(0,len(nums),1):
            print(i)
s=Solution()
print(s.decompressRLElist( [1,2,3,4]))
