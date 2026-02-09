

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
s=Solution()
print(s.replaceElements([17,18,5,4,6,1]))  #