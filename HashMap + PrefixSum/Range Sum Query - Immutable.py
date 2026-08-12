class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]