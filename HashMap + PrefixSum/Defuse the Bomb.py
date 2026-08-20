# ---------- VERSION 1 O(n x |k|) ---------
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

# ---------- VERSION-2  O(n) ---------

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code)
        if k == 0:
            return [0]*n

        res = [0]*n
        
        if k>0:
            window_sum = sum(code[j%n] for j in range(1,k+1))
            for i in range(n):
                res[i] = window_sum
                window_sum -= code[(i+1)%n]
                window_sum += code[(i+k+1)%n]
        else :
            k = -k
            window_sum = sum(code[-j%n] for j in range(1,k+1))
            for i in range(n):
                res[i] = window_sum
                window_sum -= code[(i-k)%n]
                window_sum += code[i%n]
        return res