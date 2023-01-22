from typing import Any

from data_structures.linked_list import Node


class Stack(Node):
    def pop(self) -> Any:
        data = self.data
        self._set_node(self.next)
        self._length -= 1
        return data

    def peek(self) -> Any:
        """Returns top data without pop. """
        return self.data

    def is_empty(self) -> bool:
        return self._length == 0

    def __str__(self) -> str:
        return f'Stack({self.as_list()})'


def main():
    pass


if __name__ == '__main__':
    main()
