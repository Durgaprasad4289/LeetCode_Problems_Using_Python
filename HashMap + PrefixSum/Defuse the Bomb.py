class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        res = []
        n = len(code)
        if k>0:
            for i in range(n):
                t = 0
                for j in range(1,k+1):
                    idx = (i+j) % n
                    t += code[idx]
                res.append(t)
        else:
            for i in range(n):
                t = 0
                for j in range(1,-1*k+1):
                    idx = (i-j) % n
                    t += code[idx]
                res.append(t)
        return res