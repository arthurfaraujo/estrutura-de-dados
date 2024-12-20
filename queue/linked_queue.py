from stack.linked_stack import Node
from typing import Optional, Any

class QueueError(Exception):
  def __init__(self, msg: str):
    super().__init__(msg)

class Control:
  def __init__(self, head: Optional[Node] = None, tail: Optional[Node] = None) -> None:
    self.head = head
    self.tail = tail
    

class Queue:
  def __init__(self)  -> None:
    self.__control = Control()
    self.__size = 0
    
  def enqueue(self, item: Any) -> None:
    """Adds an item to the end of the queue."""
    
    node = Node(item)
    if self.is_empty():
      self.__control.head = node
    else:
      assert self.__control.tail is not None
      self.__control.tail.next = node
    
    self.__control.tail = node
    self.__size += 1

  def dequeue(self) -> Any:
    """Remove and returns from the queue start"""
    
    if not self.is_empty():
      assert self.__control.head is not None
      
      head = self.__control.head      
      self.__control.head = self.__control.head.next      
      head.next = None
      self.__size -= 1
      
      return head.value
    
    raise QueueError('can not remove from empty queue')
    
  def peek(self) -> Any:
    if not self.is_empty():
      assert self.__control.head is not None
      
      return self.__control.head.value
    
    raise QueueError('can not peek from empty queue')
  
  def index(self, key: Any) -> Any:
    if not self.is_empty():
      count = 1
      node = self.__control.head

      while node:
        if node.value == key:
          return count
        count += 1
      
      
  
  @property
  def size(self) -> int:
    return self.__size
    
  def is_empty(self)-> bool:
    return self.__size == 0
  
  def __str__(self) -> str:
    nodes = '(head) '

    if not self.is_empty():
        node: Optional[Node] = self.__control.head

        while node:
            nodes += str(node.value) + ' -> '
            node = node.next
            
    nodes = nodes.rstrip(' -> ')
    nodes += " (tail)"
    return nodes if self.__size else 'empty queue'
