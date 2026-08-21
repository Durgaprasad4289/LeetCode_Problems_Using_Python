class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        def solve(nums,k):
            res = l = odds = 0
            for r in range(len(nums)):
                odds += 1 if nums[r]%2 else 0
                while  odds > k:
                    if nums[l]%2 :
                        odds-=1
                    l+=1
                res += (r-l+1)
            return res

        return solve(nums,k)-solve(nums,k-1)
