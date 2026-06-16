class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set(nums)
        if len(nums) != len(duplicate):
            return True
        return False