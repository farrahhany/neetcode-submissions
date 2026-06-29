class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        boundary_index = {}
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # left is sorted
            if nums[left] <= nums[mid] :
                if target > nums[mid] or target < nums[left]: # means we search the right portion
                    left = mid + 1
                else:
                    right = mid - 1
            # right is sorted
            else:
                if target < nums[mid] or target > nums[right]: # means we search the left portion
                    right = mid - 1
                else:
                    left = mid + 1




        return -1