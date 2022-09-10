from typing import Any


class Node:
    def __init__(self, data: Any = None):
        self.data = data
        self.next = None
        self._length = 1 if data else 0

    def append(self, data) -> None:
        if not self.data:
            self.data = data
            self._length += 1
        else:
            new_node = Node(data)
            s = self
            while s.next:
                s = s.next
            s.next = new_node
            self._length += 1

    def _set_node(self, node) -> None:
        self.data = node.data
        self.next = node.next

    def __str__(self) -> str:
        return f'Node({self.as_list()})'

    def as_list(self) -> list[Any]:
        as_list = [self.data]
        s = self
        while s.next:
            s = s.next
            as_list.append(s.data)
        return as_list

    def __len__(self) -> int:
        return self._length
