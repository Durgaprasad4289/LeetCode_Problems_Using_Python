class Solution:
    def maxProduct(self, n: int) -> int:
        if n<=10:
            return 0
        n = sorted(str(n))
        return int(n[-1])*int(n[-2])