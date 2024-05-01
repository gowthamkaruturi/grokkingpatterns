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
    
    def findMin(self, nums:List[int])->int:
        min , max = 0, len(nums)-1
        if nums[min] < nums[max]:
            return nums[min]
        while min <= max:
            mid = (min+max)//2
