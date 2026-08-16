class NumArray:
    def __init__(self, nums: List[int]):
        self.prefixSum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefixSum.append(total)
    def sumRange(self, left: int, right: int) -> int:
        leftSum = 0 if left == 0 else self.prefixSum[left - 1]
        return self.prefixSum[right] - leftSum