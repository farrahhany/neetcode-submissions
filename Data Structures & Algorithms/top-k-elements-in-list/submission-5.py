from collections import Counter , defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: count frequencies
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        # {1:1, 2:2, 3:3}

        # Step 2: sort by frequency (highest first) and take k
        sorted_count = sorted(count, key=lambda x: count[x], reverse=True)
        return sorted_count[:k]



    