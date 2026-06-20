class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = findLeftBound(nums, target)
        right = findRightBound(nums, target)
    

        return [left, right]

def findLeftBound(nums: List[int], target: int) -> int:
    index = -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            index = mid
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return index


def findRightBound(nums: List[int], target: int) -> int:
    index = -1
    left , right = 0 , len(nums) -1 
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            index = mid
            left = mid + 1
        
        elif nums[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1
        
    
    return index
            
        