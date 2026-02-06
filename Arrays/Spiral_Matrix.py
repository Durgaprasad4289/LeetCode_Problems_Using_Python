class Solution(object):
    def spiralOrder(self, m):
        if len(m)==0:
            return m
        res=[]
        def spiral(m):
            if len(m)==0:
                return []
            res.extend(m[0])
            new_array=list(zip(*m[1:]))[::-1]
            spiral(new_array)
        spiral(m)
        return res
        

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s=Solution()
print(s.spiralOrder(matrix))