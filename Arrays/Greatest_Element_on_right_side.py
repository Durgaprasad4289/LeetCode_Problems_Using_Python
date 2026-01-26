
# Traverse the array from right to left so that all right-side elements
# are already processed when handling the current index.

# Maintain a variable that always stores the maximum value seen so far
# on the right side of the current position.

# The last element has no elements to its right, so it is replaced with -1.

# For each index:
# 1. Save the current element before overwriting it.
# 2. Replace the current element with the stored right-side maximum.
# 3. Update the right-side maximum using the saved element.

# Continue this process until the start of the array is reached.

# The final array contains, at each index, the greatest element
# present to its right.


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        right_max=-1
        current_element=0
        for i in range(len(arr)-1,-1,-1):
            current_element,arr[i]=arr[i],right_max
            right_max=max(right_max,current_element)
        return arr