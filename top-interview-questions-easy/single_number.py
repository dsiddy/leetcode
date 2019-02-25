from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Essentially, we want `set(nums) - (nums - set(nums))`."""

        # TODO(dsiddy): See if I can avoid storing `set(nums)`.
        elements = set(nums)

        for element in elements:
            nums.remove(element)

        for num in nums:
            elements.remove(num)

        return elements.pop()


s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))
