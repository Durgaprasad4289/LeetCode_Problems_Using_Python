
class Solution(object):
    def twoSum(self, nums, target):
        map={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in map:
                return [map[diff],i]
            map[j]=i
                    
s=Solution()
print(s.twoSum([2,7,11,15],9))  # Output: [0, 1]

