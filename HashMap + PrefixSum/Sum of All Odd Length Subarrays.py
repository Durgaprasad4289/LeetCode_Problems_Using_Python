class Solution:
    def sumOddLengthSubarrays(self, arr):
        total = 0

        for i in range(len(arr)):
            current_sum = 0

            for j in range(i, len(arr)):
                current_sum += arr[j]

                length = j - i + 1

                if length % 2 == 1:
                    total += current_sum

        return total