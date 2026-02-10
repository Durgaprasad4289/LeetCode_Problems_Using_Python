class Solution(object):
    def isValidSudoku(self, b):
        
        for i in range(9):
            res=set()
            for j in range(9):
                ele=b[i][j]
                if ele!="." and ele in res:
                    return False
                res.add(ele)

        for i in range(9):
            res=set()
            for j in range(9):
                ele=b[j][i]
                if ele!="." and ele in res:
                    return False
                res.add(ele)
        

        for i in range(0,9,3):
            for j in range(0,9,3):
                res=set()
                for x in range(3):
                    for y in range(3):
                            ele=b[x+i][y+j]
                            if ele!="." and ele in res:
                                return False
                            res.add(ele)
        return True
  
board1 =[[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
s=Solution()
print(s.isValidSudoku(board1))


