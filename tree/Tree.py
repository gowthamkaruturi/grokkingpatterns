class Node:
  def __init__(self, data:int) -> None:
    self.right = None
    self.left = None
    self.data = data
  
  def insert(self, value:int) ->None:
    if value< self.data:
      if self.left is None:
        self.left = Node(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = Node(value)
      else:
        self.right.insert(value=value)
  
  def contains(self, value:int) -> bool:
    if value == self.data:
      return True
    elif value < self.data:
      if self.left is None:
        return False
      else:
        self.left.contains(value)
    else:
      if self.right is None:
        return False
      else:
        self.right.contains(value)  
              
  def printInOrder(self)->None:
    if self.left is not None:
      self.left.printInOrder()
    print(self.data)    
    if self.right is not None:
      self.right.printInOrder()
    