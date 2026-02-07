# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

nums = [1,2,3,1]
k = 3

def dups(a, k):
    d = {}
    for i in range(len(a)):
        j = a[i]
        if j in d and abs(d[j] - i) <= k: 
            return True
        d[j] = i
    return False

print(dups(nums, k))  
