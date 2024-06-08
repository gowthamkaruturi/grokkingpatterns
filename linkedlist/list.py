
import Node as Node
class LinkedList:
  
  def __init__(self) -> None:
    self.head = None
  
  def insert_at_begining(self, new_data):
    new_node = Node.Node(new_data)
    new_node.next = self.head
  
  def print_list(self):
  
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
    
  def remove_element_from_start(self):
    if self.head is  None:
      return 
    else:
      self.head = self.head.next
      
  def remove_element_from_end(self):
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
    
  def removeNthFromEndOfTheList(self,head:Node.Node, n :int)-> Node.Node:
  
    slow = head
    fast = head
    for i in range(n):
      fast= fast.next
    if not fast:
      return head
    while fast.next!= None:
      fast = fast.next
      slow = slow.next
      
    slow.next = slow.next.next
    return head

if __name__ == "__main__":
   list = LinkedList()
   list.insert_at_begining(Node.Node(69))
   list.insert_at_begining(Node.Node(8))
   list.insert_at_begining(Node.Node(49))
   list.insert_at_begining(Node.Node(106))
   list.insert_at_begining(Node.Node(116))
   list.insert_at_begining(Node.Node(113))
   response = list.removeNthFromEndOfTheList(list.head, 6)
   while response.next is not None:
     print(response.data)
     response = response.next
   