class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerBound , upperBound = 1 , max(piles)
        currRate = upperBound

        def canFinish(rate):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / rate)
            
            return total_hours <= h

        while lowerBound <= upperBound:
            mid = (lowerBound + upperBound) // 2

            # if feasible condition
            if canFinish(mid):
                currRate = min(currRate , mid)
                upperBound = mid - 1

            
            else:
                lowerBound = mid + 1
        

        return currRate

