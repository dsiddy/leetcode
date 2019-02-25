import math


class Solution:
    # TODO(dsiddy): Get this running more quickly. It times out for the test
    # case 999983.
    def countPrimes(self, n: int) -> int:
        """Count primes using the sieve of Eratosthenes."""
        possible_primes = set(range(2, math.floor(math.sqrt(n)) + 1))  # Of course, as initialized, this contains composite numbers as well, but these'll be weeded out. # noqa: E501
        composites = set()

        # First, filter the composites out of the list of possible primes.
        for i in possible_primes:
            composites.update(
                set(
                    filter(lambda j: j % i == 0 and j != i, possible_primes)
                )
            )

        primes = possible_primes - composites

        integers = set(range(2, n))  # By definition, 1 is not prime.
        composites = set()  # Reinitialize this for use below.

        for i in primes:
            composites.update(
                set(
                    filter(lambda j: j % i == 0 and j != i, integers)
                )
            )

        integers = integers - composites

        return len(integers)


s = Solution()
print(s.countPrimes(499979))
