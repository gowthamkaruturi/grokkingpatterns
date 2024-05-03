import math
from typing import List


class BinarySearchSolution:
    def __init__(self) -> None:
        pass

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        min_speed = 1
        ans = max_speed
        while min_speed <= max_speed:
            mid = (min_speed+max_speed)//2
            time=0
            for pile in piles:
                time+=math.ceil(pile/mid)
            if time <=h:
                ans = min(ans, mid)
                max_speed = mid-1
            else:
                min_speed=mid+1
        return ans        
    
  # """Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

  #     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time."""
    def findMin(self, nums:List[int])->int:
        left , right, n = 0, len(nums)-1, len(nums)
        
       
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < nums[(mid-1+n)%n] and nums[mid] < nums[(mid+1)%n]:
              return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid+1
            else:
              right = mid-1
        return nums[0]
      
#     """
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.    
#     """
    def search(self, nums: List[int], target: int) -> int:
        left , right, n = 0, len(nums)-1, len(nums)
        
       
        while left <= right:
            mid = (left+right)//2
            if  nums[mid] == target:
              return target
            
            if nums[left] <= nums[mid]:
              if nums[left] <= target < nums[mid]:
                right = mid -1
              else:
                left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
      
if __name__ == "__main__":
  bs = BinarySearchSolution()
  print(bs.search([1],0))
      
      