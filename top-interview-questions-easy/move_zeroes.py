from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_zeroes = nums.count(0)

        while num_zeroes > 0:
            nums.remove(0)
            nums.append(0)

            num_zeroes = num_zeroes - 1


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
