
class Solution(object):
    def mergeAlternately(self, w1, w2):
        a=b=0
        cur_word=1
        res=''
        while a < len(w1) and b<len(w2):
            if cur_word==1:
                res+=w1[a]
                a+=1
                cur_word=2
            else:
                res+=w2[b]
                b+=1
                cur_word=1
        while a<len(w1):
            res+=w1[a]
            a+=1
        while b<len(w2):
            res+=w2[b]
            b+=1
        return res
    
s=Solution()
a=s.mergeAlternately("abc","pqr")

print(a)