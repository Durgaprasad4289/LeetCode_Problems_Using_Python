
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        d={}
        for i in stones:
            if i  in d:
                d[i]+=1
            else:
                d[i]=1
        res=0
        for i in set(jewels):
            if  i in d:
                res+=d[i]
        return res
        
s=Solution()
print(s.numJewelsInStones( "aA","aAAbbbb"))