class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowerBound = max(weights)
        upperBound = sum(weights)
        currCapacity = upperBound

        def canShip(capacity):
            ships, currCap = 1 , capacity
            for weight in weights:
                if currCap - weight < 0 :
                    ships +=1
                    #reset the capacity for the new ship
                    currCap = capacity
                currCap -= weight

            return ships <= days


        while lowerBound <= upperBound:
            capacity = (upperBound + lowerBound) // 2
            #sum of nums in weights till the mid is finished
            if canShip(capacity):
                currCapacity = min(capacity, currCapacity)
                upperBound = capacity - 1

            else:
                lowerBound = capacity + 1


        return currCapacity
        