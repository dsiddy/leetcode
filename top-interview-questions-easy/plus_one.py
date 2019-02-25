from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        TODO(dsiddy): Try coming up with an iterative solution as well.
        """
        last_digit = digits.pop()

        if last_digit != 9:
            digits.append(last_digit + 1)

            return digits
        else:
            while last_digit == 9:
                if len(digits) == 0:
                    # Prepend 1 and 0 to the list of digits.
                    # TODO(dsiddy): Does this really require two `insert`
                    # calls?
                    digits.insert(0, 0)
                    digits.insert(0, 1)

                    return digits
                else:
                    # TODO(dsiddy): This looks more elegant, but results in
                    # nested lists. Any way to flatten 'em?
                    # return [self.plusOne(digits), 0]

                    solution = []
                    solution.extend(self.plusOne(digits))
                    solution.append(0)

                    return solution


s = Solution()
print(s.plusOne([9, 1, 2]))
