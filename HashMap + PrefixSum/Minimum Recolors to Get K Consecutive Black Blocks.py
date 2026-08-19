class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        freq = defaultdict(int )
        l = 0 
        res = float('inf')
        for r in range(len(s)):
            freq[s[r]] += 1
            if (r-l+1) == k:
                res = min(res,k-freq['B'])
                freq[s[l]]-=1
                l+=1
        return res