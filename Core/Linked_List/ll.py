class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Linked_List:
  def __init__(self):
    self.head = None

  def append(self,data): # like the insert function in python
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head # so here we are using the  last_node(just a variable name) to traverse the list
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def print_list(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data,cur_node.next)
      cur_node = cur_node.next
    
  def prepend(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def postpend(self,data):
    if self.head is None:
      self.head = new_node
      return
    new_node = Node(data)
    last_node = self.head # traversing to reach the last node
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def delete_beg(self,key): # key is the linked list && not needed as it is added to the  delete
    if self.head is None:
      return "Before deleting append something!!!"
    cur_node = self.head
    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      cur_node = None 
      return
    else:
      print("Key is not matching buddy")

  def delete(self,key):
    if self.head is None:
      return "Before deleting append something!!!"
    cur_node = self.head
    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      cur_node = None 
      return
    # else:
      # print("Key is not matching buddy")
    
    cur_node = self.head
    try:
      while cur_node.data != key:
        prev_node = cur_node
        cur_node = cur_node.next
    except:
      print("Key is not mapping well")
    if cur_node is None:
      return 
    # print(cur_node.data,cur_node.next)
    # print(prev_node.data,prev_node.next)
    if cur_node.next:
      prev_node.next = cur_node.next
      cur_node = None
    else:
      prev_node.next = None
      # print("No Match found for the given key")


llist = Linked_List()
llist.append("A")
llist.append("B")
llist.append("C")
llist.postpend("D")
llist.print_list()
print()
llist.delete_beg("D")
llist.print_list()
print()
llist.delete("C")
llist.delete("A")
llist.delete("D")
llist.delete("A")
llist.print_list()
print()