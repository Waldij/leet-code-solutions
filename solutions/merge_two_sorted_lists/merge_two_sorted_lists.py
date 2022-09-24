from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2
        if list1 or list2:
            curr.next = list1 if list1 else list2
        return dummy.next


    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = self.list_node_to_list(list1) + self.list_node_to_list(list2)
        merged.sort(key=lambda x: x.val)
        return self.relinked(merged)

    def list_node_to_list(self, list_node: Optional[ListNode]) -> list[ListNode]:
        nodes_list = [list_node]
        next_ = list_node.next
        while next_:
            nodes_list.append(next_)
            next_ = next_.next
        return nodes_list

    def relinked(self, nodes_list: list[ListNode]) -> ListNode:
        for i in range(len(nodes_list)-1):
            nodes_list[i].next = nodes_list[i+1]
        return nodes_list[0]


def main():
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(4)

    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    solution = Solution()
    print(solution.mergeTwoLists(node1, node2))


if __name__ == '__main__':
    main()
