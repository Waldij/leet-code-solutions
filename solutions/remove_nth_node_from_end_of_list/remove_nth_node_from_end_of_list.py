from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'Node[{self.val=}]'


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Recursion"""
        def remove(head_):
            if not head_:
                return 0, head_
            i, head_.next = remove(head_.next)
            return i + 1, (head_, head_.next)[i + 1 == n]

        return remove(head)[1]

    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Intuitive"""
        nodes = [head]
        node = head
        while node.next:
            node = node.next
            nodes.append(node)

        if len(nodes) == 1:
            return head
        elif n == len(nodes):
            return nodes[1]
        elif n == 1:
            nodes[-n - 1].next = None
            return head
        else:
            nodes[-n - 1].next = nodes[-n + 1]
        return head

    def get_nodes_list(self, head: Optional[ListNode]) -> list:
        nodes = [head]
        node = head
        while node.next:
            node = node.next
            nodes.append(node)
        return nodes

    def get_values(self, head: Optional[ListNode]) -> list:
        return [node.val for node in self.get_nodes_list(head)]


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    print(solution.get_values(head))
    new_head = solution.removeNthFromEnd(head, 1)
    print(solution.get_values(new_head))

    # 2
    head = ListNode(1)
    head.next = ListNode(2)

    print(solution.get_values(head))
    new_head = solution.removeNthFromEnd(head, 2)
    print(solution.get_values(new_head))


if __name__ == '__main__':
    main()
