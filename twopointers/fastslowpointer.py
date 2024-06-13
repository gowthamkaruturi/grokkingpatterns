class Solution():
  def __init__():
    pass
  
  
  def sumofSquareOfNumbers(self, n:int) -> int:
    sum = 0 
    while n >0 :
      tobeSquared = n %10
      sum = sum + (tobeSquared * tobeSquared)
      n = n /10
    return sum

  def isHappy(self, n:int)->bool:
    slowPointer = n
    fastPointer = self.sumofSquareOfNumbers(n)
    while slowPointer != fastPointer and fastPointer != 1 :
      slowPointer = self.sumofSquareOfNumbers(slowPointer)
      fastPointer = self.sumofSquareOfNumbers(self.sumofSquareOfNumbers(fastPointer))
    return fastPointer ==1 

if __name__ == "__main___":
    sol = Solution()
    print(sol.isHappy(19))