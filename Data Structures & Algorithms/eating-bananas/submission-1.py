class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = math.ceil(sum(piles) / h)
        valid = False
        last_valid_k = 0
        while min_k <= max_k:
            mid_k = (max_k + min_k) // 2
            # if mid_k valid, max_k = mid_k - 1
            # if mid_k not valid, min_k = mid_k + 1
            hours = 0
            for pile in piles:
                pile_hour = math.ceil(pile / mid_k)
                hours += pile_hour
            if hours <= h:
                max_k = mid_k - 1
                valid = True
                last_valid_k = mid_k
            else:
                min_k = mid_k + 1
                valid = False
        if valid:
            return mid_k
        else:
            return last_valid_k