class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = set(nums1)
        # nums2 = set(nums2) 
        # res = []
        # if len(nums1)<len(nums2):
        #     for num in nums1:
        #         if num in nums2:
        #             res.append(num)
        # else:
        #     for num in nums2:
        #         if num in nums1:
        #             res.append(num)
        # return res

        return list(set(nums1) & set(nums2))