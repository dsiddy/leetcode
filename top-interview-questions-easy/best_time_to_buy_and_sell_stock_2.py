import json
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = {}

        for index in range(len(prices) - 1):
            buy_date = index + 1

            profits[buy_date] = {
                (sell_date + (buy_date + 1)): price - prices[index]
                for sell_date, price in enumerate(prices[(index + 1):])
            }

        # TODO(dsiddy): Determine how to walk this data structure.

        # This works better than `pprint` for my purposes.
        print(json.dumps(profits, indent=4))


s = Solution()
s.maxProfit([7, 1, 5, 3, 6, 4])
