import linkedlist.list
import linkedlist.Node as Node
class TwoPointers:
  def __init__(self):
    pass
  
  def validPallindrome(self, s:str) -> bool:
    left, right = 0, len(s)-1
    
    while left < right:
      if s[left] != s[right]:
        return False
      left = left+1
      right = right-1
    return True

  def find_sum_of_three(self, nums:list, target: int) -> bool:
    nums.sort()
    for i in range (0, len(nums)-2):
      low = i+1
      high = len(nums)-1
      while low < high:
        triplet = nums[i]+ nums[low]+ nums[high]
        if triplet == target:
          return True
        elif triplet < target:
          low +=1
        else:
          high -=1
    return False
  

      
if __name__ == "__main__":
  twoPointers = TwoPointers()
  list = linkedlist.list.LinkedList()
  
  response = twoPointers.removeNthFromEndOfTheList(list.head, 6)
  while response.next != None:
    print(response.next)
    response = response.next
    
  
  # print(twoPointers.validPallindrome("raceacar"))
  # print(twoPointers.find_sum_of_three([0,1,3,8,12],12))