class Solution:
    def maxScore(self, s: str) -> int:
        totalSum = sum(int(num) for num in s )
        zeros = 0
        maxSum = 0
        for i in range(len(s)-1):
            num = s[i]
            if num == "0" :
                zeros+=1
            else:
                totalSum-=1
            maxSum = max(maxSum,totalSum+zeros)
        return maxSum
