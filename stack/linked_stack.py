# Brabor
from typing import Optional, Any
class StackError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)

class Node:
    def __init__(self, value: Any, next: Optional['Node'] = None) -> None:
        self.__value = value
        self.__next = next

    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, value: Any) -> None:
        self.__value = value

    @property
    def next(self) -> Optional['Node']:
        return self.__next

    @next.setter
    def next(self, next: Optional['Node']) -> None:
        self.__next = next

    def __repr__(self) -> str:
        return f'{self.__value}'

    def __str__(self) -> str:
        return f'{self.__value}'


class StackIterator:
    def __init__(self, head: Node | None):
        self.__current: Node | None = head

    def __next__(self) -> Any:
        if not self.__current:
            raise StopIteration

        node = self.__current
        assert node is not None
        self.__current = node.next

        return node.value

    def __iter__(self) -> 'StackIterator':
        return self


class Stack:
    def __init__(self) -> None:
        self.__head: Optional[Node] = None
        self.__size = 0

    @classmethod
    def join(cls, stack1: 'Stack', stack2: 'Stack') -> 'Stack':
        joined = Stack()
        st1_empty = stack1.is_empty()
        st2_empty = stack2.is_empty()

        if st1_empty and st2_empty:
            raise StackError('invalid join with two empty stacks')

        if st1_empty:
            return stack2

        if st2_empty:
            return stack1

        for node in stack2:
            joined.push(node)

        for node in stack1:
            joined.push(node)

        joined.invert()

        return joined

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1

    def pop(self) -> Node:
        if self.is_empty():
            raise StackError('pop from empty stack')

        node = self.__head
        assert node is not None
        self.__head = node.next
        self.__size -= 1
        return node

    def peek(self) -> Node:
        if self.is_empty():
            raise StackError('empty stack')

        assert self.__head is not None
        return self.__head

    def is_empty(self) -> bool:
        return self.__size == 0

    def invert(self) -> None:
        if self.is_empty():
            raise StackError('invert empty stack')

        curr = None
        size = self.__size

        while not self.is_empty():
            node = self.pop()
            node.next = curr
            curr = node

        self.__head = curr
        self.__size = size

    def empty(self) -> None:
        self.__head = None
        self.__size = 0

    def concat(self, stack: 'Stack') -> None:
        if stack.is_empty() or self.is_empty():
            raise StackError('impossible to concatenate with an empty stack')

        for node in reversed(stack):
            self.push(node)

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        nodes = ''

        if not self.is_empty():
            node: Optional[Node] = self.__head

            while node:
                nodes += str(node.value) + ' -> '
                node = node.next

        return nodes.rstrip(' -> ') if self.__size else 'Pilha vazia'

    def __iter__(self) -> StackIterator:
        return StackIterator(self.peek())

    def __reversed__(self) -> StackIterator:
        rev = Stack()

        for node in self:
            rev.push(node)

        return StackIterator(rev.peek())
