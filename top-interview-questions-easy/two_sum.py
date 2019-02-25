from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            diff = target - nums[index]

            try:
                diff_index = nums.index(diff)

                # Remember, we can't reuse values.
                if diff_index == index:
                    continue
            except ValueError:
                continue

            return [index, diff_index]


s = Solution()
print(s.twoSum([3, 2, 4], 6))
