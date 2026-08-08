class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
        
        d = {}
        for r in range(len(nums)):
            if nums[r] in d:
                if abs(r-d[nums[r]])<=k:
                    return True
            d[nums[r]] = r

        return False
