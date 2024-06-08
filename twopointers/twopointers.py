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
  def swap(self, nums, i,j):
    nums[i], nums[j] = nums[j], nums[i]
    
    
  def sort_colors(self, nums:list ) ->list:
    start = current =0
    end = len(nums)-1
    while(current<=end):
      if nums[current] ==0:
        if nums[start] !=0:
          self.swap(nums, start, current)
        start = start+1
        current = current+1
      elif nums[current]==1:
        current= current+1
      elif nums[current]==2:
        self.swap(nums,current,end)
        end= end-1
    return nums
        
      
  def reverse_words_in_string(self, sentence:str) -> str:
      words = sentence.split()
      start, end = 0, len(words)-1
      while(start < end):
          words[start], words[end] = words[end], words[start]
          start = start+1
          end = end-1
      return " ".join(words[::1])
  def reverse_words_in_string_two(self,sentence:str) -> str:
      s = list(sentence)
      start =0
      for end in range(len(s)):
        if s[end] == ' ' or end == len(s)-1:
          left, right = start,end-1
          if end == len(s)-1:
            right = end
          while left < right:
            s[left],s[right] = s[right], s[left]
            left = left+1
            right = right-1
          start = end+1
      return "".join(s)
          
    
    
       
  
if __name__ == "__main__":
  twoPointers = TwoPointers()
  twoPointers.sort_colors([2,0,1])
  print(twoPointers.reverse_words_in_string_two("i am gowtham"))
  
  # print(twoPointers.validPallindrome("raceacar"))
  # print(twoPointers.find_sum_of_three([0,1,3,8,12],12))