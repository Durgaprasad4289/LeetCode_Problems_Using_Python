class Solution(object):
    def isValid(self, s):
        if len(s)%2!=0:
            return False
        a=[]
        d={'{':'}','(':')','[':']'}
        
        for i in s:
            if i in d:
                a.append(i)
            else:
                if not a :
                    return False

                p=a.pop()
                if d[p]!=i:
                    return False
        return len(a)==0
        return None 
s=Solution()
print(s.isValid("()[]{}"))  # True# Logic: Valid Parenthesis using Stack
