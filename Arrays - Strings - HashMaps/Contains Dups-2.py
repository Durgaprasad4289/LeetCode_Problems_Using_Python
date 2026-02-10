
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
