from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # 1. Create a set from the list. This automatically removes duplicates.
        unique_elements = set(nums)
        
        # 2. Compare the length of the original list with the length of the set.
        # If the set is smaller than the list, duplicates were removed, so return True.
        return len(unique_elements) != len(nums)