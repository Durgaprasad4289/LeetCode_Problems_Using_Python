class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code)
        if k == 0:
            return [0]*n

        res = [0]*n
        if k>0:
            window_sum = sum(num for num in code[1:k+1])
            for i in range(len(code)):
                res[i] = window_sum
                window_sum -= code[(i+1)%n]
                window_sum += code[(i+k+1)%n]
            return res
        else:
            k = -k
            window_sum = sum(code[(i-k)%n] for i in range(k))
            for i in range(len(code)):
                res[i] = window_sum
                window_sum -= code[(i-k)%n]
                window_sum += code[i]
            return res 


        # if k>0:
        #     for i in range(n):
        #         t = 0
        #         for j in range(1,k+1):
        #             idx = (i+j) % n
        #             t += code[idx]
        #         res.append(t)
        # else:
        #     for i in range(n):
        #         t = 0
        #         for j in range(1,-1*k+1):
        #             idx = (i-j) % n
        #             t += code[idx]
        #         res.append(t)
        # return res