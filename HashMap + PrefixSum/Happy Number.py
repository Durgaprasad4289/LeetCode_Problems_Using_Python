class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n):
            cur_sum = 0
            while n:
                digit = n%10
                cur_sum += digit*digit
                n //= 10
            return cur_sum
        
        slow = fast = n
        while True:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))

            if slow == fast:
                return slow == 1
            
