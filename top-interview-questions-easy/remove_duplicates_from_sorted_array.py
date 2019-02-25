from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prev_value = nums[0]
        index = 1

        while index < len(nums):
            value = nums[index]

            if value == prev_value:
                nums.pop(index)
            else:
                prev_value = value
                index = index + 1

        return len(nums)


s = Solution()
print(s.removeDuplicates([1, 2, 2, 3, 4, 4, 4]))
