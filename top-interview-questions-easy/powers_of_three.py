import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # The clever approach.
        if n <= 0:
            return False
        else:
            # Alas, `math.log` returns a `float`.
            # return type(math.log(n, 3)) is int

            # Same idea, but `math.log(243, 3)` evaluates to 4.999999999999999,
            # not 5.
            # return math.log(n, 3) % 1 == 0

            # This should work (for relatively small powers of 3, anyway).
            # Alas, it fails for 129140162 (3 ** 17 - 1).
            # return math.isclose(
            #     math.log(n, 3),
            #     round(math.log(n, 3))
            # )

            # Finally, something that works.
            return 3 ** round(math.log(n, 3)) == n

        """
        # The naive approach:
        while n > 1:
            if n % 3 == 0:
                n = n // 3
            else:
                return False

        return n == 1
        """


s = Solution()
print(s.isPowerOfThree(129140162))
