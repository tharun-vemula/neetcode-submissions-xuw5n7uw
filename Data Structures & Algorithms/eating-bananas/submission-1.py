class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        i,j = 1, maximum
        res = maximum

        while i <= j:
            mid = (i+j) // 2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid
            if time <= h:
                res = min(mid, maximum)
                j = mid - 1
            else:
                i = mid + 1
        
        return res


        