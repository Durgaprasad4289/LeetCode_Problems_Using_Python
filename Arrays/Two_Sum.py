
# Logic: Two Sum using Hash Map (Dictionary)
# -----------------------------------------
# Goal:
# Find two indices such that a[i] + a[j] == target (t)

# Approach:
# We iterate through the array only once (O(n) time complexity).
# A dictionary is used to store numbers we have already seen
# along with their indices for quick lookup.

# Steps:
# 1. Traverse the array using enumerate() to get both index and value.
# 2. For each element, calculate the required value (diff)
#    diff = target - current_element
# 3. Check if diff already exists in the dictionary:
#    - If yes, we have found two numbers whose sum equals the target.
#      Return the index of diff (stored earlier) and the current index.
# 4. If not found, store the current element and its index in the dictionary.
# 5. If no pair is found after traversal, the function returns None.

# Why this works:
# Dictionary lookup is O(1), so the overall time complexity is O(n).
# This is more efficient than a nested loop approach (O(n²)).


array=[1,7,2,8]
def function(a,t):
    dictionary={}
    diff=0
    for i,j in enumerate(a):
        diff=t-j
        if diff in dictionary:
            return [dictionary[diff],i]
        dictionary[j]=i 

print(function(array,9))

