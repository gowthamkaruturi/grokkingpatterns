from twopointers.ReverselinkedList import reverse_linked_list


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
  def checkIfStringContainsPallindrome(self, s:str) -> bool:
    left=0
    right =len(s)-1
    while left < right:
      if s[left] == s[right]:
        left = left+1
        right = right-1
      else:
        return self.valid_Pallindrome(s, left+1, right) or self.valid_Pallindrome(s, left, right-1)
  def valid_Pallindrome(self, s:str, left:int, right:int) -> bool:
 
    
    while left < right:
      if s[left] != s[right]:
        return False
      left = left +1
      right = right-1
    return True  
    
  def sumofSquareOfNumbers(self, n:int) -> int:
    sum = 0 
    while n >0 :
      tobeSquared = n %10
      sum = sum + (tobeSquared * tobeSquared)
      n = n //10
    return sum

  def isHappy(self, n:int)->bool:
    slowPointer = n
    fastPointer = self.sumofSquareOfNumbers(n)
    while slowPointer != fastPointer and fastPointer != 1 :
      slowPointer = self.sumofSquareOfNumbers(slowPointer)
      fastPointer = self.sumofSquareOfNumbers(self.sumofSquareOfNumbers(fastPointer))
    return fastPointer ==1       
  
  # def detect_cycle(self, head:Node.Node) -> Node.Node:
  #  fast = head 
  #  slow = head
  #  while fast is not None and fast.next is not None :
  #     slow= slow.next
  #     fast = fast.next.next
  #     if fast == slow :
  #        return True
       
       
  # def get_middle_node(self , head:Node.Node)-> Node.Node:
  #   fast = slow= head
  #   while fast is not None and fast.next is not None:
  #       slow = slow.next
  #       fast = fast.next.next
  #   # Replace this placeholder return statement with your code
  #   return slow 
  
  def getNextIndex(self, isForward:bool,index:int,nums:list) -> int:
    direction= False
    if nums[index]>=0:
      direction = True
    if direction != isForward:
      return -1
    nextIndex = (index+nums[index])%len(nums)
    if nextIndex <0:
      nextIndex = nextIndex+len(nums)
    if nextIndex == index:
      return -1
    return -1
  
  def findCircularArrayLoop(self, nums:list)->bool:
    for i in range(len(nums)):
      slow= fast =i
      isForward = (i>=0)
      while True:
        slow = self.getNextIndex(isForward, slow, nums)
        if slow == -1:
          break
        fast = self.getNextIndex(isForward, fast, nums)
        if fast == -1:
          break
        fast = self.getNextIndex(isForward, fast, nums)
        if fast == -1:
          break
        if fast == slow:
          return True
        
    return False
  
  def findDuplicateNumbers(self, nums:list)->int:
    slow = fast = nums[0]
    while True:
      slow = nums[slow]
      fast = nums[nums[fast]]
      if fast == slow:
        break
    slow = nums[0]
    while slow != fast:
        slow= nums[slow]
        fast = nums[fast]
    return fast    
      
  def compareTwoHalves(self, head, rev)->bool:
    while head and rev:
        if head.data != rev.data:
            return False
        head = head.next
        rev = rev.next
    return True
  
  def palindrome(self, head):   
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    rev_lst = reverse_linked_list(slow) 
    print(rev_lst)
    # Replace this placeholder return statement with your code
    return self.compareTwoHalves(head, rev_lst)
  
if __name__ == "__main__":
  twoPointers = TwoPointers()
  print(twoPointers.isHappy(19))
  nums = [1,2,-3,3,4,7,1]
  twoPointers.findCircularArrayLoop(nums=nums)
  # twoPointers.sort_colors([2,0,1])
  # print(twoPointers.reverse_words_in_string_two("i am gowtham"))
  
  # print(twoPointers.validPallindrome("raceacar"))
  # print(twoPointers.find_sum_of_three([0,1,3,8,12],12))