class Solution:
  def __init__(self) -> None:
    pass
  
  def medianOfArray(self, nums:list[int]) -> int:
    if len(nums)%2==1:
      return nums[len(nums)//2]
    else:
      return (nums[len(nums)//2]+nums[len(nums)//2-1])/2

  def mergeSort(self, arr1:list[int], arr2:list[int]) -> list[int]:
    l
  
if __name__ =="__main__":
  sol = Solution()
  print(sol.medianOfArray([9,8,8,7]))