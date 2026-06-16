class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initial check for different lengths is correct and efficient
        if len(s) != len(t):
            return False
        
        # 1. Convert strings to lists of characters and sort them using the sorted() function
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        # 2. Compare the two sorted lists (or you could rejoin them into strings)
        return s_sorted == t_sorted