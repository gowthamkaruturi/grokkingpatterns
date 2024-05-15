
import Node
class LinkedList:
  
  def __init__(self) -> None:
    self.head = None
  
  def insertAtBegining(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
  
  def printList(self):
  
    start = self.head
    while start:
      print(start.data)
      start = start.next
  
  def insert_at_end(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head= new_node
      return 
    last = self.head
    while last:
      last = last.next
    last.next = new_node
    
  def removeElementFromStartOfList(self):
    if self.head is  None:
      return 
    else:
      self.head = self.head.next
      
  def removeElementFromEndOfList(self):
    if self.head is  None:
      return 
    else:
      start = self.head
      while start.next is not None:
        start = start.next
      start = None
      
  def search_element(self,element):
    if self.head is None:
      return "element not found"
    start = self.head
    index =0
    while start.data == element:
      start = start.next
      index = index+1
    return "element "+ element + " found at "+index
    