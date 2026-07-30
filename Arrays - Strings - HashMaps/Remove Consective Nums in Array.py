def remove_duplicates(nums):
    if not nums :
        return nums
    while True:
        stack = []
        i = 0
        while i<len(nums):
            j = i
            while j<len(nums) and nums[i] == nums[j]:
                j+=1
            if j-i == 1:
                stack.append(nums[i])
            i = j
        if nums == stack:
            return stack
        nums = stack

    

# n = int(input())
# arr = list(map(int,input().split()))[:n]
stack = remove_duplicates([1,1,1,1,2,3,3,3,4,3,3,5,6,6,5])

for i in stack:
        print(i,end=" ")

