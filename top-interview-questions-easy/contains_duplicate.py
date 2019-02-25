from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        nums.sort()

        current_value = nums[0]
        index = 1

        while index < len(nums):
            value = nums[index]

            if value == current_value:
                return True
            else:
                current_value = value
                index = index + 1

        return False


s = Solution()
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
