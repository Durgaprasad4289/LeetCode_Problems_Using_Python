#   Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#   An input string is valid if:

#   1.Open brackets must be closed by the same type of brackets.
#   2.Open brackets must be closed in the correct order.
#   3.Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "([)]"
# Output: false

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
