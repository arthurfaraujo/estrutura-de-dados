# Brabor
from typing import Any, Optional
from stack.stack_error import StackError


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


class Stack:
    def __init__(self) -> None:
        self.__head: Optional[Node] = None
        self.__size = 0

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise StackError('pop from empty stack')

        node = self.__head
        assert node is not None
        self.__head = node.next
        self.__size -= 1
        return node.value

    def peek(self) -> Any:
        if self.is_empty():
            raise StackError('empty stack')

        return self.__head

    def is_empty(self) -> bool:
        return self.__head is None

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
